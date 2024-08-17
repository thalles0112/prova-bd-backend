from django.urls import re_path
from django.conf.urls import include
from api import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('vendas', views.Venda)


urlpatterns = [
    re_path(r'^', include(router.urls))
]