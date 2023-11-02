from rest_framework import serializers

from app_payment.models import Payment
from app_payment.services import create_session


class PaymentSerializer(serializers.ModelSerializer):
	payment_url = serializers.SerializerMethodField()

	def get_payment_url(self, instance):
		return create_session(instance)

	class Meta:
		model = Payment
		fields = '__all__'
