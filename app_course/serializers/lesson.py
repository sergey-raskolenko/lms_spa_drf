from rest_framework import serializers

from app_course.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = '__all__'
