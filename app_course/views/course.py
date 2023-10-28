from rest_framework.viewsets import ModelViewSet

from app_course.models import Course
from app_course.serializers.course import CourseSerializer
from users.permissions import IsManager, IsSuperUser


class CourseViewSet(ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()

	def get_permissions(self):
		if self.request.method in ['PUT', 'PATCH']:
			permission_classes = [IsSuperUser | IsManager]
		elif self.request.method in ['POST', 'DELETE']:
			permission_classes = [IsSuperUser]
		else:
			permission_classes = []
		return [permission() for permission in permission_classes]
