from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app_course.models import Course, Subscription
from app_course.paginators import CoursePaginator
from app_course.serializers.course import CourseSerializer, SubscriptionSerializer
from app_course.tasks import course_update_mail_sending
from users.permissions import IsManager, IsSuperUser, IsOwner


class CourseViewSet(ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()
	pagination_class = CoursePaginator

	def perform_create(self, serializer):
		new_course = serializer.save()
		new_course.owner = self.request.user
		new_course.save()

	def get_queryset(self):
		user = self.request.user
		if user.groups.filter(name='Manager') or user.is_superuser:
			return Course.objects.all()
		return Course.objects.filter(owner=user)

	def get_permissions(self):
		if self.request.method in ['PUT', 'PATCH']:
			permission_classes = [IsOwner | IsSuperUser | IsManager]
		elif self.request.method in ['DELETE']:
			permission_classes = [IsSuperUser]
		elif self.request.method in ['POST']:
			permission_classes = [~IsManager]
		else:
			permission_classes = []
		return [permission() for permission in permission_classes]

	def update(self, request, *args, **kwargs):
		obj = self.get_object()
		course_update_mail_sending.delay(obj.id, model="Course")
		return super().update(request, *args, **kwargs)

class SubscriptionCreateAPIView(generics.CreateAPIView):
	serializer_class = SubscriptionSerializer


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
	serializer_class = SubscriptionSerializer
	queryset = Subscription.objects.all()
