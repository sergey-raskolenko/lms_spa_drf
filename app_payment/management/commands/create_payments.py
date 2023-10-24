from django.core.management import BaseCommand

from app_payment.models import Payment


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		payment = Payment.objects.create(
			user_id=1,
			course_id=1,
			amount=10000,
			payment_type='cash'
		)
		payment.save()

		payment = Payment.objects.create(
			user_id=1,
			lesson_id=1,
			amount=1100,
			payment_type='remittance'
		)
		payment.save()

		payment = Payment.objects.create(
			user_id=2,
			course_id=1,
			amount=10000,
			payment_type='remittance'
		)
		payment.save()

		payment = Payment.objects.create(
			user_id=2,
			lesson_id=3,
			amount=1300,
			payment_type='cash'
		)
		payment.save()

		payment = Payment.objects.create(
			user_id=2,
			lesson_id=4,
			amount=1400,
			payment_type='cash'
		)
		payment.save()
