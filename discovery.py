from dataclasses import dataclass, asdict
from typing import Iterable


@dataclass
class NetworkDevice:
    """Normalized representation of a network device."""

    hostname: str
    management_ip: str
    vendor: str
    platform: str
    site: str
    role: str
    source: str


def normalize_device(raw: dict, source: str) -> NetworkDevice:
    """
    Convert source-specific network data into
    a common infrastructure model.
    """

    return NetworkDevice(
        hostname=str(raw.get("hostname", "")).strip().lower(),
        management_ip=str(raw.get("management_ip", "")).strip(),
        vendor=str(raw.get("vendor", "unknown")).strip(),
        platform=str(raw.get("platform", "unknown")).strip(),
        site=str(raw.get("site", "unknown")).strip(),
        role=str(raw.get("role", "unknown")).strip(),
        source=source,
    )


def normalize_inventory(
    devices: Iterable[dict],
    source: str,
) -> list[dict]:
    """
    Normalize a collection of devices received
    from an API, DCIM/IPAM platform or inventory file.
    """

    normalized = []

    for device in devices:
        item = normalize_device(device, source)
        normalized.append(asdict(item))

    return normalized


def correlate_devices(*inventories: list[dict]) -> list[dict]:
    """
    Merge inventories using management IP as the
    correlation key.

    If the same device exists in several sources,
    information from the later source is merged
    into the existing record.
    """

    correlated = {}

    for inventory in inventories:
        for device in inventory:
            management_ip = device.get("management_ip")

            if not management_ip:
                continue

            if management_ip not in correlated:
                correlated[management_ip] = device.copy()
                correlated[management_ip]["sources"] = [
                    device.get("source", "unknown")
                ]
                continue

            existing = correlated[management_ip]

            for key, value in device.items():
                if value and value != "unknown":
                    existing[key] = value

            source = device.get("source")

            if source and source not in existing["sources"]:
                existing["sources"].append(source)

    return list(correlated.values())
