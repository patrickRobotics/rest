from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'farmers', views.FarmersViewSet)
router.register(r'locations', views.LocationsViewSet)
urlpatterns = router.urls
