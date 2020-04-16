from rest_framework import serializers
from .models import Emplo,Rating

class EmploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emplo
        fields = ('id','name','descriptions',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','emplo','prof','character','user',)