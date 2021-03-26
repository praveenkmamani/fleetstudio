from rest_framework import serializers
from .models import Profile

# A serializer class to convert the Model objects to API
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id', "profileUser", "firstName", "lastName", "emailid", "phoneNumber")
        model = Profile