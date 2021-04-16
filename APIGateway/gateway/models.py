from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import os
# Create your models here.

class Data(models.Model):
    # token = models.CharField(unique=True,max_length=200,)
    failur_numbers = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(0)],blank=True)
    stop_request = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)],blank=True)
   


    class Meta:
        verbose_name_plural = "Data"

