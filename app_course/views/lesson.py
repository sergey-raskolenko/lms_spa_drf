from rest_framework import generics

from app_course.models import Lesson
from app_course.serializers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
	serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
