from django.db import models
import os

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    sobrenome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    telefone = models.CharField(max_length=11, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)

    def get_upload_handler(instance, filename):
        return os.path.join('static', 'fotos', filename)

    foto = models.ImageField(upload_to=get_upload_handler, blank=False, null=False)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=30, blank=False)
    bairro = models.CharField(max_length=15, blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)
    estado = models.CharField(max_length=10, blank=False, null=False)

    cliente = models.ForeignKey(Cliente, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+" "+self.estado +" " + self.cidade + " " + self.bairro + " - " + self.cliente.nome + " " + self.cliente.cpf


