from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

class UsersWViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer