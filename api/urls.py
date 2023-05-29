from django.urls import include, path
from rest_framework import routers

from api.views import BasketModelViewSe, ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()    # Добавление CRUD запросов
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSe)
urlpatterns = [
    path('', include(router.urls)),
]
