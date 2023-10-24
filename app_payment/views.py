from rest_framework.generics import ListAPIView

from app_payment.models import Payment
from app_payment.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
	serializer_class = PaymentSerializer
	queryset = Payment.objects.all()

