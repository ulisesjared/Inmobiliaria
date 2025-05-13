from django.db import models

class Propiedad(models.Model):
    TIPO_COMPRA_CHOICES = [
        ('compra', 'Compra'),
        ('renta', 'Renta'),
    ]

    TIPO_INMUEBLE_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('terreno', 'Terreno'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    foto_principal = models.ImageField(upload_to='propiedades/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    tipo_compra = models.CharField(max_length=10, choices=TIPO_COMPRA_CHOICES, default='compra')
    tipo_inmueble = models.CharField(max_length=15, choices=TIPO_INMUEBLE_CHOICES, default='casa')
    numero_recamaras = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo
