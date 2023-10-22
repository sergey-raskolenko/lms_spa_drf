from rest_framework.routers import DefaultRouter

from app_course.apps import AppCourseConfig
from app_course.views.course import CourseViewSet

app_name = AppCourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

]

urlpatterns += router.urls
