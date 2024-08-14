from .views import getIndex
from django.urls import path

urlpatterns = [
    path('', getIndex),
]