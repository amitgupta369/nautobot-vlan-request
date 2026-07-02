from django.db import models
from django.urls import reverse
from nautobot.apps.models import PrimaryModel

class VLANRequest(PrimaryModel):
    STATUS_CHOICES = (
        ("Requested", "Requested"),
        ("Generated", "Generated"),
        ("Committed", "Committed"),
        ("Deployed", "Deployed"),
        ("Failed", "Failed"),
    )
    vlan_id = models.PositiveIntegerField(unique=True)
    vlan_name = models.CharField(max_length=100)
    tenant = models.CharField(max_length=100)
    subnet = models.CharField(max_length=50)
    gateway = models.GenericIPAddressField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Requested"
    )

    rendered_yaml = models.TextField(blank=True)


    class Meta:
        ordering = ["vlan_id"]

    def __str__(self):
        return f"{self.vlan_id} - {self.vlan_name}"

    def get_absolute_url(self):
        return reverse(
            "plugins:nautobot_vlan_request:vlanrequest",
            args=[self.pk],
        )

