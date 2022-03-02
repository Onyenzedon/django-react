from django.urls import path,include
from rest_framework import routers
from .views import InvoiceView
    # InvoiceDetailView,
    # InvoiceCreateView,
    # InvoiceDeleteView,
    # InvoiceUpdateView,
    

router = routers.DefaultRouter()
router.register("api", InvoiceView, basename="invoiceview")
# router.register("detail/", InvoiceDetailView, basename="invoicedetailview")
# router.register("create/", InvoiceCreateView, basename="invoicecreateview")
# router.register("delete/", InvoiceDeleteView, basename="invoicedeleteview")
# router.register("update/", InvoiceUpdateView, basename="invoiceupdateview")

urlpatterns = [
    path("", include(router.urls)),
]