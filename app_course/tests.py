from django.urls import reverse
from rest_framework import status, serializers
from rest_framework.test import APITestCase

from app_course.models import Course, Lesson, Subscription
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
		self.client.force_authenticate(self.user)
		self.course = Course.objects.create(title='Test')
		self.lesson = Lesson.objects.create(name='test', description='test')

	def test_lesson_create(self):
		data = {
			"name": "Test",
			"course": self.course.id
		}
		response = self.client.post(
			reverse('course:create-lesson'),
			data=data
		)
		self.assertEqual(
			response.status_code,
			status.HTTP_201_CREATED
		)

	def test_list_lessons(self):
		response = self.client.get(reverse('course:list-lesson'))
		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

	def test_update_lesson(self):
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
		self.client.post(
			reverse('course:create-lesson'),
			data=data
		)
		self.assertRaises(serializers.ValidationError)


class SubscriptionTestCase(APITestCase):
	def create_user(self):
		self.user = User.objects.create(
			email='test@test.com',
			is_superuser=True
		)
		self.user.set_password('12345678')
		self.user.save()

	def setUp(self):
		self.create_user()
		self.client.force_authenticate(self.user)
		self.course = Course.objects.create(title='Test')
		self.sub = Subscription.objects.create(user=self.user, course=self.course)

	def test_create_sub(self):
		data = {
			'user': self.user.pk,
			'course': self.course.pk,
			'is_active': False
		}
		response = self.client.post(
			reverse('course:create-subscription'),
			data=data
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_delete_sub(self):
		new_sub = Subscription.objects.create(user=self.user, course=self.course)
		response = self.client.delete(
			reverse('course:delete-subscription', kwargs={'pk': new_sub.pk})
		)
		self.assertEquals(
			response.status_code,
			status.HTTP_204_NO_CONTENT
		)