from rest_framework.routers import DefaultRouter
from .views import CompraLeiteViewSet

router = DefaultRouter()

router.register(r'compras-leite', CompraLeiteViewSet)

urlpatterns = router.urls