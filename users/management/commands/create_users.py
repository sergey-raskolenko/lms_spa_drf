from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		user_1 = User.objects.create(
			email='test@testov.com',
			first_name='Test',
			last_name='Testov',
			phone='89998887766',
			city='Moscow'
		)

		user_1.set_password('test1test1')
		user_1.save()

		user_2 = User.objects.create(
			email='ivan@ivanov.com',
			first_name='Ivan',
			last_name='Ivanov',
			phone='89998887765',
			city='St.Petersburg'
		)

		user_2.set_password('ivan1ivan1')
		user_2.save()
