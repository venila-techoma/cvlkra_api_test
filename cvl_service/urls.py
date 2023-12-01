from django.urls import path
from . import views

urlpatterns = [
    path('my_view/', views.my_view, name='my_view'),  # Map the URL 'home/' to the 'home' view
   
]
