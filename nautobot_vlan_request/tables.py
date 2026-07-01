from nautobot.apps.tables import BaseTable
from .models import VLANRequest


class VLANRequestTable(BaseTable):
    class Meta:
        model = VLANRequest
        fields = (
            "vlan_id",
            "vlan_name",
            "tenant",
            "subnet",
            "gateway",
        )