from django.db import models
from django import forms

class Pais(models.Model):
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    nome = models.CharField(max_length=64)
    sigla = models.CharField(max_length=3)
    def __unicode__(self):
        return self.sigla
        
class Estado(models.Model):
    nome = models.CharField(max_length=64)
    pais = models.ForeignKey(Pais)
    def __unicode__(self):
        return self.nome
    
class Cidade(models.Model):
    nome = models.CharField(max_length=64)
    estado = models.ForeignKey(Estado)
    def __unicode__(self):
        return self.nome

class EstadoCivil(models.Model):
    class Meta:
        verbose_name_plural = 'Estado civil'
        verbose_name = 'Estado civil'
    nome = models.CharField(max_length=64)
    descricao = models.TextField(max_length=64)
    def __unicode__(self):
        return self.nome

class Cadastro(models.Model):
    class Meta:
        verbose_name_plural = 'Cadastros'
        verbose_name = 'Cadastro'
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    data_nascimento = models.DateField(max_length=64)
    nome_pai = models.CharField(max_length=64)
    nome_mae = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    senha = models.CharField(max_length=64)
    rua = models.CharField(max_length=64)
    numero_casa = models.IntegerField(max_length=64)
    bairro = models.CharField(max_length=64)
    
    cep = models.CharField(max_length=64)
    rg = models.CharField(max_length=64)
    cpf = models.CharField(max_length=64)
    sexo = models.BooleanField(max_length=64)
    
    
    estado_civil = models.ForeignKey(EstadoCivil)
    telefone_residencial = models.CharField(max_length=64)
    telefone_celular = models.CharField(max_length=64)
    cidade = models.ForeignKey(Cidade)

class Etnia(models.Model):
    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'
    nome = models.CharField(max_length = 64)
    descricao = models.TextField()
    
class MeioTransporte(models.Model):
    class Meta:
        verbose_name = 'Meio de transporte'
        verbose_name_plural = 'Meio de transporte'
    nome = models.CharField(max_length = 64)
    descricao = models.TextField()
    
class Formulario(models.Model):
    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'
    etnia = models.ForeignKey(Etnia)
    moradia1 = models.CharField(max_length=64)
    moradia2 = models.CharField(max_length=64)
    mora_com_quem = models.CharField(max_length=64)
    mora_quantas_pessoas = models.IntegerField(max_length=64)
    
    meio_transporte = models.ForeignKey(MeioTransporte)
    atividade_remunerada = models.BooleanField(max_length=64)

    renda_mensal_individual = models.DecimalField(max_digits = 12, decimal_places=2)
    pais_conjuge_falescidos = models.BooleanField(max_length=64)
    situacao_conjugal_pais = models.ForeignKey(EstadoCivil)
    filhos = models.BooleanField(max_length=64)
    pensao_filhos_ex = models.DecimalField(max_digits = 12, decimal_places=2)
    bolsa_academica = models.DecimalField(max_digits = 12, decimal_places=2)