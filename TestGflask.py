#!/usr/bin/env python3

from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort
from unittest import main, TestCase
from gflask import error_wrapper, index, about_page, gods_model, heros_model, creatures_model, myths_model, god_page, hero_page, creature_page, myth_page, static_files

app = Flask(__name__)

#------------------------------------------------------------------------#
# WARNING :                                                              #
# All the test cases are dummy and can't be run right now                #
# and need to be fixed upon next Phases                                  #
#------------------------------------------------------------------------#

class MyUnitTest(TestCase) :
    def setUp (self) :
        self.app = app.test_client()

        self.a = [
            error_wrapper,
            index,
            about_page,
            gods_model,
            heros_model,
            creatures_model,
            myths_model,
            god_page,
            hero_page,
            creature_page,
            myth_page,
            static_files]

    #---------------------
    # test error_wrapper()
    #---------------------

    def test_1 (self) :
        res = self.app.get('/')
        assertEqual(res.data, 'error_template.html')

        for f in self.a :
            assertEqual(error_wrapper('error_template.html'), error_message)

    def test_2 (self) :
        for f in self.a :
            assertEqual(error_wrapper(' '), null)

    def test_3 (self) :
        for f in self.a :
            assertEqual(error_wrapper('error.html', 'Page for myth: ' + myth + ' to be added')

    #-------------------
    # test index()
    #-------------------
    def test_4 (self) :
        res = self.app.get('zeus')
        assertEqual(res.data, '/static/gods/zeus')

        for f in self.a :
            assertEqual(index('zeus'), '/static/gods/zeus')

    def test_5 (self) :
        for f in self.a :
            assertEqual(index('poseidon'), '/static/gods/poseidon')

    def test_6 (self) :
        for f in self.a :
            assertEqual(index('hades'), '/static/gods/hades')

    def test_7 (self) :
        for f in self.a :
            assertEqual(index('hercules'), '/static/heros/hercules')

    def test_8 (self) :
        for f in self.a :
            assertEqual(index('odysseus'), '/static/heros/odysseus')

    def test_9 (self) :
        for f in self.a :
            assertEqual(index('perseus'), '/static/heros/perseus')

    def test_10 (self) :
        for f in self.a :
            assertEqual(index('medusa'), '/static/creatures/medusa')

    def test_11 (self) :
        for f in self.a :
            assertEqual(index('arguspanoptes'), '/static/creatures/arguspanoptes')

    def test_12 (self) :
        for f in self.a :
            assertEqual(index('minotaur'), '/static/creatures/minotaur')

    #-------------------
    # test about_page
    #-------------------
    def test_13 (self) :
        for f in self.a :
            assertEqua(about_page('STATIC_ABOUT_PAGE'), '/static/about')

    def test_14 (self) :
        for f in self.a :
            assertEqua(about_page('ABOUT_PAGE'), 'About page to be added')

    #-------------------
    # test gods_model
    #-------------------
    def test_15 (self) :
        for f in self.a :
            assertEqua(gods_model(), '/static/gods.html')

    def test_16 (self) :
        for f in self.a :
            assertEqua(gods_model('GODS_LIST'), null)

    #-------------------
    # test heros_model
    #-------------------
    def test_17 (self) :
        for f in self.a :
            assertEqua(heros_model(), '/static/heros.html')

    def test_18 (self) :
        for f in self.a :
            assertEqua(heros_model('HEROS_LIST'), null)

    #-------------------
    # test creatures_model
    #-------------------
    def test_19 (self) :
        for f in self.a :
            assertEqua(creatures_model(), '/static/creatures.html')

    def test_20 (self) :
        for f in self.a :
            assertEqua(creatures_model('CREATURES_LIST'), null)

    #-------------------
    # test myths_model
    #-------------------
    def test_21 (self) :
        for f in self.a :
            assertEqua(myths_model(), '/static/myths.html')

    def test_22 (self) :
        for f in self.a :
            assertEqua(myths_model('MYTHS_LIST'), null)

    #-------------------
    # test gods_page
    #-------------------
    def test_23 (god) :
        for f in self.a :
            assertEqua(gods_page('hades'), '/static/gods/hades.html')

    def test_24 (god) :
        for f in self.a :
            assertEqua(gods_page('poseidon'), '/static/gods/poseidon.html')

    def test_25 (god) :
        for f in self.a :
            assertEqua(gods_page('zeus'), '/static/gods/zeus.html')

    #-------------------
    # test heros_page
    #-------------------
    def test_26 (hero) :
        for f in self.a :
            assertEqua(heros_page('hercules'), '/static/heros/hercules.html')

    def test_27 (hero) :
        for f in self.a :
            assertEqua(heros_page('odysseus'), '/static/heros/odysseus.html')

    def test_28 (hero) :
        for f in self.a :
            assertEqua(heros_page('perseus'), '/static/heros/perseus.html')

    #-------------------
    # test creatures_page
    #-------------------
    def test_29 (creature) :
        for f in self.a :
            assertEqua(creatures_page('arguspanoptes'), '/static/creatures/arguspanoptes.html')

    def test_30 (creature) :
        for f in self.a :
            assertEqua(creatures_page('medusa'), '/static/creatures/medusa.html')

    def test_31 (creature) :
        for f in self.a :
            assertEqua(creatures_page('minotaur'), '/static/creatures/minotaur.html')

    #-------------------
    # test myths_page
    #-------------------
    def test_32 (myth) :
        for f in self.a :
            assertEqua(myths_page('flightofdaedalusandicarus'), '/static/myths/flightofdaedalusandicarus.html')

    def test_33 (myth) :
        for f in self.a :
            assertEqua(myths_page('mythofperseus'), '/static/myths/mythofperseus.html')

    def test_34 (myth) :
        for f in self.a :
            assertEqua(myths_page('OrpheoandEurydice'), '/static/myths/OrpheoandEurydice.html')

    #-------------------
    # test static_files
    #-------------------
    def test_35 (folder, file) :
        for f in self.a :
            assertEqua(static_files(css, full_slider.css), '/static/css/full_slider.css')

    def test_36 (folder, file) :
        for f in self.a :
            assertEqua(static_files(gods, hades.html), '/static/gods/hades.html)')

    def test_37 (folder, file) :
        for f in self.a :
            assertEqua(static_files(heros, hercules.html), '/static/heros/hercules.html')

    def test_38 (folder, file) :
        for f in self.a :
            assertEqua(static_files(creatures, medusa.html), '/static/creatures/medusa.html')

    def test_39 (folder, file) :
        for f in self.a :
            assertEqua(static_files(myths, mythofperseus.html), '/static/css/mythofperseus.html')

#------
# main
#------
if __name__ == "__main__ " :
    main()
