from django.db import models

# Create your models here.

class profesionales(models.Model):
    

    class Meta:
        verbose_name_plural= "profesionales"

    def __str__(self):
        return self.titulo

