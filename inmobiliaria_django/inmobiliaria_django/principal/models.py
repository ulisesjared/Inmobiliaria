from django.db import models

class Propiedad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto_principal = models.ImageField(upload_to='propiedades/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
