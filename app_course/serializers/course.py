from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from app_course.models import Course, Subscription
from app_course.serializers.lesson import LessonSerializer
from app_course.validators import CourseUrlValidator


class CourseSerializer(serializers.ModelSerializer):
	lesson_counter = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
	lessons = LessonSerializer(source='lesson_set.all', many=True, read_only=True)
	subscription = serializers.SerializerMethodField()

	class Meta:
		model = Course
		fields = '__all__'
		validators = [CourseUrlValidator(field='description')]

	def get_subscription(self, value):
		try:
			Subscription.objects.get(
				course=value,
				user=self.context.get('request').user.pk,
				is_active=True
			)
		except ObjectDoesNotExist:
			return 'Подписка отсутствует'
		else:
			return 'Подписка активна'


class SubscriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscription
		fields = '__all__'
