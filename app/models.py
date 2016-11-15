from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5421/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# helper functions for columns
def character_column():
    return db.Column('character_id', db.Integer, db.ForeignKey('character.id'))

def god_column():
    return db.Column('god_id', db.Integer, db.ForeignKey('god.id'))

def hero_column():
    return db.Column('hero_id', db.Integer, db.ForeignKey('hero.id'))

def creature_column():
    return db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'))

def myth_column():
    return db.Column('myth_id', db.Integer, db.ForeignKey('myth.id'))

"""
Maps characters to parents if the parents are not gods
"""
characters_to_parents = db.Table('characters_to_parents',
                                 character_column(), character_column())

"""
Maps gods to their children
"""
gods_to_children = db.Table('gods_to_children',
                            god_column(), character_column())

"""
Maps creatures to related characters
"""
creatures_to_characters = db.Table('creatures_to_characters',
                                   creature_column(), character_column())

"""
Maps creatures to related myths
"""
creatures_to_myths = db.Table('creatures_to_myths',
                              creature_column(), myth_column())

"""
Maps myths to main characters
"""
myths_to_characters = db.Table('myths_to_characters',
                               myth_column(), character_column())

"""
Maps myths to related gods
"""
myths_to_gods = db.Table('myths_to_gods', myth_column(), god_column())


class God(db.Model):
    """
    Information about a god in Greek mythology.
    """

    __tablename__ = 'god'

    name = db.Column(db.String, primary_key=True)
    power = db.Column(db.String)
    roman_name = db.Column(db.String)
    power = db.Column(db.String)
    symbol = db.Column(db.String)
    olympian = db.Column(db.Boolean)
    father_god = db.Column(db.String, db.ForeignKey('god.name'))
    father_hero = db.Column(db.String, db.ForeignKey('hero.name'))
    mother_god = db.Column(db.String, db.ForeignKey('god.name'))
    mother_hero = db.Column(db.String, db.ForeignKey('hero.name'))

    def __init__(self, name, roman_name, power, symbol):
        self.name = name
        self.power = power
        self.roman_name = roman_name
        self.power = power
        self.symbol = symbol

    def __repr__(self):
        return '<God %r>' % self.name


class Hero(db.Model):
    """
    Information about a hero in Greek mythology.
    """

    __tablename__ = 'hero'

    name = db.Column(db.String, primary_key=True)
    hero_type = db.Column(db.String)
    father_god = db.Column(db.String, db.ForeignKey('god.name'))
    father_hero = db.Column(db.String, db.ForeignKey('hero.name'))
    mother_god = db.Column(db.String, db.ForeignKey('god.name'))
    mother_hero = db.Column(db.String, db.ForeignKey('hero.name'))  
    power = db.Column(db.String)
    home = db.Column(db.String)

    def __init__(self, name, hero_type, power, home):
        self.name = name
        self.hero_type = hero_type
        self.power = power
        self.home = home

    def __repr__(self):
        return '<Hero %r>' % self.name


class Location(db.Model):
    """
    Information about a location from Greek mythology.
    """

    __tablename__ = 'location'

    name = db.Column(db.String, primary_key=True)
    alt_name = db.Column(db.String)
    myth = db.Column(db.String, db.ForeignKey('myth.name'))
    location_type = db.Column(db.String)
    god = db.Column(db.String, db.ForeignKey('god.name'))

    def __init__(self, name, alt_name, location_type):
        self.name = name
        self.alt_name = alt_name
        self.location_type = location_type

    def __repr__(self):
        return '<Location %r>' % self.name

class Myth(db.Model):
    """
    Information about a myth from Greek mythology.
    """

    __tablename__ = 'myth'

    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)
    gods = db.Column(db.String, db.ForeignKey('god.name'))
    non_gods = db.Column(db.String, db.ForeignKey('hero.name'))
    place = db.Column(db.String)
    theme = db.Column(db.String)

    def __init__(self, name, description, place, theme):
        self.name = name
        self.description = description
        self.place = place
        self.theme = theme

    def __repr__(self):
        return '<Myth %r>' % self.name
