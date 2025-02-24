from django.db import models

class Denuncia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, default='pendiente')
    fecha_creacion = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo