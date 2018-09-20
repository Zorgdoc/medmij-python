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
(env) $ git clone https://github.com/Zorgdoc/medmij-python.git $PATH_TO_CLONE
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

WHITELIST_URL = "http://gids.samenbeter.org/openpgoexamples/whitelist-voorbeeld-v1.0.xml"

with urllib.request.urlopen(WHITELIST_URL) as u:
    whitelist_xml = u.read()

whitelist = medmij.Whitelist(xmldata=whitelist_xml)

print('rcf-rso.nl' in whitelist)
print('example.com' in whitelist)
```

Run `whitelist.py`:

```shell
(env) $ python whitelist.py
...
lxml.etree.XMLSyntaxError: Element '{http://afsprakenstelsel.medmij.nl/whitelist/1_0/schema/}Whitelist': No matching global declaration available for the validation root.
```

### ZAL

```python
import urllib.request

import medmij

ZAL_URL = "http://gids.samenbeter.org/openpgoexamples/zorgaanbiederslijst-voorbeeld-v1.0.xml"

with urllib.request.urlopen(ZAL_URL) as u:
    zal_xml = u.read()

zal = medmij.ZAL(xmldata=zal_xml)
za = zal["umcharderwijk@medmij"]
print(za.gegevensdiensten["4"].authorization_endpoint_uri)
```

Run `zal.py`:

```shell
(env) $ python zal.py
...
lxml.etree.XMLSyntaxError: Element '{http://afsprakenstelsel.medmij.nl/zorgaanbiederslijst/1_0/schema/}Zorgaanbiederslijst': No matching global declaration available for the validation root.
```

### OCL

```python
import urllib.request

import medmij

OCL_URL = "http://gids.samenbeter.org/openpgoexamples/oauthclientlist-voorbeeld-v1.0.xml"

with urllib.request.urlopen(OCL_URL) as u:
    ocl_xml = u.read()

ocl = medmij.OAuthclientList(xmldata=ocl_xml)
client = ocl["medmij.deenigeechtepgo.nl"]

print(client.organisatienaam)
```

Run `ocl.py`:

```shell
(env) $ python ocl.py
...
lxml.etree.XMLSyntaxError: Element '{http://afsprakenstelsel.medmij.nl/oauthclientlist/1_0/schema/}OAuthclientlist': No matching global declaration available for the validation root.
```
