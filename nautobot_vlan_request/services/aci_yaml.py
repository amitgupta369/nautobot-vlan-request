import yaml


class ACIYamlGenerator:

    def __init__(self, vlan_request):
        self.vlan_request = vlan_request

    def build_payload(self):
        payload = {
            "apic": {
                "tenants": [
                    {
                        "name": self.vlan_request.tenant,
                        "vrfs": [
                            {
                                "name": self.vlan_request.vrf
                            }
                        ],
                        "bridge_domains": [
                            {
                                "name": f"{self.vlan_request.vlan_name}-BD",
                                "vrf": self.vlan_request.vrf,
                                "subnets": [
                                    {
                                        "ip": self.vlan_request.subnet,
                                    }
                                ]
                            }
                        ],
                        "application_profiles": [
                            {
                                "name": "APP-PROFILE",
                                "endpoint_groups": [
                                    {
                                        "name": self.vlan_request.vlan_name,
                                        "bridge_domain": f"{self.vlan_request.vlan_name}-BD"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }

        return payload

    def render_yaml(self):
        payload = self.build_payload()
        return yaml.dump(payload, sort_keys=False)

    def save_to_file(self, output_path):
        rendered_yaml = self.render_yaml()

        with open(output_path, "w") as file:
            file.write(rendered_yaml)

        return rendered_yaml