from nautobot.apps.ui import (
    NavMenuItem,
    NavMenuTab,
    NavMenuGroup,
)

menu_items = (
    NavMenuTab(
        name="VLAN Requests",
        groups=(
            NavMenuGroup(
                name="Requests",
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_vlan_request:vlanrequest_list",
                        name="VLAN Requests",
                    ),
                ),
            ),
        ),
    ),
)