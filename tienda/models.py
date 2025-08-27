from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        # Ej: "Teclado ($120000.00)"
        return f"{self.nombre} (${self.precio})"


class Pedido(models.Model):
    ESTADOS = [
        ("nuevo", "Nuevo"),
        ("pagado", "Pagado"),
        ("enviado", "Enviado"),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="nuevo")

    # Relación M2M directa como se ve en clase (prefetch_related("productos"))
    productos = models.ManyToManyField(Producto, related_name="pedidos")

    class Meta:
        ordering = ["-fecha"]

    def __str__(self) -> str:
        return f"Pedido #{self.id} - {self.cliente}"

    @property
    def total(self):
        # Suma simple de precios (sin cantidades por producto)
        return sum(p.precio for p in self.productos.all())
