from nautobot.apps.tables import BaseTable
import django_tables2 as tables

from .models import VLANRequest


class VLANRequestTable(BaseTable):
    vlan_id = tables.LinkColumn()
    vlan_name = tables.LinkColumn()

    class Meta:
        model = VLANRequest
        fields = (
            "vlan_id",
            "vlan_name",
            "tenant",
            "subnet",
            "gateway",
        )