import jwt
from .models import Jwt
from user.models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .authentication import Authentication
from rest_framework.permissions import IsAuthenticated


def get_random(length):
    """[Restituisce un random token come stringa]
    Returns:
        [type]: [token]
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    """[Contiene l'informazione dell'user logato]

    Args:
        payload 

    Returns:
        [type]: [l'informazione del Jwt]
    """
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5),
         ** payload},  # scade in 5 minuti
        settings.SECRET_KEY,
        algorithm="HS256"
    )


def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        # validiamo tramite serializer il formato di Username e Password
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # django module to check encrypted password (from django.contrib.auth import authenticate)
        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password'])

        #se l'user non esiste
        if not user:
            return Response({"error": "Invalid email or password"}, status="400")

        Jwt.objects.filter(user_id=user.id).delete()

        access = get_access_token(payload={"user_id": user.id})
        refresh = get_refresh_token()

        # salvo le informazioni nel DB tramite modello Jwt
        Jwt.objects.create(
            user_id=user.id, access_token=access, refresh_token=refresh
        )

        return Response({"access": access, "refresh": refresh})


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({"success": "User created."})

# torna un token aggiornato in caso sia scaduto
class RefreshView(APIView):
    serializer_class = RefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # get dell'attuale 'refresh token'
            active_jwt = Jwt.objects.get(
                refresh=serializer.validated_data["refresh"])
        # verifica esistenza e validitò
        except Jwt.DoesNotExist:
            return Response({"error": "refresh token not found"}, status="400")
        if not Authentication.verify_token(serializer.validated_data["refresh"]):
            return Response({"error": "Token is invalid or has expired"})

        # prendo l'user dal modello JWT (oneToOne Field)
        access = get_access_token({"user_id": active_jwt.user.id})
        refresh = get_refresh_token()

        active_jwt.access = access.decode()
        active_jwt.refresh = refresh.decode()
        active_jwt.save()

        return Response({"access": access, "refresh": refresh})


# from rest_framework.decorators import authentication_classes
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
# @authentication_classes(IsAuthenticated)
from rest_framework.permissions import IsAuthenticated
# classe per verificare il servizio di autenticazione
class GetSecuredInfo(APIView):
    permission_classes = [IsAuthenticated]
    #authentication_classes = [Authentication]

    def get(self, request): 
        print(request.user)
        return Response({"data": "This is a secured info"})
