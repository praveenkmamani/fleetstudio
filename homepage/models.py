from django.db import models
from django.contrib.auth.models import User

# The below class is the model of the Profile table
class Profile(models.Model):
    profileUser = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.phoneNumber
