from django.urls import path

from app_payment.apps import AppPaymentConfig
from app_payment.views import PaymentListAPIView

app_name = AppPaymentConfig.name

urlpatterns = [
	path('payment/', PaymentListAPIView.as_view(), name='list-payment'),
]
