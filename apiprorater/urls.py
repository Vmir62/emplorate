from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import EmploViewSet, RatingViewSet


router = routers.DefaultRouter()
router.register('emplos',EmploViewSet)
router.register('ratings',RatingViewSet)

urlpatterns = [
    path('', include (router.urls)),
]
