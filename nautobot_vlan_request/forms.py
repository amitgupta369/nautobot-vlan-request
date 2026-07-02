from django import forms
from .models import VLANRequest


class VLANRequestForm(forms.ModelForm):
    class Meta:
        model = VLANRequest
        fields = [
            "vlan_id",
            "vlan_name",
            "tenant",
            "vrf",
            "subnet",
            "gateway",
        ]

    def clean_vlan_id(self):
        vlan = self.cleaned_data["vlan_id"]

        if vlan < 1 or vlan > 4094:
            raise forms.ValidationError(
                "VLAN must be between 1 and 4094"
            )

        return vlan
