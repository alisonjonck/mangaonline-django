from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from django import forms
from django.shortcuts import render

def usuario(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'usuario.html', {
        'form': form,
    })

class FormUsuario(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

class FormSocioeconomico(forms.Form):
    nome_pai = forms.CharField(max_length=50)
    email_pai = forms.EmailField(required=False)
    nome_mae = forms.CharField(max_length=50)
    email_mae = forms.EmailField(required=False)

class FormCadastro(forms.Form):
    nome = forms.CharField()
    sobrenome = forms.CharField()
    data_nascimento = forms.DateField()
    nome_pai = forms.CharField()
    nome_mae = forms.CharField()
    email = forms.EmailField(required=False)
    senha = forms.CharField(widget=forms.PasswordInput)
    rua = forms.CharField()
    numero_casa = forms.IntegerField()
    bairro = forms.CharField()
    
    cep = forms.CharField()
    rg = forms.CharField()
    cpf = forms.CharField()
    sexo = forms.TypedChoiceField(
                   coerce=lambda x: True if x == 'True' else False,
                   choices=((False, 'Femenino'), (True, 'Masculino')),
                   widget=forms.RadioSelect,
                   initial='True',
                )
    estado_civil = forms.TypedChoiceField(
                   coerce=lambda x: True if x == 'True' else False,
                   choices=((False, 'Solteiro'), (True, 'Casado')),
                   widget=forms.RadioSelect,
                   initial='False',
                )
    telefone_residencial = forms.CharField()
    telefone_celular = forms.CharField()
    cidade = forms.CharField()

class FormFormulario(forms.Form):
    etnia = forms.TypedChoiceField(
                   choices=((1, 'Branca'), (2, 'Negra'), (3, 'Amarela')),
                   widget=forms.RadioSelect,
                   required=False
                )
    moradia1 = forms.CharField()
    moradia2 = forms.CharField()
    mora_com_quem = forms.CharField()
    mora_quantas_pessoas = forms.IntegerField()
    
    meio_transporte = forms.TypedChoiceField(
                   choices=((1, 'Veiculo proprio'), (2, 'Transporte publico'), (3, 'Outros')),
                   widget=forms.RadioSelect,
                   required=False
                )
    atividade_remunerada = forms.TypedChoiceField(
                   coerce=lambda x: True if x == 'True' else False,
                   choices=((False, 'Nao'), (True, 'Sim')),
                   widget=forms.RadioSelect,
                   initial='False'
                )

    renda_mensal_individual = forms.DecimalField(max_digits = 12, decimal_places=2)
    pais_conjuge_falescidos = forms.TypedChoiceField(
                   coerce=lambda x: True if x == 'True' else False,
                   choices=((False, 'Nao'), (True, 'Sim')),
                   widget=forms.RadioSelect,
                   initial='False'
                )
    situacao_conjugal_pais = forms.TypedChoiceField(
                   choices=((1, 'Solteiro'), (2, 'Casado'), (3, 'Separado'), (2, 'Divorciado'), (3, 'Viuvo')),
                   widget=forms.RadioSelect,
                   required=True,
                   initial='1'
                )

    filhos = forms.TypedChoiceField(
                   coerce=lambda x: True if x == 'True' else False,
                   choices=((False, 'Nao'), (True, 'Sim')),
                   widget=forms.RadioSelect,
                   initial='False'
                )
    pensao_filhos_ex = forms.DecimalField(max_digits = 12, decimal_places=2)
    bolsa_academica = forms.DecimalField(max_digits = 12, decimal_places=2)

from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User

def adicionar_usuario(request):
    #formUsuario = FormUsuario()
    formUsuario = FormCadastro()
    return render_to_response(
        'usuario.html',
        locals(),
        context_instance=RequestContext(request)
        )

def adicionar_socioeconomico(request):
    #formSocioeconomico = FormSocioeconomico()
    formSocioeconomico = FormFormulario()
    return render_to_response(
        'socioeconomico.html',
        locals(),
        context_instance=RequestContext(request)
        )