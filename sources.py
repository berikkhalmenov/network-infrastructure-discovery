"""
Demo infrastructure data sources.

All addresses, hostnames and site names in this module
are fictional and intended for demonstration only.
"""


def get_network_api_devices() -> list[dict]:
    """Simulate devices collected from a network management API."""

    return [
        {
            "hostname": "core-sw-01",
            "management_ip": "192.0.2.10",
            "vendor": "Cisco",
            "platform": "NX-OS",
            "site": "DC-01",
            "role": "core-switch",
        },
        {
            "hostname": "edge-fw-01",
            "management_ip": "192.0.2.20",
            "vendor": "Fortinet",
            "platform": "FortiOS",
            "site": "DC-01",
            "role": "firewall",
        },
    ]


def get_dcim_devices() -> list[dict]:
    """Simulate devices received from a DCIM/IPAM system."""

    return [
        {
            "hostname": "CORE-SW-01",
            "management_ip": "192.0.2.10",
            "vendor": "Cisco",
            "platform": "NX-OS",
            "site": "DC-01",
            "role": "core-switch",
        },
        {
            "hostname": "branch-rtr-01",
            "management_ip": "192.0.2.30",
            "vendor": "Cisco",
            "platform": "IOS-XE",
            "site": "BRANCH-01",
            "role": "router",
        },
    ]


def get_inventory_file_devices() -> list[dict]:
    """Simulate records imported from a legacy inventory file."""

    return [
        {
            "hostname": "branch-rtr-01",
            "management_ip": "192.0.2.30",
            "vendor": "Cisco",
            "platform": "IOS-XE",
            "site": "BRANCH-01",
            "role": "router",
        }
    ]
