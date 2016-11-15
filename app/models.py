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
    father_god = db.Column(db.String, db.ForeignKey('god.name'), nullable=True)
    father_hero = db.Column(db.String, db.ForeignKey('hero.name'),
                            nullable=True)
    roman_counterpart = db.Column(db.String)

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
    creature_type = db.Column(db.String)
    characteristics = db.Column(db.String)
    related_characters = db.relationship('Character',
                                         secondary=creatures_to_characters)
    related_myths = db.relationship('Myth',
                                    secondary=creatures_to_myths)

    def __init__(self, name, creature_type, characteristics):
        super().__init__(self, name)
        self.creature_type = creature_type
        self.characteristics = characteristics

    def __repr__(self):
        return '<Creature %r>' % self.name

class Myth(db.Model):
    """
    Information about a myth from Greek mythology.
    """

    __tablename__ = 'myth'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    main_characters = db.relationship('Character',
                                      secondary=myths_to_characters)
    related_gods = db.relationship('God', secondary=myths_to_gods)
    summary = db.Column(db.String)
    impact_on_greek_life = db.Column(db.String)

    def __init__(self, name, summary, impact_on_greek_life):
        self.name = name
        self.summary = summary
        self.impact_on_greek_life = impact_on_greek_life

    def __repr__(self):
        return '<Myth %r>' % self.name
