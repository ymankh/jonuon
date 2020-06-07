from django.urls import path
from .views import teachers


urlpatterns = [
    path("", teachers)
]