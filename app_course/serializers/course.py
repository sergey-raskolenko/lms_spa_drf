from rest_framework import serializers

from app_course.models import Course
from app_course.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
	lesson_counter = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
	lessons = LessonSerializer(source='lesson_set.all', many=True)

	class Meta:
		model = Course
		fields = '__all__'
