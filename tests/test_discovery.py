from discovery import correlate_devices, normalize_device, normalize_inventory


def test_normalize_device_hostname():
    raw_device = {
        "hostname": "CORE-SW-01",
        "management_ip": "192.0.2.10",
        "vendor": "Cisco",
        "platform": "NX-OS",
        "site": "DC-01",
        "role": "core-switch",
    }

    device = normalize_device(raw_device, "network-api")

    assert device.hostname == "core-sw-01"
    assert device.management_ip == "192.0.2.10"
    assert device.source == "network-api"


def test_correlate_devices_from_multiple_sources():
    network_api = normalize_inventory(
        [
            {
                "hostname": "core-sw-01",
                "management_ip": "192.0.2.10",
                "vendor": "Cisco",
                "platform": "NX-OS",
                "site": "DC-01",
                "role": "core-switch",
            }
        ],
        "network-api",
    )

    dcim = normalize_inventory(
        [
            {
                "hostname": "CORE-SW-01",
                "management_ip": "192.0.2.10",
                "vendor": "Cisco",
                "platform": "NX-OS",
                "site": "DC-01",
                "role": "core-switch",
            }
        ],
        "dcim",
    )

    devices = correlate_devices(network_api, dcim)

    assert len(devices) == 1
    assert devices[0]["management_ip"] == "192.0.2.10"
    assert devices[0]["hostname"] == "core-sw-01"
    assert set(devices[0]["sources"]) == {"network-api", "dcim"}


def test_device_without_management_ip_is_ignored():
    inventory = normalize_inventory(
        [
            {
                "hostname": "unknown-device",
                "management_ip": "",
                "vendor": "Cisco",
                "platform": "IOS-XE",
                "site": "LAB-01",
                "role": "router",
            }
        ],
        "inventory-file",
    )

    devices = correlate_devices(inventory)

    assert devices == []
