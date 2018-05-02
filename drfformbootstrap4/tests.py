"""
Simple tests that verify templates can be rendered.
"""
from django.test import TestCase
from django.test import Client
from django.urls import reverse


class SerializerTestCase(TestCase):
    """
    Test template packs by rendering each page.
    """
    def setUp(self):
        self.client = Client()

    def _test_get_and_post(self, url_name):
        """
        Test both get and post requests for the given URL name.
        For post, the content will be empty, which will be invalid,
        but the response should still render with code 200.
        """
        get_resp = self.client.get(reverse(url_name))
        self.assertEqual(get_resp.status_code, 200)

        # Post an empty form- the serializer will be invalid, but
        # response should still be 200.
        post_resp = self.client.post(reverse(url_name), {})
        self.assertEqual(post_resp.status_code, 200)

    def test_horizontal(self):
        self._test_get_and_post('horizontal')

    def test_vertical(self):
        self._test_get_and_post('vertical')

    def test_inline(self):
        self._test_get_and_post('inline')
