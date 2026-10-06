from django.db import models
from django.core.validators import MinValueValidator

class Pedido(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.CharField(max_length=120, verbose_name="Nombre del Cliente")
    direccion = models.CharField(max_length=200, verbose_name="Dirección de Entrega")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono de Contacto")
    descripcion_productos = models.TextField(verbose_name="Detalle de Productos")
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(1.00)],
        verbose_name="Total a Pagar ($)"
    )
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"
# Create your models here.
