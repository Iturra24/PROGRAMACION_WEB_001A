from .models import Usuario, Juego, Categoria
from rest_framework import serializers

# Serializer de Usuario
# Para poder ocuparlo en el login
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# Serializer de Juego
class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'


# Serializer de Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'




