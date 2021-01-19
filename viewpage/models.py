from django.db import models
from .listas import paises, provincias, tipopersona


# Create your models here.

class SociosSuscriptoresModel(models.Model):
    Socio_suscriptor=models.CharField(max_length=100,choices=(('Suscriptor', 'Suscriptor'), ('Socio', 'Socio')), default="Suscriptor")
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
    telefono=models.CharField(max_length=100)
    pais=models.CharField(max_length=100,choices=paises, default="Argentina")
    provincia=models.CharField(max_length=100,choices=provincias, default="CABA")
    lugar_de_residencia=models.CharField(max_length=100)
    nacimiento=models.DateField()
    tipo_de_persona=models.CharField(max_length=100,choices=tipopersona, blank=True, null=True, default="Socio persona que tartamudea")
    mensaje=models.TextField(blank=True, null=True)
    Comprobante_de_pago=models.ImageField(upload_to='images', default=None, blank=True, null=True)

    def __str__(self):
        return self.nombre


class ContactoModel(models.Model):
    nombre=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
    mensaje=models.TextField()

    def __str__(self):
        return "Consulta de " + self.nombre
    