from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SociosSuscriptoresForm, ContactoForm
from .models import SociosSuscriptoresModel
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


# Create your views here.

class inicio(TemplateView):
    template_name='inicio.html'


class quienes_somos(TemplateView):
    template_name='nosotros/quienes-somos.html'

class comision_directiva(TemplateView):
    template_name='nosotros/comision-directiva.html'

class galeriaView(TemplateView):
    template_name='nosotros/galeria.html'


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


def SociosSuscriptoresView(request):
    form = SociosSuscriptoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        subject="Felicidades! Nuevo " + request.POST["Socio_suscriptor"]
        message="Nombre: " + request.POST["nombre"] + "\n" + "apellido: " + request.POST["apellido"] + "\n" + "mail: " + request.POST["mail"] + "\n" + "telefono: " + request.POST["telefono"] + "\n" + "pais: " + request.POST["pais"] + "\n" + "provincia: " + request.POST["provincia"] + "\n" + "lugar de residencia: " + request.POST["lugar_de_residencia"] + "\n" + "nacimiento: " + request.POST["nacimiento"] + "\n" + "tipo de persona: " + request.POST["tipo_de_persona"] + "\n" + "mensaje: " + request.POST["mensaje"]
        

        email_from=settings.EMAIL_HOST_USER
        recipient_list=["nahuelbarreiro@gmail.com"]

        # image = request.FILES['Comprobante_de_pago']
        # filename = 'C:/Users/Arvan Bishwas/PycharmProjects/SendingEmails' + image.url

        # attachment  =open(filename,'rb')


        email = EmailMessage(subject, message, email_from, recipient_list)
        
        email.send()

    
        form =SociosSuscriptoresForm()

    context = {
        'form':form
    }

    return render(request, "socios-suscriptores.html", context)

def contactView(request):
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Nueva consulta de parte de "+  request.POST['nombre']
            email_from= settings.EMAIL_HOST_USER
            content = "Recibimos una consulta de parte de " + request.POST['nombre'] + " su mail de contacto es" + request.POST['mail'] + "\n Y su mensaje es: " + request.POST['mensaje'] 
            recipient_list=["nahuelbarreiro@gmail.com"]
            try:
                send_mail(subject, content, email_from, recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contacto.html", {'form': form})

def successView(request):
    return render(request, "success.html")


