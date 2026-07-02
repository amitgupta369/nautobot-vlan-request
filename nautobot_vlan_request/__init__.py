"""App declaration for nautobot_vlan_request."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version("nautobot-vlan-request")


class NautobotVLANRequestConfig(NautobotAppConfig):
    """App configuration for the nautobot_vlan_request app."""

    name = "nautobot_vlan_request"
    verbose_name = "Nautobot Vlan Request App"
    version = __version__
    author = "Amit Gupta"
    description = "Nautobot VLAN Request App developed by HCLTech"

config = NautobotVLANRequestConfig  # pylint:disable=invalid-name

jobs = ["nautobot_vlan_request.jobs"]