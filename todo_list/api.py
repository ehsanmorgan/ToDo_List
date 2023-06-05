from .models import ToDo
from .serializer import ToDo_Serializer
from rest_framwork import viewsets


class ToDo_Api(viewsets.Modelviewsets):
    queryset = ToDo.objects.all()
    serializer_class=ToDo_Serializer
        