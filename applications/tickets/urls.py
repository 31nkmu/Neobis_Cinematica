from rest_framework.routers import DefaultRouter

from applications.tickets import views

router = DefaultRouter()
router.register('', views.TicketViewSet, basename='cinemas')

urlpatterns = router.urls
