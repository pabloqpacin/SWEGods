import IDB3
from IDB3 import *
import app
from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort
import unittest
import os
import json
from flask_testing import TestCase

# app = Flask(__name__)

class tests(unittest.TestCase) :

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Create Flask test client
        self.app = IDB3.app.test_client()

        self.a = [index, about_page, gods_model, heroes_model, creatures_model, myths_model, god_page, hero_page, location_page, myth_page, static_files, ]

    def test_index(self):
        self.assertEqual(self.app.get('/').status, '200 OK')

    def test_index_2(self):
        self.assertEqual(self.app.get('/gods/').status, '200 OK')

    def test_index_3(self):
        self.assertEqual(self.app.get('/god/').status, '404 NOT FOUND')

    def test_index_4(self):
        self.assertEqual(self.app.get('/gods/zeus/').status, '200 OK')

    def test_index_5(self):
        self.assertEqual(self.app.get('/gods/zeu').status, '301 MOVED PERMANENTLY')

    def test_index_6(self):
        self.assertEqual(self.app.get('/heroes/').status, '200 OK')

    def test_index_7(self):
        self.assertEqual(self.app.get('/hero/').status, '404 NOT FOUND')

    def test_index_8(self):
        self.assertEqual(self.app.get('/heroes/apollo/').status, '200 OK')

    def test_index_9(self):
        self.assertEqual(self.app.get('/heroes/apoll').status, '301 MOVED PERMANENTLY')

    def test_index_10(self):
        self.assertEqual(self.app.get('/heroes/somehero/').status, '200 OK')

    def test_index_11(self):
        self.assertEqual(self.app.get('/about/').status, '200 OK')

    def test_index_12(self):
        self.assertEqual(self.app.get('/about').status, '301 MOVED PERMANENTLY')

    def test_index_13(self):
        self.assertEqual(self.app.get('/bout/').status, '404 NOT FOUND')

    def test_index_14(self):
        self.assertEqual(self.app.get('/about/something/').status, '404 NOT FOUND')

    def test_index_15(self):
        self.assertEqual(self.app.get('/locations/').status, '200 OK')

    def test_index_16(self):
        self.assertEqual(self.app.get('/location/').status, '404 NOT FOUND')

    def test_index_17(self):
        self.assertEqual(self.app.get('/locations/troy/').status, '200 OK')

    def test_index_18(self):
        self.assertEqual(self.app.get('/locations/someplace/').status, '200 OK')

    def test_index_19(self):
        self.assertEqual(self.app.get('/locations/troys').status, '301 MOVED PERMANENTLY')

    def test_index_20(self):
        self.assertEqual(self.app.get('/gods/somegod/').status, '200 OK')

    def test_index_21(self):
        self.assertEqual(self.app.get('/myths/').status, '200 OK')

    def test_index_22(self):
        self.assertEqual(self.app.get('/myth/').status, '404 NOT FOUND')

    def test_index_23(self):
        self.assertEqual(self.app.get('/myths/The Myth of Europe/').status, '200 OK')

    def test_index_24(self):
        self.assertEqual(self.app.get('/myths/somemyths/').status, '200 OK')

    def test_index_25(self):
        self.assertEqual(self.app.get('/myths/troys').status, '301 MOVED PERMANENTLY')

    def test_index_26(self):
        self.assertEqual(self.app.get('/search/zeus').status, '404 NOT FOUND')

    def test_index_27(self):
        self.assertEqual(self.app.get('/search/gods').status, '404 NOT FOUND')

    def test_index_28(self):
        self.assertEqual(self.app.get('/search/heroes').status, '404 NOT FOUND')

    def test_index_29(self):
        self.assertEqual(self.app.get('/search/locations').status, '404 NOT FOUND')

    def test_index_30(self):
        self.assertEqual(self.app.get('/search/myths').status, '404 NOT FOUND')

if(__name__ == '__main__'):
    unittest.main()
