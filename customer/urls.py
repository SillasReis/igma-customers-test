from django.urls import include, path
from rest_framework.routers import DefaultRouter

from customer.views import CustomerViewSet


router = DefaultRouter(trailing_slash=False)
router.register('', CustomerViewSet, basename='Customers')


urlpatterns = [
    path('', include(router.urls)),
]
