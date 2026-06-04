from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    edad_libro = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'anio_publicacion' ,'edad_libro']

    def validate_anio_publicacion(self, value):
        if value > 2026:
            raise serializers.ValidationError(
                "El año de publicación no puede ser futuro"
            )
        return value
    
    def validate_autor(self, value):
        if value == "Paulo Coelho":
            raise serializers.ValidationError(
                "Respeto!, esta es una biblioteca respetable"
            )
        return value
    
    def validate(self, data):
        if data.get('titulo') != None and len(data['titulo']) < 3:
            raise serializers.ValidationError(
                "El título debe tener al menos 3 caracteres"
            )
        return data
    
    def get_edad_libro(self, obj):
        from datetime import datetime
        return datetime.now().year - obj.anio_publicacion
    