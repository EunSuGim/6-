from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('list/', views.p_list, name='list'),
    path('create/', views.p_create, name='create'),
]
