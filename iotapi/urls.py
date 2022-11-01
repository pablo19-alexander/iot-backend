from rest_framework import routers

from iotapi.views import UserView

router = routers.SimpleRouter()

router.register('users', UserView)


urlpatterns = router.urls
