# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class tipousuario(models.Model):
	nombre = models.CharField(max_length=50)

class usuario(models.Model):
	nombre = models.CharField(max_length=50)
	tipousuario = models.ForeignKey(tipousuario, null=True, blank=True, on_delete=models.CASCADE)