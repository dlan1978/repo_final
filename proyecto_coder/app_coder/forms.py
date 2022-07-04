from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Curso_formulario(forms.Form):

        nombre = forms.CharField(max_length=40)
        camada = forms.IntegerField()


class Alumno_formulario(forms.Form):
    
        nombre = forms.CharField(max_length=40)
        camada = forms.IntegerField()
        nacimiento = forms.DateField()

class Profesor_formulario(forms.Form):
        nombre = forms.CharField(max_length=40)
        legajo = forms.IntegerField()

class UserEditForm(UserCreationForm):
        
        email = forms.EmailField(label="Modificar")
        password1 = forms.CharField(label="Contrasenia" , widget=forms.PasswordInput)
        password2 = forms.CharField(label="Repetir la Contrasenia" , widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = [ 'email' , 'password1' , 'password2']
            help_text = {k:"" for k in fields}
