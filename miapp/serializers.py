from rest_framework import serializers #Import the REST Framework serializer
from .models import Hero #Importar modelo Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer): #class that links the Hero with its serializer
    class Meta:
        model = Hero
        fields = ('name', 'alias')
