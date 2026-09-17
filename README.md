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
