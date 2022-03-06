from django.urls import path,include
from rest_framework import routers
from .views import InvoiceAppView

router = routers.DefaultRouter()
router.register("api", InvoiceAppView, basename="invoiceAppview")
# router.register("login", LoginPage, basename="LoginPage")

urlpatterns = [
    path("", include(router.urls)),
]