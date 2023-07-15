
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

from API.serializers import FilmSerializer
from API.models import Film

@authentication_classes([])
@permission_classes([])
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        queryset = Film.objects.all()

        character_id = self.request.query_params.get('character_id')
        if character_id:
            queryset = queryset.filter(characters__id=character_id)

        return queryset