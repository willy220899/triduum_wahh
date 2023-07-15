
from rest_framework import serializers

from API.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Character
        fields = '__all__'
        