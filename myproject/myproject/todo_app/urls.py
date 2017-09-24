from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
