from django.shortcuts import render
from django.views.generic import TemplateView
from .models import galeria


# Create your views here.

class inicio(TemplateView):
    template_name='inicio.html'


class quienes_somos(TemplateView):
    template_name='nosotros/quienes-somos.html'

class comision_directiva(TemplateView):
    template_name='nosotros/comision-directiva.html'

class galeriaView(TemplateView):
    template_name='nosotros/galeria.html'
    model = 'galeria'
    context_object_name = 'galeria'

class ActividadesView(TemplateView):
    template_name='tartamudez/Actividades.html'   

class ProfesionalesView(TemplateView):
    template_name='tartamudez/profesionales.html'


class FormacionView(TemplateView):
    template_name='tartamudez/Formacion.html'
    

class GuiasFolletosView(TemplateView):
    template_name='tartamudez/guias-folletos.html'

class PreguntasFrecuentesView(TemplateView):
    template_name='tartamudez/preguntas-frecuentes.html'


class SociosSuscriptoresView(TemplateView):
    template_name='socios-suscriptores.html'