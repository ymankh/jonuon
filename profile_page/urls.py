from django.urls import path
from .views import login_page, logout_page, signup

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_page, name='logout'),
]
