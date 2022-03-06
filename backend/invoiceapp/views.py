from django.shortcuts import render
from .models import InvoiceApp
from .serializers import InvoiceSerializer
from rest_framework import viewsets


class InvoiceAppView(viewsets.ModelViewSet):
    queryset = InvoiceApp.objects.all()
    serializer_class = InvoiceSerializer