from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django.db.models import F

from iotapi.models import User, IdentificationType, VehicleType, Vehicle, Assignment, Passenger
from iotapi.serializers import UserSerializer, IdentificationTypeSerializer, VehicleTypeSerializer, VehicleSerializer, AssignmentSerializer, PassengerSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.select_related('identification_type').all().annotate(
        identification_type_name = F('identification_type__name')
    )
    

class IdentificationTypeView(ModelViewSet):
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()
    
#vehicle
class VehicleTypeView(ModelViewSet):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()

#assignament ///////////////////////// pediente //////////////////////
class AssignmentView(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

#vehicle type ///////////////////////// pediente //////////////////////
class VehicleView(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    # queryset = Vehicle.objects.select_related('vehicle_type').all().annotate(
    #     vehicle_type_name = F('vehicle_type__name')
    # )

#passenger
class PassengerView(ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()
