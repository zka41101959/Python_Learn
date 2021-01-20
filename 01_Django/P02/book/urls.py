from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('rece/', views.ReceiveView.as_view()),
]
