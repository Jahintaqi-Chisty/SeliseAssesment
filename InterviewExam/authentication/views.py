from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (IsAdminUser,)
    permission_classes = (AllowAny,) # Permission added for anyone so, anyone can register
    serializer_class = RegisterSerializer
