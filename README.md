# medmij-python

## Installation

First start and activate a virtualenv:

```shell
$ python3.7 -m venv env
$ . env/bin/activate
(env) $
```

Clone the repo and install:

```shell
(env) $ PATH_TO_CLONE=~/example/medmij-python
(env) $ git clone https://github.com/GidsOpenStandaarden/OpenPGO-Medmij-ImplementatieBouwstenen-Python.git $PATH_TO_CLONE
...
(env) $ cd $PATH_TO_CLONE
(env) $ python setup.py install
...
```

## Usage

### Whitelist

```python
import urllib.request

import medmij

WHITELIST_URL = "https://afsprakenstelsel.medmij.nl/download/attachments/22348803/MedMij_Whitelist_example.xml"

with urllib.request.urlopen(WHITELIST_URL) as u:
    whitelist_xml = u.read()

whitelist = medmij.Whitelist(xmldata=whitelist_xml)

print('rcf-rso.nl' in whitelist)
print('example.com' in whitelist)
```

Run `whitelist.py`:

```shell
(env) $ python whitelist.py
True
False
```

### ZAL

```python
import urllib.request

import medmij

ZAL_URL = "https://afsprakenstelsel.medmij.nl/download/attachments/22348803/MedMij_Zorgaanbiederslijst_example.xml"

with urllib.request.urlopen(ZAL_URL) as u:
    zal_xml = u.read()

zal = medmij.ZAL(xmldata=zal_xml)
za = zal["umcharderwijk@medmij"]
print(za.gegevensdiensten["4"].authorization_endpoint_uri)
```

Run `zal.py`:

```shell
(env) $ python zal.py
https://medmij.za982.xisbridge.net/oauth/authorize
```

### OCL

```python
import urllib.request

import medmij

OCL_URL = "https://afsprakenstelsel.medmij.nl/download/attachments/22348803/MedMij_OAuthclientlist_example.xml"

with urllib.request.urlopen(OCL_URL) as u:
    ocl_xml = u.read()

ocl = medmij.OAuthclientList(xmldata=ocl_xml)
client = ocl["medmij.deenigeechtepgo.nl"]

print(client.organisatienaam)
```

Run `ocl.py`:

```shell
(env) $ python ocl.py
De Enige Echte PGO
```

### GNL

```python
import urllib.request

import medmij

GNL_URL = "https://afsprakenstelsel.medmij.nl/download/attachments/22348803/MedMij_Gegevensdienstnamenlijst_example.xml"

with urllib.request.urlopen(GNL_URL) as u:
    gnl_xml = u.read()

gnl = medmij.GNL(xmldata=gnl_xml)
gd = gnl["1"]

print(gd.weergavenaam)
```

Run `gnl.py`:

```shell
(env) $ python gnl.py
Basisgegevens Zorg
```
