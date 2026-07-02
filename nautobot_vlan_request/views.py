from nautobot.apps.views import ObjectListView, ObjectEditView, ObjectView
from .models import VLANRequest
from .tables import VLANRequestTable
from .forms import VLANRequestForm
from .filters import VLANRequestFilterSet
from .services.aci_yaml import ACIYamlGenerator



class VLANRequestListView(ObjectListView):
    queryset = VLANRequest.objects.all()
    table = VLANRequestTable
    filterset = VLANRequestFilterSet


class VLANRequestDetailView(ObjectView):
    queryset = VLANRequest.objects.all()


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