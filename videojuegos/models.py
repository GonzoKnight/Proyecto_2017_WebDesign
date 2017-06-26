# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Genero(models.Model):
	nombre = models.CharField(max_length=50)

class Clasificacion(models.Model):
	nombre = models.CharField(max_length=50)

class Juego(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=144)
	imagen = models.ImageField(null=True, blank=True)
	genero = models.ForeignKey(Genero, null=True, blank=True, on_delete=models.CASCADE)
	clasificacion = models.ForeignKey(Clasificacion, null=True, blank=True, on_delete=models.CASCADE)
	