from .models import *
from rest_framework import serializers

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceApp
        fields = '__all__'