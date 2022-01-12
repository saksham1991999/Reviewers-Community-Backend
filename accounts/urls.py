from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register("users", UserViewSet, basename="user-detail")

urlpatterns = router.urls
