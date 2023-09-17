from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main-page'),
    path('beast-sellers/', topSellers, name='top_1-sellers'),
    path('advertisement-post/', advertPost, name='advertis_1-post' ),
    path('register/', regis, name='register_1'),
    path('profile/', prof, name='profile_1'),
    path('login/', log, name='login_1')
]