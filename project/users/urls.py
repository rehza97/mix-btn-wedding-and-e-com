

from django.urls import path
from .views import *
app_name = 'users'
urlpatterns = [
    # path('reg/',regFirstTypoeUser,name='reg'),
    path('register_user/',register_user,name='reg2'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
]
