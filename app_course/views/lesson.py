from rest_framework import generics

from app_course.models import Lesson
from app_course.serializers.lesson import LessonSerializer
from users.permissions import IsManager, IsSuperUser


class LessonCreateAPIView(generics.CreateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [IsSuperUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [IsSuperUser | IsManager]


class LessonListAPIView(generics.ListAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
	permission_classes = [IsSuperUser]
