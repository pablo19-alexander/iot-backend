from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from django.db.models import F

from iotapi.models import User, IdentificationType, VehicleType, Vehicle, Assignment, Passenger, Driver, \
    Device, DataDevice, DeviceVehicle
from iotapi.serializers import UserSerializer, IdentificationTypeSerializer, VehicleTypeSerializer, VehicleSerializer, \
    AssignmentSerializer, PassengerSerializer, DriverSerializer, DeviceSerializer, DataDeviceSerializer, DeviceVehicleSerializer


class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.select_related('identification_type').all().annotate(
        identification_type_name=F('identification_type__name')
    )


class IdentificationTypeView(ModelViewSet):
    serializer_class = IdentificationTypeSerializer
    queryset = IdentificationType.objects.all()
    
class DeviceView(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    
class DataDeviceView(ModelViewSet):
    serializer_class = DataDeviceSerializer
    queryset = DataDevice.objects.all()

# vehicle
class VehicleTypeView(ModelViewSet):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()


# assignament ///////////////////////// pediente //////////////////////
class AssignmentView(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
# Guarda una nueva instancia antes de almacenar
    def perform_create(self, serializer):
        return serializer.save(user_modifier=self.request.user, state=True)

    def perform_update(self, serializer):
        return serializer.save(user_modifier=self.request.user, state=True)


# vehicle type ///////////////////////// pediente //////////////////////
# TODO: Pendiente tipo de vehiculo
class VehicleView(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    # queryset = Vehicle.objects.select_related('vehicle_type').all().annotate(
    #     vehicle_type_name = F('vehicle_type__name')
    # )

class DeviceVehicleView(ModelViewSet):
    serializer_class = DeviceVehicleSerializer
    queryset = DeviceVehicle.objects.all()

#Driver
class DriverView(ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


# passenger
class PassengerView(ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()
