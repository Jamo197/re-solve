from rest_framework import generics
from rest_framework.generics import get_object_or_404

from order_process.models import Request
from order_process.api.serializers import RequestSerializer


class RequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer