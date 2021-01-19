from django.urls import path
from .views import inicio,quienes_somos,galeriaView, comision_directiva, ActividadesView, ProfesionalesView, FormacionView, GuiasFolletosView,SociosSuscriptoresView, PreguntasFrecuentesView, contactView,successView


urlpatterns = [
    path('', inicio.as_view(), name= 'inicio' ),
    path('quienes-somos/', quienes_somos.as_view(), name="quienes-somos"),
    path('comision-directiva/', comision_directiva.as_view(), name="comision-directiva"),
    path('galeria/', galeriaView.as_view(), name="galeria"),
    path('actividades/', ActividadesView.as_view(), name="actividades"),
    path('profesionales/', ProfesionalesView.as_view(), name="profesionales"),
    path('formacion/', FormacionView.as_view(), name="formacion"),
    path('guias-folletos/', GuiasFolletosView.as_view(), name="guias-folletos"),
    path('socios-suscriptores/', SociosSuscriptoresView, name="socios-suscriptores"),
    path('preguntas-frecuentes/', PreguntasFrecuentesView.as_view(), name="preguntas-frecuentes"),
    path('contacto/', contactView, name="contacto"),
    path('success/', successView, name="success"),

]