from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('delete/<str:pk>', views.delete, name='delete')
]