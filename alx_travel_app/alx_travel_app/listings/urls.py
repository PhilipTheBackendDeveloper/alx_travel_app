# listings/urls.py
from django.urls import path
from .views import sample_listings

urlpatterns = [
    path('', sample_listings, name='sample_listings'),
]
