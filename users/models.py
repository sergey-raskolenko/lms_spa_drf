from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
	username = None

	email = models.EmailField(unique=True, verbose_name='почта')

	phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
	city = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)
	avatar = models.ImageField(upload_to='users/', verbose_name='фото', **NULLABLE)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		db_table = 'users'
		ordering = ['id']

	def __str__(self):
		return self.email
