from rest_framework.routers import SimpleRouter
from .views import ProductView, CategoryView


router = SimpleRouter()
router.register('products', ProductView)
router.register('category', CategoryView)
urlpatterns = []

urlpatterns += router.urls
