import django_filters
from .models import VLANRequest


class VLANRequestFilterSet(django_filters.FilterSet):
    class Meta:
        model = VLANRequest
        fields = [
            "vlan_id",
            "tenant",
        ]