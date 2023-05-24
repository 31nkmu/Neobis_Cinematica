from rest_framework.routers import DefaultRouter

from applications.cinemas import views

router = DefaultRouter()
router.register('', views.CinemaViewSet, basename='cinemas')

urlpatterns = router.urls
