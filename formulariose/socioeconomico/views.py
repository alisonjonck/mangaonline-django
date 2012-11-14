from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from django import forms
#from socioeconomico.models import Cadastro,Pergunta,Escolha

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User

def adicionar_usuario(request):
    form = FormContato()
    return render_to_response(
        'usuario.html',
        locals(),
        context_instance=RequestContext(request)
        )

def adicionar_socioeconomico(request):
    form = FormContato()
    return render_to_response(
        'socioeconomico.html',
        locals(),
        context_instance=RequestContext(request)
        )