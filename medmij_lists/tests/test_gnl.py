# pylint: skip-file
from typing import Any
from unittest import TestCase
import lxml

import medmij_lists
from . import testdata


class TestZal(TestCase):
    def test_parse_ok(self) -> None:
        gnl = medmij_lists.GNL(testdata.GNL_EXAMPLE_XML)
        self.assertTrue(isinstance(gnl, medmij_lists.GNL))

    def test_parse_invalid_xml(self) -> None:
        with self.assertRaises(lxml.etree.XMLSyntaxError):
            medmij_lists.GNL('<kapot')

    def test_get_by_id(self) -> None:
        gnl = medmij_lists.GNL(testdata.GNL_EXAMPLE_XML)
        gd = gnl["1"]
        self.assertEqual("Basisgegevens Zorg", gd.weergavenaam)
