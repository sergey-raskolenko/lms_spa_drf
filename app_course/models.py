from django.db import models

from users.models import NULLABLE


class Course(models.Model):
	title = models.CharField(max_length=150, verbose_name='название')
	preview = models.ImageField(upload_to='courses/', verbose_name='фото курса', **NULLABLE)
	description = models.TextField(**NULLABLE, verbose_name='описание')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
		ordering = ('title',)


class Lesson(models.Model):
	name = models.CharField(max_length=150,verbose_name='название')
	description = models.TextField(**NULLABLE, verbose_name='описание')
	preview = models.ImageField(upload_to='lessons/', verbose_name='фото урока', **NULLABLE)
	video_url = models.URLField(**NULLABLE, verbose_name='ссылка на видео')

	course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

	def __str__(self):
		if self.course is not None:
			return f'{self.name}({self.course})'
		else:
			return self.name

	class Meta:
		verbose_name = ''
		verbose_name_plural = ''
		ordering = ('course', 'name',)
