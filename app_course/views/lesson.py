from rest_framework import generics

from app_course.models import Lesson
from app_course.paginators import LessonPaginator
from app_course.serializers.lesson import LessonSerializer
from users.permissions import IsManager, IsSuperUser, IsOwner


class LessonCreateAPIView(generics.CreateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [~IsManager]

	def perform_create(self, serializer):
		new_lesson = serializer.save()
		new_lesson.owner = self.request.user
		new_lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [IsOwner | IsSuperUser | IsManager]


class LessonListAPIView(generics.ListAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	pagination_class = LessonPaginator

	def get_queryset(self):
		user = self.request.user
		if user.groups.filter(name='Manager') or user.is_superuser:
			return Lesson.objects.all()
		return Lesson.objects.filter(owner=user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [IsSuperUser]
