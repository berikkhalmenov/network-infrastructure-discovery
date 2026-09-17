from flask import Flask, jsonify, request

app = Flask(__name__)


# -------------------------------------------------------------------
# Demo inventory
# All addresses and hostnames are fictional and safe for public use.
# -------------------------------------------------------------------

DEVICES = [
    {
        "id": 1,
        "hostname": "core-sw-01",
        "management_ip": "192.0.2.10",
        "vendor": "Cisco",
        "platform": "NX-OS",
        "site": "DC-01",
        "role": "core-switch",
        "source": "network-api",
    },
    {
        "id": 2,
        "hostname": "edge-fw-01",
        "management_ip": "192.0.2.20",
        "vendor": "Fortinet",
        "platform": "FortiOS",
        "site": "DC-01",
        "role": "firewall",
        "source": "network-api",
    },
    {
        "id": 3,
        "hostname": "branch-rtr-01",
        "management_ip": "198.51.100.10",
        "vendor": "Huawei",
        "platform": "VRP",
        "site": "BRANCH-01",
        "role": "wan-router",
        "source": "inventory-file",
    },
    {
        "id": 4,
        "hostname": "access-sw-01",
        "management_ip": "198.51.100.20",
        "vendor": "HPE",
        "platform": "Comware",
        "site": "BRANCH-01",
        "role": "access-switch",
        "source": "dcim",
    },
]


@app.route("/health", methods=["GET"])
def health():
    """Simple application health check."""
    return jsonify(
        {
            "status": "ok",
            "service": "network-infrastructure-discovery",
        }
    )


@app.route("/api/devices", methods=["GET"])
def get_devices():
    """Return the complete normalized device inventory."""
    return jsonify(
        {
            "count": len(DEVICES),
            "devices": DEVICES,
        }
    )


@app.route("/api/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    """Return one device by its inventory ID."""
    device = next(
        (item for item in DEVICES if item["id"] == device_id),
        None,
    )

    if device is None:
        return jsonify({"error": "device not found"}), 404

    return jsonify(device)


@app.route("/api/search", methods=["GET"])
def search_devices():
    """Search inventory by hostname, IP, vendor, site or role."""
    query = request.args.get("q", "").strip().lower()

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

    results = [
        device
        for device in DEVICES
        if any(
            query in str(device.get(field, "")).lower()
            for field in searchable_fields
        )
    ]

    return jsonify(
        {
            "query": query,
            "count": len(results),
            "devices": results,
        }
    )


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return basic statistics about the discovered inventory."""
    sites = sorted({device["site"] for device in DEVICES})
    vendors = sorted({device["vendor"] for device in DEVICES})
    sources = sorted({device["source"] for device in DEVICES})

    return jsonify(
        {
            "devices": len(DEVICES),
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
