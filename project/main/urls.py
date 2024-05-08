

from django.urls import path
from .views import *
app_name = 'main'
urlpatterns = [
    path('', index, name='index'),  # 主页
    path('shop/', shop, name='shop'),  # 主页
    path('product/<int:id>', product, name='product'),  # 主页
    path('about/', about, name='about'),  # 主页
    path('contact/', contact, name='contact'),  # 主页
    path('wishlist/', wishlist, name='wishlist'),  # 主页
    path('cart/', cart, name='cart'),  # 主页
    path('profile/', profile, name='profile'),  # 主页
    path('party_rooms/', party_rooms, name='party_rooms'),  # 主页
    path('room_details/<int:id>', room_details, name='room_details'),  # 主页
    path('makeup/', makeup, name='makeup'),  # 主页
    path('cake/', cake, name='cake'),  # 主页
    path('cameraPage/', cameraPage, name='cameraPage'),  # 主页


]
