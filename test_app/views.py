from rest_framework import serializers, generics
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets


# # Fa la GET ALL e la POST
# class SimpleGenerics(generics.ListCreateAPIView):
#     queryset = TestModel.objects.all()
#     serializer_class = SimpleSerializer

# # Fa la PUT o PATCH
# class SimpleGenericsUpdate(generics.ListCreateAPIView):
#     queryset = TestModel.objects.all()
#     serializer_class = SimpleSerializer
#     # altrimenti nella url devo passare il parametro di
#     # defaulti 'pk' invece di 'id
#     lookup_field = "id"


# metodo verbose per definire le API
# class Simple(APIView):

#     def post(self, request):
#         # Serializzo prima quanto ricevuto dal cliente nei FORM DATA
#         serializers = SimpleSerializer(data=request.data)
#         # notifico automaticamente il client in caso di errori di validazione nei dati ricevuti
#         serializers.is_valid(raise_exception=True)
#         serializers.save()  # chiama il metodo Create del Serializer
#         return JsonResponse({"data": serializers.data})

#     def get(self, request):
#         content = TestModel.objects.all()
#         return JsonResponse({'data': SimpleSerializer(content, many=True).data})

#     def put(self, request, *args, **kwargs):
#         model_id = kwargs.get("id", None)
#         if not model_id:
#             return JsonResponse({"error": "method /PUT/ not alloed"})

#         try:
#             instance = TestModel.objects.get(id=model_id)
#         except:
#             return JsonResponse({"error": f"object with id '{model_id}' does not exists"})
#         # credo che passare l'instance sia ridondante, provato senza e funziona
#         serializers = SimpleSerializer(data=request.data, instance=instance)
#         # notifico automaticamente il client in caso di errori di validazione nei dati ricevuti
#         serializers.is_valid(raise_exception=True)
#         serializers.save()  # chiama il metodo Create del Serializer
#         return JsonResponse({"data": serializers.data})
