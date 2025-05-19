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

class Contacto(models.Model):
    OPCIONES_INTERES = [
        ('compra', 'Compra de propiedad'),
        ('renta', 'Renta de propiedad'),
        ('asesoria', 'Asesoría financiera'),
    ]

    OPCIONES_CONTACTO = [
        ('telefono', 'Teléfono'),
        ('correo', 'Correo electrónico'),
        ('whatsapp', 'WhatsApp'),
    ]

    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    me_interesa = models.CharField(max_length=20, choices=OPCIONES_INTERES)
    como_contactar = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.correo_electronico})"
    

    from django.db import models

class Documento(models.Model):
    UBICACIONES = [
        ('cdmx', 'Ciudad de México'),
        ('guadalajara', 'Guadalajara'),
        ('monterrey', 'Monterrey'),
        ('queretaro', 'Querétaro'),
        ('puebla', 'Puebla'),
        ('otro', 'Otra'),
    ]

    TIPOS_DOCUMENTO = [
        ('contrato', 'Contrato'),
        ('escritura', 'Escritura'),
    ]

    nombre = models.CharField(max_length=255)
    documento = models.FileField(upload_to='documentos/')  # Se guarda en MEDIA_ROOT/documentos/
    ubicacion = models.CharField(max_length=20, choices=UBICACIONES)
    tipo = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
