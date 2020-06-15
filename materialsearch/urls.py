from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_materials),
    path("search", views.material_search_result, name="material_search_result")
]
