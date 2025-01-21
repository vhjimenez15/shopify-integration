from .views import (
    CustomerViews, InventoryLocationViews, OrderViews, ProductViews
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', viewset=ProductViews, basename='product')
router.register(r'customer', viewset=CustomerViews, basename='customer')
router.register(r'order', viewset=OrderViews, basename='order')
router.register(
    r'inventory',
    viewset=InventoryLocationViews,
    basename='inventory'
)

urlpatterns = router.urls
