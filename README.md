# 🌐 Network Infrastructure Discovery

Python-based network infrastructure discovery and inventory platform designed to collect, normalize and correlate information from multiple infrastructure sources.

The project demonstrates an approach to building a centralized **Network Source of Truth** for enterprise environments.

> This repository contains a sanitized demonstration implementation.  
> All addresses, hostnames, credentials and infrastructure examples are fictional.

---

## 🎯 Project Goals

Enterprise network information is often distributed across multiple systems:

- Network devices
- Network management platforms
- IPAM / DCIM systems
- Monitoring systems
- Configuration files
- Legacy spreadsheets

The goal of this project is to automatically collect this information and build a unified infrastructure inventory that can be searched and consumed by engineers and automation tools.

---

## ⚙️ Key Features

- Multi-source network infrastructure discovery
- Inventory normalization into a unified data model
- Device correlation across multiple data sources
- REST API for infrastructure inventory access
- Search across hostnames, IP addresses, vendors, platforms and sites
- Infrastructure statistics and source visibility
- Modular architecture for adding new discovery sources
- Sanitized demo data suitable for public environments

---

## 🧩 What This Project Demonstrates

This project is intended to demonstrate practical network engineering and automation skills, including:

- **Python for Network Engineering** — collection, normalization and processing of infrastructure data
- **REST API Integration** — interaction with network management, inventory and infrastructure platforms
- **Network Source of Truth** — correlation of data from multiple systems into a unified inventory
- **DCIM / IPAM Integration** — working with platforms such as NetBox
- **Network Management Integration** — API-driven interaction with platforms such as FortiManager
- **Linux Operations** — deployment and operation of network automation services on Linux
- **Data Modeling** — normalization of heterogeneous network information into consistent structures
- **Infrastructure Search** — fast lookup of devices, addresses, vendors, platforms and sites
- **Automation Architecture** — modular design that can be extended with additional discovery sources

The overall engineering goal is to move network operations from isolated manual workflows toward **searchable, API-driven and automation-ready infrastructure data**.

---

## 🏗 Architecture

```text
                    +------------------+
                    |   Network APIs   |
                    +--------+---------+
                             |
                    +--------v---------+
                    |   DCIM / IPAM    |
                    +--------+---------+
                             |
+----------------+           |
| Inventory Files|-----------+
+----------------+           |
                             v
                  +----------------------+
                  |   Discovery Engine   |
                  |       Python         |
                  +----------+-----------+
                             |
                  +----------v-----------+
                  | Data Normalization   |
                  +----------+-----------+
                             |
                  +----------v-----------+
                  | Infrastructure Model |
                  +----------+-----------+
                             |
               +-------------+-------------+
               |                           |
       +-------v-------+           +-------v-------+
       |    REST API   |           |    Web UI     |
       +---------------+           +---------------+
```

---

## 🛠 Technology Stack

**Core:** Python · REST API · Linux  
**Infrastructure:** NetBox · FortiManager · DCIM / IPAM  
**Data:** Normalized infrastructure inventory  
**Interfaces:** REST API · Web UI

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/berikkhalmenov/network-infrastructure-discovery.git
cd network-infrastructure-discovery
```

Create a virtual environment:

```bash
python -m venv .venv
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The demo REST API will be available at:

```text
http://127.0.0.1:5000
```

### API Examples

Health check:

```text
GET /health
```

Normalized device inventory:

```text
GET /api/devices
```

Search the infrastructure inventory:

```text
GET /api/search?q=cisco
```

Inventory statistics:

```text
GET /api/stats
```

Example:

```bash
curl http://127.0.0.1:5000/api/devices
```

---

## 🔐 Public Demo & Security

This repository is designed as a **sanitized portfolio implementation**.

- No production credentials are included
- No production IP addresses or hostnames are included
- No private infrastructure configuration is included
- Example infrastructure data is fictional
- Secrets should be provided through environment variables or external secret-management mechanisms in real deployments

> All IP addresses, hostnames and infrastructure data in this repository are fictional and intended for demonstration purposes only.
