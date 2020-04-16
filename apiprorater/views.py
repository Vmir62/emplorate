from django.shortcuts import render
from rest_framework import viewsets
from .models import Emplo, Rating
from .serializer import EmploSerializer, RatingSerializer


class EmploViewSet(viewsets.ModelViewSet):
    queryset = Emplo.objects.all()
    serializer_class = EmploSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer