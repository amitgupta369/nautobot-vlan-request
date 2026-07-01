import django_tables2 as tables
from .models import VLANRequest


class VLANRequestTable(tables.Table):
    class Meta:
        model = VLANRequest
        fields = (
            "vlan_id",
            "vlan_name",
            "tenant",
            "subnet",
            "gateway",
        )