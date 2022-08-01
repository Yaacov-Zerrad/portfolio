from contact.views import ContactViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact', ContactViewSet)
