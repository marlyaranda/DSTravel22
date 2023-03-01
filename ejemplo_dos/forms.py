from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from ejemplo_dos.models import Comprar

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CompraForm(forms.ModelForm):
  class Meta:
    model = Comprar
    fields = ['NomPasajero', 'ApePasajero', 'DniPasajero', 'FechaNacPas', 'Email', 'Calle', 'Nro', 'Ciudad', 'Provincia', 'Pais', 'Telefono', 'TitTarjeta', 'NroTarjeta', 'DniTit', 'Vencimiento', 'CVV']