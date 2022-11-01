from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from iotapi.models import User
from iotapi.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
