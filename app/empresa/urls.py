from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet

router = DefaultRouter()
router.register(r'empresa', EmpresaViewSet)

urlpatterns = router.urls
