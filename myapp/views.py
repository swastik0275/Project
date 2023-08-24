from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer