#!/usr/bin/env python

"""Tests for the Shareabouts Flask Client."""

import unittest
from app import create_app


class TestApp(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_example(self):
        pass

if __name__ == '__main__':
    unittest.main()
