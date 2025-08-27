from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # URLs de la app tienda (raíz del sitio)
    path("", include("tienda.urls")),
]
