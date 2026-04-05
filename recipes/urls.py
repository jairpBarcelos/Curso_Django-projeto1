from django.urls import path
from .views import home, info, contact

urlpatterns = [
    path('', home), 
    path('info/', info), 
    path('contact/', contact),
]
  