
from rest_framework import viewsets
from .models import ToDo
from .serializer import ToDo_Serializer


class ToDo_Api(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class=ToDo_Serializer
        