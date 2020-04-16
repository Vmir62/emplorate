from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Emplo(models.Model):
    name = models.CharField(max_length=48,)
    descriptions = models.TextField(max_length=512,)


class Rating(models.Model):
    emplo = models.ForeignKey(Emplo, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    prof = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10),])
    character = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10),])

    class Meta:
        unique_together = (('user', 'emplo'), )
        index_together = (('user', 'emplo'), )
