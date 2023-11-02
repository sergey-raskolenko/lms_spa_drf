from django.urls import path

from app_payment.apps import AppPaymentConfig
from app_payment.views import PaymentListAPIView, PaymentCreateAPIView

app_name = AppPaymentConfig.name

urlpatterns = [
	path('payment/', PaymentListAPIView.as_view(), name='list-payment'),
	path('payment/create/', PaymentCreateAPIView.as_view(), name='create-payment'),
]
