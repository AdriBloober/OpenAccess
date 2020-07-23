---
description: How to install a OpenAccess server?
---

# Installation

## Requirements

You need a Linux-based server to setup up and install a OpenAccess server. Connect to him and run the following commands to install the requirements:

```
sudo apt-get install python3.8 python3-pip python3-venv
```

{% hint style="info" %}
If you have a non-Debian based Distribution google how to install python3.8 with pip and venv on this distribution.
{% endhint %}

## Set up OpenAccess

Clone the git repository:

```bash
git clone https://github.com/AdriBloober/OpenAccess
cd OpenAccess
python3.8 -m venv venv
```

Going into the virtual environment and install package requirements:

```bash
source venv/bin/active
python3.8 -m pip install -r requiremens.txt
```

{% page-ref page="configuration.md" %}



## Deploying

### Gunicorn

Install Gunicorn:

```bash
python3.8 -m pip install gunicorn
```

Run app with Gunicorn:

```bash
gunicorn resources:app
```

### Development server

```bash
python3.8 run.py # only for development environment
```

{% hint style="danger" %}
Use the development server not in production!
{% endhint %}

