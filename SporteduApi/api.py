from rest_framework import routers
from api.views import ProfileView

router =routers.DefaultRouter()
router.register(r'Profiles', ProfileView, basename='profiles')