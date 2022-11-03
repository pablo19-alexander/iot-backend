from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django.db.models import F

from iotapi.models import User, IdentificationType
from iotapi.serializers import UserSerializer, IdentificationTypeSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.select_related('identification_type').all().annotate(
        identification_type_name = F('identification_type__name')
    )
    

class IdentificationTypeView(ModelViewSet):
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()
    
    
