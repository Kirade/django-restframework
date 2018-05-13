from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objecst.all().order_by('date_joined')
    serializer_class = UserSerializer


class userViewSet(viewsets.ModelViewSet):
    queryset = Group.objecst.all()
    serializer_class = GroupSerializer

