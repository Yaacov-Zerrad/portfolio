from courses.models import CoursesModel
from courses.views import CoursViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', CoursViewSet)