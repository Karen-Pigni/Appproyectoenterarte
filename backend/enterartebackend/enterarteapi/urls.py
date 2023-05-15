from .views import responseViewSet

router.register('api/response', responseViewSet)

from django.urls import path, include
from rest_framework import routers
from .views2 import responseViewSet

router = routers.DefaultRouter()
router.register('response', responseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views2 import responseList, responseDetail

urlpatterns = [
    path('response/', responseList.as_view()),
    path('response/<int:pk>/', responseDetail.as_view()),
]
