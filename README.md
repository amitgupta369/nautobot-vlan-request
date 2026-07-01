# Nautobot VLAN Request

Custom Nautobot app for VLAN request workflow management.

## Requirements

* Nautobot `>=3.1,<3.2`
* Python `>=3.12,<3.14`

Validate:

```bash
nautobot-server --version
```

---

## Installation

Clone repo:

```bash
git clone https://github.com/amitgupta369/nautobot-vlan-request.git
cd nautobot-vlan-request
```

Activate Nautobot virtual environment:

```bash
source /opt/nautobot/bin/activate
```

### Development Install

```bash
pip install -e .
```

### Stable Install

```bash
pip install .
```

### Install Specific Release

```bash
pip install git+https://github.com/amitgupta369/nautobot-vlan-request.git@v0.1.0
```

---

## Enable Plugin

Edit `nautobot_config.py`:
nano ~/.nautobot/nautobot_config.py

```python
PLUGINS = ["nautobot_vlan_request"]
```

---

## Validate

```bash
nautobot-server check
```

Verify:

```bash
pip show nautobot-vlan-request
```

Current release:

```text
v0.1.0
```
