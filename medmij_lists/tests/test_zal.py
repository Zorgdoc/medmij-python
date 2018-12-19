# pylint: skip-file
from typing import Any
from unittest import TestCase
import lxml

import medmij_lists
from . import testdata


class TestZal(TestCase):
    def test_parse_ok(self) -> None:
        for xml in (testdata.ZAL_EXAMPLE_XML,
                    testdata.ZAL_EXAMPLE_EMPTY_XML):
            zal = medmij_lists.ZAL(xml)
            self.assertTrue(isinstance(zal, medmij_lists.ZAL))

    def test_parse_invalid_xml(self) -> None:
        with self.assertRaises(lxml.etree.XMLSyntaxError):
            medmij_lists.ZAL('<kapot')

    def test_parse_xsd_fail(self) -> None:
        for xml in (testdata.ZAL_XSD_FAIL1,
                    testdata.ZAL_XSD_FAIL2):
            with self.assertRaises(lxml.etree.XMLSyntaxError):
                medmij_lists.ZAL(xml)

    def test_zal_iter(self) -> None:
        zal = medmij_lists.ZAL(testdata.ZAL_EXAMPLE_XML)
        self.assertIsInstance(len(zal), int)
        self.assertGreaterEqual(len(zal), 1)
        zalist = list(zal)
        for e in zalist:
            self.assertIsInstance(e, str)

    def test_get_by_name(self) -> None:
        zal = medmij_lists.ZAL(testdata.ZAL_EXAMPLE_XML)
        self.assertIsInstance(zal["umcharderwijk@medmij"],
                              medmij_lists.Zorgaanbieder)
        key: Any
        for key in [" umcharderwijk@medmij", "UMCharderwijk@medmij", None, 3]:
            with self.assertRaises(KeyError):
                zal[key]

    def test_get_by_id(self) -> None:
        zal = medmij_lists.ZAL(testdata.ZAL_EXAMPLE_XML)
        za = zal["umcharderwijk@medmij"]
        self.assertIsInstance(za.gegevensdiensten["4"], medmij_lists.Gegevensdienst)
        key: Any
        for key in 4, "1", " 4", "", None:
            with self.assertRaises(KeyError):
                za.gegevensdiensten[key]

    def test_uris(self) -> None:
        zal = medmij_lists.ZAL(testdata.ZAL_EXAMPLE_XML)
        za = zal["umcharderwijk@medmij"]
        geg = za.gegevensdiensten["4"]
        self.assertRegex(geg.token_endpoint_uri,
                         '^https://...')
        self.assertRegex(geg.authorization_endpoint_uri,
                         '^https://...')
