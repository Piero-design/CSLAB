from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField()
    duenio = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre} ({self.especie})"