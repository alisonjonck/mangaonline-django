from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from django import forms
#from socioeconomico.models import Cadastro,Pergunta,Escolha

class FormUsuario(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

class FormSocioeconomico(forms.Form):
    nome_pai = forms.CharField(max_length=50)
    email_pai = forms.EmailField(required=False)
    nome_mae = forms.CharField(max_length=50)
    email_mae = forms.EmailField(required=False)

from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User

def adicionar_usuario(request):
    formUsuario = FormUsuario()
    return render_to_response(
        'usuario.html',
        locals(),
        context_instance=RequestContext(request)
        )

def adicionar_socioeconomico(request):
    formSocioeconomico = FormSocioeconomico()
    return render_to_response(
        'socioeconomico.html',
        locals(),
        context_instance=RequestContext(request)
        )