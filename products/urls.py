from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'products'

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product-detail")

urlpatterns = router.urls
