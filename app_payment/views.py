from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from app_payment.models import Payment
from app_payment.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
	serializer_class = PaymentSerializer
	queryset = Payment.objects.all()
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ('lesson', 'course', 'payment_type',)
	ordering_fields = ('payment_date', 'amount',)


class PaymentCreateAPIView(CreateAPIView):
	serializer_class = PaymentSerializer
