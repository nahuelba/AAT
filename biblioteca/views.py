from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .models import ArchivosModel
from .forms import FormularioLogin



# Create your views here.


class BibliotecaView(ListView):   
    model = ArchivosModel
    template_name= 'biblioteca/inicio.html'
    

    def get(self, request,*args, **kwargs):
        queryset=ArchivosModel.objects.all()
        Context={
            'Archivos':queryset
        }
        return render(request, self.template_name, Context)


class Login(FormView):
    template_name = 'biblioteca/login.html'
    form_class= FormularioLogin
    success_url = reverse_lazy('Inicio_biblioteca')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/biblioteca/accounts/login/')


