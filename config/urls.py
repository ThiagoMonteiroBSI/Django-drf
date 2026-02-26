from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from biblioteca.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
]
