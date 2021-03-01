from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import BibliotecaView, Login, Logout


urlpatterns = [
    path('', login_required(BibliotecaView.as_view()), name="Inicio_biblioteca"),
    path('accounts/login/', Login.as_view(), name="login"),
    path('logout/', login_required(Logout), name="logout"),

]