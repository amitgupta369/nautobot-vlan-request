"""Provisioning workflow."""

from pathlib import Path

from django.conf import settings

from nautobot.extras.models import Secret

from nautobot_vlan_request.models import VLANRequest
from nautobot_vlan_request.services.aci_yaml import ACIYamlGenerator
from nautobot_vlan_request.services.git.git_service import GitService


class ProvisioningService:
    """Provision VLAN request into Git repository."""

    def __init__(self, vlan_request: VLANRequest):
        self.vlan_request = vlan_request

        plugin_config = settings.PLUGINS_CONFIG["nautobot_vlan_request"]["git"]

        self.repository = Path(plugin_config["repository"])
        self.default_branch = plugin_config["branch"]
        self.yaml_directory = plugin_config["yaml_directory"]
        self.username = Path(plugin_config["username"])
        secret = Secret.objects.get(name="github-token")
        self.token = secret.get_value()

    def execute(self):
        """Execute complete provisioning workflow."""

        #
        # Step 1 - Generate YAML
        #
        generator = ACIYamlGenerator(self.vlan_request)

        rendered_yaml = generator.render_yaml()

        self.vlan_request.rendered_yaml = rendered_yaml
        self.vlan_request.status = "Generated"
        self.vlan_request.save()

        #
        # Step 2 - Build branch name
        #
        branch_name = (
            f"feature/"
            f"{self.vlan_request.tenant}_"
            f"{self.vlan_request.vrf}_"
            f"{self.vlan_request.vlan_id}"
        ).replace(" ", "-").lower()

        #
        # Step 3 - YAML destination
        #
        yaml_file = (
            self.repository
            / self.yaml_directory
            / self.vlan_request.tenant.lower()
            / f"vlan-{self.vlan_request.vlan_id}.yaml"
        )

        yaml_file.parent.mkdir(parents=True, exist_ok=True)

        yaml_file.write_text(rendered_yaml)

        #
        # Step 4 - Git
        #
        #git = GitService(self.repository)

        git = GitService(
            repository=self.repository,
            username=self.username,
            token=self.token,
        )

        git.configure_remote()

        git.checkout(self.default_branch)

        git.create_branch(branch_name)

        git.add(yaml_file)

        commit = git.commit(
            message=(
                f"Create VLAN {self.vlan_request.vlan_id} "
                f"({self.vlan_request.vlan_name})"
            )
        )

        git.push(branch_name)

        #
        # Step 5 - Update Nautobot
        #
        self.vlan_request.git_branch = branch_name
        self.vlan_request.git_commit = commit.hexsha
        self.vlan_request.status = "Committed"
        self.vlan_request.save()

        return self.vlan_request