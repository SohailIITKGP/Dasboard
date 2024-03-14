from rest_framework import serializers
from .models import Jsondata

class JsondataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jsondata
        fields = '__all__'
