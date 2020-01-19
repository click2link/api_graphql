import uuid
from django.db import models

class Venta(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cantidad = models.IntegerField(default=1)
    producto = models.TextField(max_length=140)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    reposicion = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto

    class Meta:
        ordering = ('created',)
