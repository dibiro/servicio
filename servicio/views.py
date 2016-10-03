# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import HttpResponse, render
from .models import * 
import json
from django.conf import settings as _settings
from django.contrib.auth import login, logout, authenticate
from django.core.mail import get_connection, send_mail, BadHeaderError
from datetime import datetime, date, timedelta


def corte_actual():
    return Perido.objects.get(actual=True)


def login_view(request):
    logout(request)
    username = password = ''
    next = ""
    redirect_to = getattr(_settings, 'LOGIN_REDIRECT_URL', None)
    if request.GET:
        next = request.GET['next']
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next == "":
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/')
    return render(
        request,
        'login.html',
        {
            'username': username,
            'next': next,
        },
    )


class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


class Servicio(TemplateView):
    template_name = "servicio.html"

    def get(self, request, pk, *args, **kwargs):
        alumnos = Alumnos.objects.get(cedula=pk)
        if alumnos.fecha_de_nacimiento is not None:
            alumnos.fecha_de_nacimiento = alumnos.fecha_de_nacimiento.strftime('%Y-%m-%d')
        cortes = Registros.objects.filter(estudiante=alumnos)
        intituciones = Instituciones.objects.filter(estado="1", cupos_disponibles__gte=0)
        actual = corte_actual()
        corte = 0
        for x in cortes:
            if x.periodo == actual:
                corte = 1
        if Registros.objects.filter(estudiante=alumnos, estado="3").exists():
            corte = 1
        return render(request, self.template_name, locals())


def buscar_estudiante(request):
    existe = 0
    corte = 0
    dicc = {}
    lista = []
    alumnos = Alumnos.objects.filter(cedula=request.GET['cedula'])
    if len(alumnos) > 0:
        existe = 1
        alumno = alumnos[0]
        registros = Registros.objects.filter(estudiante=alumno)
        for x in registros:
            if x.periodo == corte_actual():
                corte = 1
            dicc = {
                'id': x.id,
                'periodo': x.periodo.periodo,
                'estado': x.estado
            }
            lista.append(dicc)
            dicc = {}
    dicc = {
        'existe': existe,
        'corte': corte,
        'lista_corte': lista
    }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def crear_estudiante(request):
    mensaje = ''
    if not Alumnos.objects.filter(cedula=request.POST['cedula']).exists():
        alumno = Alumnos(
            cedula=request.POST['cedula'],
            nombres=request.POST['nombres'],
            apellidos=request.POST['apellidos'],
            telefono1=request.POST['telefono1'],
            telefono2=request.POST['telefono2'],
            direccion=request.POST['direccion'],
            email=request.POST['email'],
            sexo=request.POST['sexo'],
            fecha_de_nacimiento=request.POST['fecha_de_nacimiento'],
        )
        alumno.save()
        mensaje = 'Guardado'
    else:
        mensaje = 'Alumno Ya Existe'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def cupos_disponibles(request):
    cupos = Instituciones.objects.get(id=request.GET['id'])
    result = json.dumps(cupos.cupos_disponibles, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def Inscribirse(request):
    mensaje = 0
    corte = 0
    registro = Registros.objects.filter(estudiante_id=request.POST['id_estudiante'])
    for x in registro:
        if x.periodo == corte_actual():
            corte = 1
        if x.estado == '3':
            corte = 1
    if corte == 0:
        institution = Instituciones.objects.get(id=request.POST['id_institucion'])
        if institution.cupos_disponibles > 0:
            registro = Registros(
                estudiante_id=request.POST['id_estudiante'],
                intitucion_id=request.POST['id_institucion'],
                periodo=corte_actual(),
                estado="2",
            )
            registro.poner_tutor()
            registro.save()
            institution.cupos_disponibles = institution.cupos_disponibles - 1
            institution.save()
            mensaje = 1
        else:
            mensaje = 2
    else:
        mensaje = 3
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def poner_tutor_v(request):
    registro = Registros.objects.get(id=request.POST['id'])
    dicc = { 'dato': registro.poner_tutor() }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')

