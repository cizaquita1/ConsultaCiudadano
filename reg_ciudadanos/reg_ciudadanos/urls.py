"""reg_ciudadanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from restapi import views
from restapi.views import *
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'departamento', DepartamentoViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'identificacion', IdentificacionViewSet)
router.register(r'ciudadano', CiudadanoViewSet)


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^generar_pdf/$', views.generar_pdf, name='generar_pdf'),
	url(r'^detalle/(?P<ciudadano_id>[0-9]+)/$', views.ciudadano_detail, name='ciudadano_detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^consulta_ciudadano/', views.consulta_ciudadano, name='consulta_ciudadano'),
]
