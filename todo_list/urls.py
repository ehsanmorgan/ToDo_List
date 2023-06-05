from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import todolist
from .api import ToDo_Api






router = DefaultRouter()
router.register('',ToDo_Api)

urlpatterns = [
    path('',todolist),
    path('api/',include(router.urls)),
]
