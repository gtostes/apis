from rest_framework import viewsets
from .serializer import SessionSerializer
from .models import Session

class SessionsViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer