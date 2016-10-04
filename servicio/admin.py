from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import *
from easy_select2 import select2_modelform


RegistrosForm = select2_modelform(Registros, attrs={'width': '250px'})

class RegistrosAdmin(admin.ModelAdmin):
    form = RegistrosForm


ProfesoresByIntitucionesForm = select2_modelform(ProfesoresByIntituciones, attrs={'width': '250px'})

class ProfesoresByIntitucionesAdmin(admin.ModelAdmin):
    form = ProfesoresByIntitucionesForm


CuposForm = select2_modelform(Cupos, attrs={'width': '400px'})

class CuposAdmin(admin.ModelAdmin):
    form = CuposForm


class AlumnosAdmin(admin.ModelAdmin):
    search_fields = ['cedula', 'nombres', 'apellidos']


admin.site.register(Alumnos, AlumnosAdmin)
admin.site.register(Profesores)
admin.site.register(Perido)
admin.site.register(ProfesoresByIntituciones, ProfesoresByIntitucionesAdmin)
admin.site.register(Instituciones)
admin.site.register(Facultad)
admin.site.register(Registros, RegistrosAdmin)
admin.site.register(Cupos, CuposAdmin)