
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

from API.serializers import CharacterSerializer
from API.models import Character

@authentication_classes([])
@permission_classes([])
class CharacterViewSet(viewsets.ModelViewSet):
    
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer