from rest_framework.routers import DefaultRouter

from applications.rooms import views

router = DefaultRouter()
router.register('seat', views.SeatViewSet, basename='seats')
router.register('', views.RoomViewSet, basename='rooms')

urlpatterns = router.urls
