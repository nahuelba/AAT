from django.contrib import admin
from .models import ArchivosModel
# Register your models here.

class ArchivosAdmin(admin.ModelAdmin):
    readonly_fields=['Creado',]
    
admin.site.register(ArchivosModel, ArchivosAdmin)