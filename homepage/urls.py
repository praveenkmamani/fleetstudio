from django.urls import path, include
from .views import ProfileView

# Adding the ProfileView for the url to view via api
urlpatterns = [
    path('', ProfileView.as_view()),
]