# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from videojuegos.models import Genero, Clasificacion, Juego

# Register your models here.
admin.site.register(Genero)
admin.site.register(Clasificacion)
admin.site.register(Juego)
