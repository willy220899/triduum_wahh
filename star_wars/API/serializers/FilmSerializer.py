
from rest_framework import serializers

from API.models import Film
from API.serializers import PlanetSerializer, CharacterSerializer

class FilmSerializer(serializers.ModelSerializer):
    planetas = PlanetSerializer(source='planets', many=True, read_only=True)
    Characters = CharacterSerializer(source='characters', many=True, read_only=True)
    
    class Meta:
        model = Film
        fields = '__all__'
        extra_kwargs = {
            'planets': {'write_only': True},
            'Characters': {'write_only': True}
        }
    
    def get_queryset(self):
        queryset = super().get_queryset()

        character_id = self.request.GET.get('character_id')
        if character_id:
            queryset = queryset.filter(characters__contains=[int(character_id)])

        return queryset