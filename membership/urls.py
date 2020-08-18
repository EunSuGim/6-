from django.urls import path
from membership import views

app_name = "membership"

urlpatterns = [
    path('information/', views.information, name="information"),
    path('information/history/', views.history, name="history"),
    path("information/recharge/", views.recharge, name="recharge"),

]
