import json
import urllib.request
import smtplib

from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.conf import settings
from django.contrib import messages


from .forms import SociosSuscriptoresForm, ContactoForm
from .models import SociosSuscriptoresModel

from email.mime.text import MIMEText
from email.header import Header



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
        
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY, 'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        if result['success']:
            form.save()
            server = smtplib.SMTP("smtp.aat.org.ar", 587)#port
            server.ehlo()
            server.starttls()
            server.login()
            body = "Nombre: " + request.POST["nombre"] + "\n" + "apellido: " + request.POST["apellido"] + "\n" + "mail: " + request.POST["mail"] + "\n" + "telefono: " + request.POST["telefono"] + "\n" + "pais: " + request.POST["pais"] + "\n" + "provincia: " + request.POST["provincia"] + "\n" + "lugar de residencia: " + request.POST["lugar_de_residencia"] + "\n" + "nacimiento: " + request.POST["nacimiento"] + "\n" + "tipo de persona: " + request.POST["tipo_de_persona"] + "\n" + "mensaje: " + request.POST["mensaje"]
            msg = MIMEText(body,'plain','utf-8')
            subject = "Felicidades! Nuevo " + request.POST["Socio_suscriptor"]
            msg["Subject"] = Header(subject, 'utf-8')
            From = 'mensajeria@aat.org.ar'
            to = 'info@aat.org.ar'
            msg["From"] = Header(From, 'utf-8')
            msg["To"] = Header(to, 'utf-8')
            txt = msg.as_string()
            
            server.sendmail(From, to, txt)
            return redirect('success')
        else:
            messages.error(request, 'reCAPTCHA invalido, completelo de nuevo')
            #return redirect('socios-suscriptores')
        
       
            
        
        
            
    
        

    context = {
        'form':form
    }

    return render(request, "socios-suscriptores.html", context)

def contactView(request):
    form = ContactoForm(request.POST or None)
    
   

    if form.is_valid():
        
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY, 'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        if result['success']:
            form.save()
            server = smtplib.SMTP("smtp.aat.org.ar", 587)#port
            server.ehlo()
            server.starttls()
            server.login()
            body = "Recibimos una consulta de parte de " + request.POST['nombre'] + " su mail de contacto es " + request.POST['mail'] + "\n Y su mensaje es: " + request.POST['mensaje'] 
            msg = MIMEText(body,'plain','utf-8')
            subject = "Nueva consulta de parte de "+  request.POST['nombre']
            msg["Subject"] = Header(subject, 'utf-8')
            From = 'mensajeria@aat.org.ar'
            to = 'info@aat.org.ar'
            msg["From"] = Header(From, 'utf-8')
            msg["To"] = Header(to, 'utf-8')
            txt = msg.as_string()
            server.sendmail(From, to, txt)
            return redirect('success')
        else:
            messages.error(request, 'reCAPTCHA invalido, completelo de nuevo')
            #return redirect('contacto')
        
        #form.save()
        
        
        
        
    context = {
        'form':form
    }
    return render(request, "contacto.html", context)

def successView(request):
    return render(request, "success.html")


def donar(request):
    
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY, 'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        
        if result['success']:
            form.save()
            server = smtplib.SMTP("smtp.aat.org.ar", 587)#port
            server.ehlo()
            server.starttls()
            server.login()
            body = "Recibimos un mensaje de donacion de parte de " + request.POST['nombre'] + " su mail de contacto es " + request.POST['mail'] + "\n Y su mensaje es: " + request.POST['mensaje'] 
            recipient_list=["nahuelbarreiro@gmail.com"]
            msg = MIMEText(body,'plain','utf-8')
            subject = "Nuevo mensaje de donacion de parte de "+  request.POST['nombre']
            msg["Subject"] = Header(subject, 'utf-8')
            From = 'mensajeria@aat.org.ar'
            to = 'info@aat.org.ar'
            msg["From"] = Header(From, 'utf-8')
            msg["To"] = Header(to, 'utf-8')
            txt = msg.as_string()
            
            server.sendmail(From, to, txt)
            return redirect('success')
        else:
            messages.error(request, 'reCAPTCHA invalido, completelo de nuevo')
            #return redirect('donar')
        
        
        
        
    return render(request, "donar.html", {'form': form})


