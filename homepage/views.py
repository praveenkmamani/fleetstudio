from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsProfileRegistered

# A class to list the serializer data in an API view. Mentioned ListCreateAPIView which is enough to do the CRUD operation.

class ProfileView(generics.ListCreateAPIView):
    permission_classes = (IsProfileRegistered,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer