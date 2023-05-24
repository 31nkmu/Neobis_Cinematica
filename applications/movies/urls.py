from rest_framework.routers import DefaultRouter

from applications.movies import views

router = DefaultRouter()
router.register('', views.MovieViewSet, basename='movies')

urlpatterns = router.urls
