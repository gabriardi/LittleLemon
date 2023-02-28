from django.shortcuts import render
from . import serializers
from .models import Menu, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
# Create your views here.


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
