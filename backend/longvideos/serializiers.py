from rest_framework import serializers 
from .models import LongVideo

class LongVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongVideo
        fields = '__all__'  # '__all__' means all fields in the model