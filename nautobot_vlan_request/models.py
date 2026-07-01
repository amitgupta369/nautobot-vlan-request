from django.db import models
from nautobot.apps.models import PrimaryModel

class VLANRequest(PrimaryModel):
    vlan_id = models.PositiveIntegerField(unique=True)
    vlan_name = models.CharField(max_length=100)
    tenant = models.CharField(max_length=100)
    subnet = models.CharField(max_length=50)
    gateway = models.GenericIPAddressField()


class Meta:
    def __init__(self):
        pass

    ordering = ["vlan_id"]

def __str__(self):
    return f"{self.vlan_id} - {self.vlan_name}"

