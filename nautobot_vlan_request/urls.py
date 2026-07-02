from django.urls import path
from .views import VLANRequestListView, VLANRequestEditView, VLANRequestDetailView, generate_yaml_view

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
    path(
        "<uuid:pk>/",
        VLANRequestDetailView.as_view(),
        name="vlanrequest",
    ),
    path(
        "<uuid:pk>/generate-yaml/",
        generate_yaml_view,
        name="vlanrequest_generate_yaml",
    ),
]