from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()

    """
    def __str__(self):
        resultado = self.nombre+" - "+str(self.precio)+" - "+self.descripcion
        return resultado
    """