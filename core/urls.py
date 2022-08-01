from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from skill.urls import router as skill_router
from contact.urls import router as contact_router
from courses.urls import router as courses_router


router = routers.DefaultRouter()
router.registry.extend(skill_router.registry)
router.registry.extend(contact_router.registry)
router.registry.extend(courses_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
