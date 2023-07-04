
from rest_framework import serializers

from API.models import Film
from API.serializers import PlanetSerializer

class FilmSerializer(serializers.ModelSerializer):
    planetas = PlanetSerializer(source='planets', many=True, read_only=True)
    
    class Meta:
        model = Film
        fields = '__all__'
        extra_kwargs = {
            'planets': {'write_only': True}
        }