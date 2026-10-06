from django import forms
from .models import Pedido

# Formulario para Crear (no pide estado porque inicia por defecto en 'Pendiente')
class PedidoCrearForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion', 'telefono', 'descripcion_productos', 'total']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle, número, depto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'descripcion_productos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ej: 1 Pizza Familiar, 1 Bebida'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12000'}),
        }

# Formulario para Editar (permite cambiar y gestionar el estado del delivery)
class PedidoEditarForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion', 'telefono', 'descripcion_productos', 'total', 'estado']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_productos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }