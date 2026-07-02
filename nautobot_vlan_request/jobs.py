import os

from nautobot.apps.jobs import Job, ObjectVar, register_jobs

from .models import VLANRequest
from .services.aci_yaml import ACIYamlGenerator


class GenerateACIYaml(Job):
    class Meta:
        name = "Generate ACI YAML"
        enabled = True
        description = "Generate NetAsCode YAML from VLAN Request"

    vlan_request = ObjectVar(
        model=VLANRequest,
        description="Select VLAN Request"
    )

    def run(self, vlan_request):
        generator = ACIYamlGenerator(vlan_request)

        output_dir = "/opt/netascode/data"
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(
            output_dir,
            f"vlan-{vlan_request.vlan_id}.yaml"
        )

        rendered_yaml = generator.save_to_file(output_file)

        vlan_request.rendered_yaml = rendered_yaml
        vlan_request.status = "Generated"
        vlan_request.save()

        self.log_success(
            message=f"Generated YAML at {output_file}"
        )

register_jobs(GenerateACIYaml)