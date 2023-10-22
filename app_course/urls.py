from django.urls import path
from rest_framework.routers import DefaultRouter

from app_course.apps import AppCourseConfig
from app_course.views.course import CourseViewSet
from app_course.views.lesson import *
app_name = AppCourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
	path('lesson/create/', LessonCreateAPIView.as_view(), name='create-lesson'),
	path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update-lesson'),
	path('lesson/', LessonListAPIView.as_view(), name='list-lesson'),
	path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='detail-lesson'),
	path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete-lesson'),
]

urlpatterns += router.urls
