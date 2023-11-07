from celery import shared_task
from django.core.mail import send_mail

from app_course.models import Course, Subscription, Lesson
from config import settings


@shared_task
def course_update_mail_sending(obj_id, model):
	if model == "Course":
		course = Course.objects.get(id=obj_id)
	elif model == "Lesson":
		lesson = Lesson.objects.get(id=obj_id)
		course = lesson.course
	else:
		return None

	subscribed_users_qs = Subscription.objects.filter(course_id=course.id)
	email_list = [sub.user.email for sub in subscribed_users_qs]

	send_mail(
		subject="Обновление курса",
		message=f"Уведомляем Ваc, что курс на который вы подписаны ({course.title}) - обновился!\n"
				f"Рекомендуем ознакомиться с изменениями.",
		from_email=settings.EMAIL_HOST_USER,
		recipient_list=email_list,
		fail_silently=False
	)
