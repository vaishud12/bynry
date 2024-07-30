from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_request/', views.track_request, name='track_request'),
]
