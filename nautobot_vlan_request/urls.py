from django.urls import path
from .views import VLANRequestListView, VLANRequestEditView

urlpatterns = [
    path(
        "",
        VLANRequestListView.as_view(),
        name="vlanrequest_list",
    ),
    path(
        "add/",
        VLANRequestEditView.as_view(),
        name="vlanrequest_add",
    ),
]