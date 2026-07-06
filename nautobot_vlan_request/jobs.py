import os

from nautobot.apps.jobs import Job, IntegerVar, register_jobs

from .models import VLANRequest
from .services.aci_yaml import ACIYamlGenerator


class GenerateACIYaml(Job):
    class Meta:
        name = "Generate ACI YAML"
        description = "Generate NetAsCode YAML from VLAN Request"
        enabled = True

    vlan_id = IntegerVar(
        description="Enter VLAN ID",
        required=True,
    )

    output_directory = "/home/nautobot/data"

    def run(self, vlan_id):
        """Generate NetAsCode YAML from a VLAN Request."""

        self.logger.info("Searching VLAN Request...")

        try:
            vlan_request = VLANRequest.objects.get(vlan_id=vlan_id)

        except VLANRequest.DoesNotExist:
            self.log_failure(
                message=f"VLAN {vlan_id} not found."
            )
            return

        self.logger.info(
            "Found VLAN %s (%s)",
            vlan_request.vlan_id,
            vlan_request.vlan_name,
        )

        generator = ACIYamlGenerator(vlan_request)

        os.makedirs(self.output_directory, exist_ok=True)

        output_file = os.path.join(
            self.output_directory,
            f"vlan-{vlan_request.vlan_id}.yaml",
        )

        try:
            rendered_yaml = generator.save_to_file(output_file)

            vlan_request.rendered_yaml = rendered_yaml
            vlan_request.status = "Generated"
            vlan_request.save()

            self.log_success(
                message=f"Generated YAML: {output_file}"
            )

        except Exception as exc:
            vlan_request.status = "Failed"
            vlan_request.save()

            self.log_failure(
                message=str(exc)
            )

            raise


register_jobs(GenerateACIYaml)