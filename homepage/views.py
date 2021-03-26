from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsProfileRegistered

class ProfileView(generics.ListCreateAPIView):
    permission_classes = (IsProfileRegistered,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer