from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()

urlpatterns = [
  
  
    path("", include(router.urls)),
]