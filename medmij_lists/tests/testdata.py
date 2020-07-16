"""Testdata"""
import pkg_resources


def _load(name: str) -> bytes:
    return pkg_resources.resource_string(__name__, name)


WHITELIST_EXAMPLE_XML = _load("whitelist_example.xml")
WHITELIST_EXAMPLE_SINGLE_XML = _load("whitelist_example_single.xml")
WHITELIST_XSD_FAIL1 = "<test/>"
WHITELIST_XSD_FAIL2 = """<Whitelist
    xmlns="xmlns://afsprakenstelsel.medmij.nl/whitelist/release2/"
/>"""

ZAL_EXAMPLE_XML = _load("zal_example.xml")
ZAL_EXAMPLE_EMPTY_XML = _load("zal_example_empty.xml")
ZAL_XSD_FAIL1 = "<test/>"
ZAL_XSD_FAIL2 = """<ZAL
    xmlns="xmlns://afsprakenstelsel.medmij.nl/zorgaanbiederslijst/release2/"
/>"""

OAUTHCLIENTLIST_EXAMPLE_XML = _load("oauthclientlist_example.xml")

GNL_EXAMPLE_XML = _load("gnl_example.xml")
