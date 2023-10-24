from rest_framework import serializers

from app_course.models import Course


class CourseSerializer(serializers.ModelSerializer):
	lesson_counter = serializers.IntegerField(source='lesson_set.all.count')

	class Meta:
		model = Course
		fields = '__all__'
