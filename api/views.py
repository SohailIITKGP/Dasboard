from rest_framework import viewsets
from .models import Jsondata
from .serializers import JsondataSerializer

class JsondataViewSet(viewsets.ModelViewSet):
    queryset = Jsondata.objects.all()
    serializer_class = JsondataSerializer
