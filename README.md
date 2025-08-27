# 🛒 Tienda Django

Proyecto de práctica con **Django 5** para aprender el flujo completo **Modelo → Vista → Plantilla**, optimización de consultas y organización profesional de una app.

---

## 🚀 Funcionalidades
- Gestión de **Clientes**, **Productos** y **Pedidos**.
- **Admin** de Django configurado (búsqueda, filtros, autocompletado, muchos-a-muchos).
- Vistas optimizadas con `select_related` (FK) y `prefetch_related` (M2M).
- Plantillas con **herencia** (`base.html`) y **partials** (`partials/navbar.html`).
- Estilos rápidos con **PicoCSS** + CSS propio (`static/css/main.css`).

---

## 🗂 Estructura principal

core/ # Proyecto Django
settings.py
urls.py
tienda/ # App principal
admin.py
models.py
views.py
urls.py
static/
css/
main.css
templates/
tienda/
base.html
home.html
lista_productos.html
lista_pedidos.html
detalle_producto.html
detalle_pedido.html
detalle_cliente.html
partials/
navbar.html
manage.py
requirements.txt

yaml
Copiar código

---

## 🧰 Requisitos
- Python 3.11+ (recomendado 3.12)
- pip / venv
- (Opcional) Git y VS Code

---

## ⚡ Instalación y uso

# 1) Clonar
git clone https://github.com/Danix999/django-tienda.git
cd django-tienda

# 2) Entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 3) Dependencias
pip install -r requirements.txt

# 4) Migraciones
python manage.py makemigrations
python manage.py migrate

# 5) Superusuario (para /admin)
python manage.py createsuperuser

# 6) Ejecutar
python manage.py runserver
Visita:

Home: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

🧪 Datos de prueba (opcional)
bash
Copiar código
python manage.py shell
python
Copiar código
from tienda.models import Cliente, Producto, Pedido

c1 = Cliente.objects.create(nombre="Juan Pérez", email="juan@example.com")
p1 = Producto.objects.create(nombre="Teclado mecánico", precio=120000)
p2 = Producto.objects.create(nombre="Mouse gamer", precio=80000)

pedido = Pedido.objects.create(cliente=c1, estado="pagado")
pedido.productos.add(p1, p2)
exit()
🔗 Rutas principales
Ruta	Descripción
/	Inicio
/productos/	Lista de productos
/productos/<id>/	Detalle de producto
/pedidos/	Lista de pedidos
/pedidos/<id>/	Detalle de pedido
/clientes/<id>/	Detalle de cliente (y sus pedidos)
/admin/	Panel de administración

🏗 Modelos
Cliente: nombre, email

Producto: nombre, precio

Pedido: cliente (FK), fecha (auto), estado (choices), productos (M2M)

Propiedad Pedido.total suma los precios de los productos (demo simple).

Consultas optimizadas:

python
Copiar código
Pedido.objects.select_related("cliente").prefetch_related("productos")
🎨 Frontend
Base layout: templates/tienda/base.html

Navbar parcial: templates/tienda/partials/navbar.html

Estilos: static/css/main.css + CDN de PicoCSS

🧩 Stack
Django 5, SQLite (dev)

HTML/CSS, PicoCSS

Git/GitHub para control de versiones

✅ Próximos pasos (sugerencias)
Paginación y búsqueda en listas.

Modelo intermedio PedidoItem con cantidades y subtotales.

Formularios (crear/editar) para productos y pedidos.

Autenticación de usuarios.

API REST (Django REST Framework).

Deploy en Render/Railway.

👤 Autor
Daniel Olaya — GitHub @Danix999

markdown
Copiar código








Preguntar a ChatGPT
