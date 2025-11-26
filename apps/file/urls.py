from rest_framework.routers import DefaultRouter

from apps.file.views import FileViewSet

router = DefaultRouter()
router.register(r'', FileViewSet, basename='file')
urlpatterns = router.urls
