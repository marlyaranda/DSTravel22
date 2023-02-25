from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ejemplo_dos.forms import UsuarioForm, CompraForm
from ejemplo_dos.models import Avatar, Post, Mensaje, Vuelo, Comprar
from django.contrib.auth.admin import User


#def index(request):
   #posts = Post.objects.order_by('-publicado_el').all()
   #return render(request, "ejemplo_dos/index.html", {"posts": posts})
class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-index')

#http://localhost:8000/ejemplo-dos/login/?next=/ejemplo-dos/listar/
class UserLogin(LoginView):
    next_page = reverse_lazy('ejemplo-dos-index')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-index')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('ejemplo-dos-listar')


class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('ejemplo-dos-listar')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("ejemplo-dos-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("ejemplo-dos-mensajes-listar")

class VueloListar(ListView):
    model = Vuelo 

class VueloDetalle(DetailView):
    model = Vuelo

class VueloCrear(LoginRequiredMixin, CreateView):
    model = Vuelo
    success_url = reverse_lazy("vuelolistar")
    fields = ['fechaPartida', 'fechaArrivo', 'destinoIda', 'destinoVuelta', 'precio', 'horaArrivo', 'horaPartida']

class VueloBorrar(LoginRequiredMixin, DeleteView):
    model = Vuelo
    success_url = reverse_lazy("vuelolistar")

class VueloActualizar(LoginRequiredMixin, UpdateView):
    model = Vuelo
    success_url = reverse_lazy("vuelolistar")
    # fields = ['fechaPartida', 'fechaArrivo', 'destinoIda', 'destinoVuelta', 'precio', 'horaArrivo', 'horaPartida']
    fields = "__all__"

def index(request):
    vuelos = Vuelo.objects.order_by('-fechaPartida').all()
    return render(request, "ejemplo_dos/index.html", {"vuelos": vuelos})

class VueloComprar(CreateView, LoginRequiredMixin):
    model = Comprar
    template_name = 'ejemplo_dos/vuelo_comprar.html'
    success_url = reverse_lazy("compralistar")
    # fields = ['NomPasajero', 'ApePasajero', 'DniPasajero', 'FechaNacPas', 'Email', 'Calle', 'Nro', 'Ciudad', 'Provincia', 'Pais', 'Telefono', 'TitTarjeta', 'NroTarjeta', 'DniTit', 'Vencimiento', 'CVV']
    fields = "__all__"

def compras(request):
    compras = Comprar.objects.order_by('-NomPasajero').all()
    return render(request, "ejemplo_dos/comprar_list.html", {"compras": compras})

class CompraListar(ListView):
    model = Comprar

class CompraDetalle(DetailView):
    model = Comprar
