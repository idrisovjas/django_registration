from django.urls import path
from .views import log_in,register,log_out





urlpatterns = [
        path('login/',log_in,name = 'login'),
        path('logout/',log_out,name = 'logout'),
        path('register/',register,name = 'register'),
 ]