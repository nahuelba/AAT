from django.db import models

# Create your models here.

class galeria(models.Model):
    foto = models.FileField()
    titulo =models.CharField(max_length=80, blank=True )
    descripcion = models.TextField(max_length=120, blank=True)

    class Meta:
        verbose_name_plural= "fotos"

    def __str__(self):
        return self.titulo

