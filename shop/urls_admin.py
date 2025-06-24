# shop/urls_admin.py

from rest_framework.routers import DefaultRouter
from .views_admin import AdminProductViewSet

router = DefaultRouter()
router.register('admin/products', AdminProductViewSet, basename='admin-products')

urlpatterns = router.urls
