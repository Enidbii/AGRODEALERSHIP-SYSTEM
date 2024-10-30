
from django.urls import path, include

urlpatterns = [
    path("store/", include("agrostoremanager.backend.endpoints"))
]