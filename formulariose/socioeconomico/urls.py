from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
#from socioeconomico.models import Cadastro
from django.conf import settings

urlpatterns = patterns('',

    url(r'^usuario/$', 'socioeconomico.views.adicionar_usuario'),
    url(r'^socioeconomico/$', 'socioeconomico.views.adicionar_socioeconomico'),
)