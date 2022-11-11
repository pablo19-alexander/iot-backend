from rest_framework import routers

from iotapi.views import UserView, IdentificationTypeView, VehicleTypeView, VehicleView, AssignmentView, PassengerView

router = routers.DefaultRouter()

router.register('users', UserView)
router.register('identification-type', IdentificationTypeView)
router.register('vehicle-Type', VehicleTypeView)
router.register('vehicle', VehicleView)
router.register('assignment', AssignmentView)
router.register('passenger', PassengerView)




urlpatterns = router.urls
