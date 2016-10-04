from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db import models
from django.utils import timezone


class Perido(models.Model):
    periodo = models.CharField(max_length=50, unique=True)
    fecha_de_inicio = models.DateField()
    fecha_de_fin = models.DateField()
    actual = models.BooleanField(default=True)

    class Meta:
        db_table = 'Perido'
        verbose_name_plural = "Periodos"

    def save(self, *args, **kwargs):
        if self.actual:
            Perido.objects.all().update(actual=False)
        super(Perido, self).save(*args, **kwargs)
    
    def __unicode__(self):
        if self.actual:
            mensaje = "Este Es El Periodo Actual"
        else:
            mensaje = ""
        return '%s (%s)' % (self.periodo, mensaje)


class Facultad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'facultad'
        verbose_name_plural = "Facultades"

    def __unicode__(self):
        return '%s' % (self.nombre)


class Alumnos(models.Model):
    SEX_CHOICES = (("1", "Masculino"), ("2", "Femenino"))
    cedula = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono1 = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    facultad = models.ForeignKey(Facultad, blank=True, null=True)

    def get_sex(self):
        if self.sexo == '1':
            return u"Masculino"
        elif self.sexo == '2':
            return u"Femenino"

    class Meta:
        db_table = 'alumnos'
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return '%s (%s %s)' % (self.cedula, self.nombres, self.apellidos)


class Profesores(models.Model):
    SEX_CHOICES = (("1", "Masculino"), ("2", "Femenino"))
    cedula = models.CharField(max_length=50, unique=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono1 = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)

    def get_sex(self):
        if self.sexo == '1':
            return u"Masculino"
        elif self.sexo == '2':
            return u"Femenino"

    class Meta:
        db_table = 'profesores'
        verbose_name_plural = "Profesores"

    def __unicode__(self):
        return '%s (%s %s)' % (self.cedula, self.nombres, self.apellidos)


class Instituciones(models.Model):
    TYPE_CHOICES = (("1", "Activo"), ("2", "Inactivo"), ("3", "Descartado"))
    nombre = models.CharField(max_length=500)
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=500)
    enlace = models.CharField(max_length=500)
    telefono_de_enlace = models.CharField(max_length=500)
    estado = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'escuelas'
        verbose_name_plural = "Instituciones"

    def __unicode__(self):
        return '%s, Telefono: %s, Direccion: %s)' % (self.nombre, self.telefono, self.direccion)


class Cupos(models.Model):
    cupos = models.IntegerField()
    periodo = models.ForeignKey(Perido)
    institucion = models.ForeignKey(Instituciones)
    facultad = models.ForeignKey(Facultad)

    def cupos_disponibles(self):
        return self.cupos - Registros.objects.filter(periodo=self.periodo, estudiante__facultad=self.facultad).count()

    class Meta:
        db_table = 'cupos'
        verbose_name_plural = "Cupos"
    
    def __unicode__(self):
        cupos_disponibles = self.cupos - Registros.objects.filter(periodo=self.periodo, estudiante__facultad=self.facultad).count()
        return 'Perido: %s, Institucion: %s, Facultad: %s, Cupos: %s, Cupos Disponibles: %s' % (self.periodo.periodo, self.institucion, self.facultad, self.cupos, cupos_disponibles)


class ProfesoresByIntituciones(models.Model):
    profesor = models.ForeignKey(Profesores)
    institucion = models.ForeignKey(Instituciones)
    periodo = models.ForeignKey(Perido)

    class Meta:
        db_table = 'profesores_by_intituciones'
        verbose_name_plural = "Profesors Asignados a Instituciones"

    def save(self, *args, **kwargs):
        super(ProfesoresByIntituciones, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Profesor: %s, institucion: %s, periodo: %s)' % (self.profesor, self.institucion, self.periodo)


class Registros(models.Model):
    STATUS_CHOICES = (("1", "Reguistrado"), ("2", "Asignado"), ("3", "Culminado"))
    estudiante = models.ForeignKey(Alumnos)
    tutor = models.ForeignKey(ProfesoresByIntituciones, blank=True, null=True)
    institucion = models.ForeignKey(Instituciones, blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_inicio = models.DateField(blank=True, null=True)
    fecha_de_fin = models.DateField(blank=True, null=True)
    periodo = models.ForeignKey(Perido)
    estado = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=True, null=True)

    def get_estado(self):
        if self.estado == '1':
            return u"Reguistrado"
        elif self.estado == '2':
            return u"Asignado"
        elif self.estado == '3':
            return u"Culminado"

    def poner_tutor(self):
        try:
            profesor = ProfesoresByIntituciones.objects.get(institucion=self.institucion, periodo=self.periodo)
            self.tutor = profesor
            self.save()
            return 1
        except:
            return 0

    class Meta:
        db_table = 'registros'
        verbose_name_plural = "Registros"

    def __unicode__(self):
        return 'Estudiante: %s, Tutor: %s, Escuela: %s)' % (self.estudiante, self.tutor, self.institucion)
