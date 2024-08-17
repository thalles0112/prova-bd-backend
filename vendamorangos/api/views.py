from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Venda
from .serializers import VendaSerializer
# Create your views here.


class Venda(ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer