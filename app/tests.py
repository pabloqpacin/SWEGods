from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort
from unittest import main, TestCase
from IDB3 import error_wrapper, index, about_page, gods_model, heroes_model, creatures_model, myths_model, god_page, hero_page, creature_page, myth_page, static_files

app = Flask(__name__)

#------------------------------------------------------------------------#
# WARNING :                                                              #
# All the test cases are dummy and can't be run right now                #
# and need to be fixed upon next Phases                                  #
#------------------------------------------------------------------------#

class TestIDB(TestCase):
    def setUp (self) :
        self.app = app.test_client()

        self.a = [
            error_wrapper,
            index,
            about_page,
            gods_model,
            heroes_model,
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

    #-------------------
    # test index()
    #-------------------

    #-------------------
    # test about_page
    #-------------------

    #-------------------
    # test gods_model
    #-------------------

    #-------------------
    # test heroes_model
    #-------------------

    #-------------------
    # test creatures_model
    #-------------------

    #-------------------
    # test myths_model
    #-------------------

    #-------------------
    # test gods_page
    #-------------------

    #-------------------
    # test heroes_page
    #-------------------

    #-------------------
    # test creatures_page
    #-------------------

    #-------------------
    # test myths_page
    #-------------------

    #-------------------
    # test static_files
    #-------------------

#------
# main
#------
if __name__ == "__main__ " :
    main()
