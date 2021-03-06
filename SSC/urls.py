from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from servicio.views import *

urlpatterns = [
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^$', Index.as_view()),
    url(r'^buscar_estudiante/', buscar_estudiante),
    url(r'^crear_estudiante/', crear_estudiante),
    url(r'^cupos_disponibles/', cupos_disponibles),
    url(r'^Inscribirse/', Inscribirse),
    url(r'^poner_tutor/', poner_tutor_v),
    url(r'^servicio/(?P<pk>[0-9]+)', Servicio.as_view()),
    url(r'^reportes/', login_required(Reporte.as_view())),
    url(r'^InformeEstudiantesEnInstituciones.pdf/(?P<periodo_id>\d+)/(?P<institucion_id>\d+)/(?P<facultad_id>\d+)/$',
        login_required(ReporteIntitucionPeriodo.as_view())
    ),
]
