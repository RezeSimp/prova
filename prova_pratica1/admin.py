from django.contrib import admin

# Register your models here.
from .models import Materia, Voti, Studente

admin.site.register(Studente)
admin.site.register(Materia)
admin.site.register(Voti)