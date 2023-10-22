from rest_framework.viewsets import ModelViewSet

from app_course.models import Course
from app_course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()
