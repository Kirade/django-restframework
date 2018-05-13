from django.urls import re_path, include
from rest_framework import routers
from tutorial.quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
        re_path(r'^', include(router.urls)),
        re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
