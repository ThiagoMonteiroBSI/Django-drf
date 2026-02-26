from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Categoria, Editora
from biblioteca.serializers import CategoriaSerializer, EditoraSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer