from django.urls import path

from order_process.api.views import (RequestListCreateAPIView, RequestDetailAPIView)

urlpatterns = [
    path("requests/", 
         RequestListCreateAPIView.as_view(), 
         name="request-list"),
    path("requests/<int:pk>/", 
         RequestDetailAPIView.as_view(), 
         name="request-detail"),
]