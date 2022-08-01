from rest_framework import routers
from skill.views import SkillViewSet

router = routers.DefaultRouter()
router.register('skill', SkillViewSet)