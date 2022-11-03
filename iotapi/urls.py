from rest_framework import routers

from iotapi.views import UserView, IdentificationTypeView

router = routers.DefaultRouter()

router.register('users', UserView)
router.register('identification-type', IdentificationTypeView)


urlpatterns = router.urls
