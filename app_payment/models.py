from django.db import models
from app_course.models import Course, Lesson
from config import settings
from users.models import NULLABLE


class Payment(models.Model):
	PAYMENT_CASH = 'cash'
	PAYMENT_TRANSFER = 'remittance'
	PAYMENT_TYPES = [
		(PAYMENT_CASH, 'наличные'),
		(PAYMENT_TRANSFER, 'перевод')
	]
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
	payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='оплаченный курс', **NULLABLE)
	lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='оплаченный урок', **NULLABLE)
	amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
	payment_type = models.CharField(max_length=25, choices=PAYMENT_TYPES, verbose_name='способ оплаты')

	def __str__(self):
		return f'{self.lesson if self.lesson else self.course}: {self.amount} ({self.amount})'

	class Meta:
		verbose_name = 'оплата'
		verbose_name_plural = 'оплаты'
		ordering = ('payment_date',)
