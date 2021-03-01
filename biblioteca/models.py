from django.db import models

# Create your models here.


class ArchivosModel(models.Model):
    Titulo = models.CharField(max_length=400)
    Archivo = models.FileField()
    Creado = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Titulo

    class Meta:
        ordering = ["Creado"]
        verbose_name= "Archivo"
        verbose_name_plural= "Archivos"
    