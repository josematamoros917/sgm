from django.db import models

# Create your models here.

class Taller(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del taller")
    descripcion = models.TextField(verbose_name="Descripción breve", help_text="Una breve descripción del taller")
    direccion = models.CharField(max_length=255, verbose_name="Dirección física", blank=True, null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono de contacto", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo de contacto", blank=True, null=True)
    horario = models.CharField(max_length=100, verbose_name="Horario de atención", blank=True, null=True)
    enlace_facebook = models.URLField(verbose_name="Enlace a Facebook", blank=True, null=True)
    enlace_instagram = models.URLField(verbose_name="Enlace a Instagram", blank=True, null=True)
    enlace_whatsapp = models.URLField(verbose_name="Enlace a WhatsApp", blank=True, null=True)
    logo = models.ImageField(upload_to="logos/", verbose_name="Logo del taller", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre