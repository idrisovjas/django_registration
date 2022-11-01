from django.urls import path
from .views import home_def
urlpatterns = [
    path('',home_def, name = 'home')
]