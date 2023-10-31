from rest_framework import serializers

from app_course.models import Lesson
from app_course.validators import LessonUrlValidator


class LessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lesson
		fields = '__all__'
		validators = [LessonUrlValidator(field='video_url')]
