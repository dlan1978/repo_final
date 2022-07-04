from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} camada: {self.camada} "

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()

    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(ComentariosForm, self).__init__(*args, **kwargs)
        self.fields['creado_en'].disable = True
        self.fields['creado_por'].disable = True

