from IDB3 import app
from unittest import main, TestCase
from IDB3 import db, God, Hero, Location, Myth

GOD_COLS = ['name', 'power', 'romanname', 'power', 'symbol', 'father', 'mother']
HERO_COLS = ['name', 'herotype', 'father', 'mother', 'power', 'home']
LOCATION_COLS = ['name', 'altname', 'myth', 'locationtype', 'gods']
MYTH_COLS = ['name', 'description', 'gods', 'nongods', 'place', 'theme']
MODELS_TO_COLS = {
    God: GOD_COLS,
    Hero: HERO_COLS,
    Location: LOCATION_COLS,
    Myth: MYTH_COLS
}


class TestIDB(TestCase):

    def setUp(self):
        # Create Flask test client
        self.app = app.test_client()

        # self.a = [index, about_page, gods_model, heroes_model, creatures_model, myths_model, god_page, hero_page, location_page, myth_page, static_files, ]

    #------
    # index
    #------

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


    #-------
    # models
    #-------

    def test_models_work(self):
        for model in MODELS_TO_COLS:
            with self.subTest():
                model.query.all()

    def test_models_correct_cols(self):
        for model in MODELS_TO_COLS:
            with self.subTest():
                for col in MODELS_TO_COLS[model]:
                    with self.subTest():
                        self.assertTrue(hasattr(model, col))



#------
# main
#------
if __name__ == "__main__" :
    main()

