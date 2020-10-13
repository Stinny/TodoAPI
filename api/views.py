from rest_framework import viewsets
from core.models import ToDo
from .serializers import TodoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer



