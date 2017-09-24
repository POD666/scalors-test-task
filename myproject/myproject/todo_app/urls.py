from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TODOViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'todo', TODOViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
