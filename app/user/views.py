"""
Views for the user API
"""

from rest_framework import generics

from user.serialiizers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer