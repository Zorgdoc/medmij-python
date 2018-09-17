# pylint: skip-file
from unittest import TestCase
import lxml

import medmij
from . import testdata


class TestWhitelist(TestCase):
    def test_parse_ok(self) -> None:
        for xml in (testdata.WHITELIST_EXAMPLE_XML,
                    testdata.WHITELIST_EXAMPLE_SINGLE_XML):
            whitelist = medmij.Whitelist(xml)
            self.assertTrue(isinstance(whitelist, medmij.Whitelist))

    def test_parse_invalid_xml(self) -> None:
        with self.assertRaises(lxml.etree.XMLSyntaxError):
            medmij.Whitelist('<kapot')

    def test_parse_xsd_fail(self) -> None:
        for xml in (testdata.WHITELIST_XSD_FAIL1,
                    testdata.WHITELIST_XSD_FAIL2):
            with self.assertRaises(lxml.etree.XMLSyntaxError):
                medmij.Whitelist(xml)

    def test_whitelist_contains(self) -> None:
        whitelist = medmij.Whitelist(testdata.WHITELIST_EXAMPLE_XML)
        self.assertIn("rcf-rso.nl", whitelist)
        self.assertNotIn("rcf-rso.nl.", whitelist)
        self.assertNotIn("RFC-RSO.NL", whitelist)
        self.assertNotIn(None, whitelist)

    def test_zal_iter(self) -> None:
        whitelist = medmij.Whitelist(testdata.WHITELIST_EXAMPLE_XML)
        self.assertIsInstance(len(whitelist), int)
        self.assertGreaterEqual(len(whitelist), 1)
        whlst = list(whitelist)
        for e in whlst:
            self.assertIsInstance(e, str)
