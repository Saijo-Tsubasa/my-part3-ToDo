from django.urls import path
from . import views

app_name='app'
urlpatterns = [
        path('', views.index, name='index'),
        path('users/<int:pk>/', views.user_detail, name='user_detail'),
    ]
