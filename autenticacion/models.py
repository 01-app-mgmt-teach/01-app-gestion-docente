from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class PerfilUsuario(models.Model):
#     TIPO_USUARIO_CHOICES = [
#         ('opcion1', 'Estudiante'),
#         ('opcion2', 'Profesor'),
#     ]

#     # Relación con el modelo User
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")

#     # Datos del perfil
#     tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
#     nombres = models.CharField(max_length=100)
#     apellidop = models.CharField(max_length=100)
#     apellidom = models.CharField(max_length=100)
#     dni = models.CharField(max_length=8, unique=True)  # Campo para el DNI
#     email = models.EmailField(unique=True)

#     # Datos modificables
#     descripcion = models.TextField(blank=True, null=True)

#     # Métodos de ayuda
#     def __str__(self):
#         return f"{self.nombres} {self.apellidop} ({self.dni})"

#     def actualizar_password(self, nueva_password):
#         """
#         Actualiza la contraseña del usuario relacionado.
#         """
#         self.user.set_password(nueva_password)
#         self.user.save()

class MiPerfil(models.Model):
    # Relación de uno a uno con el modelo User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    # Campo DNI, asegurándote de que sea único y tenga un máximo de 8 caracteres
    dni = models.CharField(max_length=8, unique=True)
    
    # Campos adicionales para descripción y número de teléfono
    descripcion = models.TextField(blank=True, null=True)
    numero_telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"