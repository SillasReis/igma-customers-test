from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from customer.models import Customer
from customer.serializers import CustomerSerializer


ValidationError.status_code = 422


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'birth_date']
    filterset_fields = ['cpf']
    
    http_method_names = ['get', 'post', 'head']
