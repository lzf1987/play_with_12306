import sys
from unittest import TestCase

sys.path.append('../../../src')
from core.tools.generate_headers import GenerateHeaders


class TestGenerateHeaders(TestCase):
    def test_get_rail_expiration_device_id(self):
        result = GenerateHeaders.get_rail_expiration_device_id()
        self.assertIsNotNone(result["RAIL_EXPIRATION"])
        self.assertIsNotNone(result["RAIL_DEVICEID"])

    def test_get_header(self):
        headers = GenerateHeaders.get_headers()
        self.assertIsNotNone(headers)
        self.assertIsNotNone(headers["User-Agent"])