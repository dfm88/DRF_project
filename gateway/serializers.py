from rest_framework import serializers

# Creo 3 serializer per tornare la risposta in caso di
# - LOGIN
# - REGISTRAZIONE
# - REFRESH del TOKEN

# - LOGIN
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# - REGISTRAZIONE
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()

# - REFRESH del TOKEN
class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
