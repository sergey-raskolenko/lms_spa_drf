from rest_framework import serializers

from app_course.models import Course
from app_course.serializers.lesson import LessonSerializer
from app_course.validators import CourseUrlValidator


class CourseSerializer(serializers.ModelSerializer):
	lesson_counter = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
	lessons = LessonSerializer(source='lesson_set.all', many=True, read_only=True)

	class Meta:
		model = Course
		fields = '__all__'
		validators = [CourseUrlValidator(field='description')]
