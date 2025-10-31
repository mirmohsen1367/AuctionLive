from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from api.views.bid_view import CreateBidViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()
    
router.register(prefix=r'create_bid', viewset=CreateBidViewSet, basename="bid")

urlpatterns = [
    path('', include(router.urls))
]
