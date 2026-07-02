from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from nautobot.apps.views import ObjectListView, ObjectEditView, ObjectView
from .models import VLANRequest
from .tables import VLANRequestTable
from .forms import VLANRequestForm
from .filters import VLANRequestFilterSet
from .services.aci_yaml import ACIYamlGenerator


from nautobot.apps.ui import (
    ObjectDetailContent,
    Button,
)


class VLANRequestListView(ObjectListView):
    queryset = VLANRequest.objects.all()
    table = VLANRequestTable
    filterset = VLANRequestFilterSet


class VLANRequestDetailView(ObjectView):
    queryset = VLANRequest.objects.all()
    def get_object_detail_content(self):
        return ObjectDetailContent(
            extra_buttons=[
                Button(
                    url=f"{self.object.get_absolute_url()}generate-yaml/",
                    label="Generate YAML",
                    icon="mdi mdi-file-code",
                )
            ]
        )

    def get_extra_context(self, request, instance):
        context = super().get_extra_context(request, instance)

        context["generate_yaml_url"] = reverse(
            "plugins:nautobot_vlan_request:vlanrequest_generate_yaml",
            kwargs={"pk": instance.pk},
        )

        return context


class VLANRequestEditView(ObjectEditView):
    queryset = VLANRequest.objects.all()
    model_form = VLANRequestForm


def generate_yaml_view(request, pk):
    vlan_request = get_object_or_404(VLANRequest, pk=pk)

    generator = ACIYamlGenerator(vlan_request)

    output_dir = "/tmp/netascode"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(
        output_dir,
        f"vlan-{vlan_request.vlan_id}.yaml"
    )

    rendered_yaml = generator.save_to_file(output_file)

    vlan_request.rendered_yaml = rendered_yaml
    vlan_request.status = "Generated"
    vlan_request.save()

    return redirect(vlan_request.get_absolute_url())