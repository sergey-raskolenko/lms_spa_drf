from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app_course.models import Course
from app_course.serializers.course import CourseSerializer
from users.permissions import IsManager, IsSuperUser


class CourseViewSet(ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()

	def perform_create(self, serializer):
		new_course = serializer.save()
		new_course.owner = self.request.user
		new_course.save()

	def get_permissions(self):
		if self.request.method in ['PUT', 'PATCH']:
			permission_classes = [IsSuperUser | IsManager]
		elif self.request.method in ['DELETE']:
			permission_classes = [IsSuperUser]
		elif self.request.method in ['POST']:
			permission_classes = [~IsManager]
		else:
			permission_classes = []
		return [permission() for permission in permission_classes]
