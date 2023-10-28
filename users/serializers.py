from rest_framework import serializers

from app_payment.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
	user_payments = PaymentSerializer(source='payment_set', many=True)

	class Meta:
		model = User
		fields = '__all__'
