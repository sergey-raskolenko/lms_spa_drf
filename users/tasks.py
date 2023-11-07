from django.utils import timezone

from celery import shared_task

from users.models import User


@shared_task(name="ban_inactive_users")
def ban_inactive_users():
	date_delta = timezone.now() - timezone.timedelta(days=1)
	users_to_ban = User.objects.filter(last_login__lt=date_delta, is_active=True)
	for user in users_to_ban:
		user.is_active = False
		user.save()
