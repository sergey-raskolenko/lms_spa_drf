from django.urls import reverse
from rest_framework import status, serializers
from rest_framework.test import APITestCase

from app_course.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
	def create_user(self):
		self.user = User.objects.create(
			email='test@test.com',
			is_superuser=True
		)
		self.user.set_password('12345678')
		self.user.save()

	def setUp(self):
		self.create_user()
		self.course = Course.objects.create(title='Test')
		self.lesson = Lesson.objects.create(name='test', description='test')

	def test_lesson_create(self):
		data = {
			"name": "Test",
			"course": self.course.id
		}
		self.client.force_authenticate(self.user)
		response = self.client.post(
			reverse('course:create-lesson'),
			data=data
		)
		self.assertEqual(
			response.status_code,
			status.HTTP_201_CREATED
		)

	def test_list_lessons(self):
		self.client.force_authenticate(self.user)
		response = self.client.get(reverse('course:list-lesson'))
		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

	def test_update_lesson(self):
		self.client.force_authenticate(self.user)
		data = {
			"course": self.course.id
		}
		response = self.client.patch(
			reverse('course:update-lesson', kwargs={'pk': self.lesson.pk}),
			data=data
		)
		self.assertEqual(
			response.status_code,
			status.HTTP_200_OK
		)

	def test_delete_lesson(self):
		self.client.force_authenticate(self.user)
		lesson = Lesson.objects.create(
			name="testcase",
			description="testcase"
		)
		response = self.client.delete(
			reverse('course:delete-lesson', kwargs={'pk': lesson.pk})
		)
		self.assertEquals(
			response.status_code,
			status.HTTP_204_NO_CONTENT
		)

	def test_lesson_create_validation_error(self):
		data = {
			"name": "Test",
			"course": self.course.id,
			"video_url": "http://www.pingpong.com"
		}
		self.client.force_authenticate(self.user)
		response = self.client.post(
			reverse('course:create-lesson'),
			data=data
		)
		self.assertRaises(serializers.ValidationError)
