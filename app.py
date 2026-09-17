from flask import Flask, jsonify, request

from discovery import correlate_devices, normalize_inventory
from sources import (
    get_dcim_devices,
    get_inventory_file_devices,
    get_network_api_devices,
)

app = Flask(__name__)


def build_inventory() -> list[dict]:
    """
    Collect demo data from multiple infrastructure sources,
    normalize it and correlate duplicate devices.
    """

    network_api = normalize_inventory(
        get_network_api_devices(),
        "network-api",
    )

    dcim = normalize_inventory(
        get_dcim_devices(),
        "dcim",
    )

    inventory_file = normalize_inventory(
        get_inventory_file_devices(),
        "inventory-file",
    )

    devices = correlate_devices(
        network_api,
        dcim,
        inventory_file,
    )

    return sorted(
        devices,
        key=lambda device: device["management_ip"],
    )


@app.route("/health", methods=["GET"])
def health():
    """Application health check."""

    return jsonify(
        {
            "status": "ok",
            "service": "network-infrastructure-discovery",
        }
    )


@app.route("/api/devices", methods=["GET"])
def get_devices():
    """Return the normalized and correlated inventory."""

    devices = build_inventory()

    return jsonify(
        {
            "count": len(devices),
            "devices": devices,
        }
    )


@app.route("/api/devices/<path:management_ip>", methods=["GET"])
def get_device(management_ip):
    """Return one device by management IP address."""

    devices = build_inventory()

    device = next(
        (
            item
            for item in devices
            if item["management_ip"] == management_ip
        ),
        None,
    )

    if device is None:
        return jsonify({"error": "device not found"}), 404

    return jsonify(device)


@app.route("/api/search", methods=["GET"])
def search_devices():
    """
    Search inventory by hostname, IP address,
    vendor, platform, site, role or source.
    """

    query = request.args.get("q", "").strip().lower()
    devices = build_inventory()

    if not query:
        return jsonify(
            {
                "query": "",
                "count": 0,
                "devices": [],
            }
        )

    searchable_fields = (
        "hostname",
        "management_ip",
        "vendor",
        "platform",
        "site",
        "role",
        "source",
    )

    results = []

    for device in devices:
        searchable_values = [
            str(device.get(field, "")).lower()
            for field in searchable_fields
        ]

        searchable_values.extend(
            str(source).lower()
            for source in device.get("sources", [])
        )

        if any(query in value for value in searchable_values):
            results.append(device)

    return jsonify(
        {
            "query": query,
            "count": len(results),
            "devices": results,
        }
    )


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return basic statistics for the discovered inventory."""

    devices = build_inventory()

    sites = sorted(
        {
            device["site"]
            for device in devices
            if device.get("site")
        }
    )

    vendors = sorted(
        {
            device["vendor"]
            for device in devices
            if device.get("vendor")
        }
    )

    sources = sorted(
        {
            source
            for device in devices
            for source in device.get("sources", [])
        }
    )

    return jsonify(
        {
            "devices": len(devices),
            "sites": len(sites),
            "vendors": len(vendors),
            "sources": len(sources),
            "site_names": sites,
            "vendor_names": vendors,
            "source_names": sources,
        }
    )


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "resource not found"}), 404


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )
