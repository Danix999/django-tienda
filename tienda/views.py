from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente


def home(request):
    # Página de inicio sencilla
    return render(request, "tienda/home.html")


def lista_productos(request):
    # Listado de productos, ordenados por nombre
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})


def lista_pedidos(request):
    # Listado de pedidos, optimizando consultas:
    # - select_related("cliente") para la FK
    # - prefetch_related("productos") para la M2M
    pedidos = (
        Pedido.objects
        .select_related("cliente")
        .prefetch_related("productos")
        .order_by("-fecha")
    )
    return render(request, "tienda/lista_pedidos.html", {"pedidos": pedidos})


def detalle_pedido(request, pk):
    # Detalle de 1 pedido con cliente y productos pre-cargados
    pedido = get_object_or_404(
        Pedido.objects.select_related("cliente").prefetch_related("productos"),
        pk=pk
    )
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})


def detalle_cliente(request, pk):
    # Perfil del cliente + sus pedidos
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = (
        cliente.pedidos
        .prefetch_related("productos")
        .order_by("-fecha")
    )
    ctx = {"cliente": cliente, "pedidos": pedidos}
    return render(request, "tienda/detalle_cliente.html", ctx)


def detalle_producto(request, pk):
    # Ficha del producto + pedidos donde aparece
    producto = get_object_or_404(Producto, pk=pk)
    pedidos = (
        producto.pedidos
        .select_related("cliente")
        .order_by("-fecha")
    )
    ctx = {"producto": producto, "pedidos": pedidos}
    return render(request, "tienda/detalle_producto.html", ctx)
