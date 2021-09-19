from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name='api-owerview'),
    path('profiles/', profileList, name='profiles'),
    path('profile-create/', profileCreate, name='profile-create'),
    path('profile-update/<str:pk>', profileCreate, name='profile-update'),
    path('profile-delete/<str:pk>', profileDelete, name='profile-delete'),

]
