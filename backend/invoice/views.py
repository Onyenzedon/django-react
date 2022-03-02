from django.shortcuts import render
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework import viewsets
# from rest_framework import permissions
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

class InvoiceView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# class InvoiceView(ListAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permissions_classes = (permissions.AllowAny,)

# class InvoiceDetailView(RetrieveAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permissions_classes = (permissions.AllowAny,)

# class InvoiceCreateView(CreateAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permissions_classes = (permissions.AllowAny,)

# class InvoiceDeleteView(DestroyAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permissions_classes = (permissions.AllowAny,)

# class InvoiceUpdateView(UpdateAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permissions_classes = (permissions.AllowAny,)