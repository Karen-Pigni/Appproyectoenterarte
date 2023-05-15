from django.shortcuts import render
from .data import JsonResponse
from .models import Event
from django.shortcuts import render, redirect
from .forms import EventForm

from rest_framework.generics import ListAPIView

class responseList(ListAPIView):
    queryset = response.objects.all()
    serializer_class = responseSerializer


from django.urls import path, include
from rest_framework import routers
from .views import responseViewSet

router = routers.DefaultRouter()
router.register('response', responseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.shortcuts import render
from django.http import JsonResponse
from .models import Events

def event_list(request):
    Event = Event.objects.all()
    data = {'events': list(Events.values())}
    return JsonResponse(data)

def event_detail(request, pk):
    Events = Events.objects.get(pk=pk)
    data = {'response': {
        'title': Events.title,
        'description': Events.description,
        'location': Events.location,
        'price': Events.price,
    }}
    return JsonResponse(data)
