from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .form import PedidoCrearForm, PedidoEditarForm

# Consultar (R - Read)
def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})

# Crear (C - Create)
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoCrearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoCrearForm()
    return render(request, 'pedidos/crear.html', {'form': form})

# Modificar (U - Update)
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoEditarForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoEditarForm(instance=pedido)
    return render(request, 'pedidos/editar.html', {'form': form, 'pedido': pedido})

# Eliminar (D - Delete)
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedidos')
    return render(request, 'pedidos/eliminar.html', {'pedido': pedido})