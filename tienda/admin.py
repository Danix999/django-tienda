from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, Producto, Pedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email")
    search_fields = ("nombre", "email")
    ordering = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio")
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "fecha", "estado", "total")
    list_filter = ("estado", "fecha")
    search_fields = ("cliente__nombre",)
    autocomplete_fields = ("cliente",)
    filter_horizontal = ("productos",)
    ordering = ("-fecha",)
