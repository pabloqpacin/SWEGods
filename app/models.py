from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/greekmythology'
db = SQLAlchemy(app)

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

# characters to parents (who are not gods)
characters_to_parents = db.Table('characters_to_parents',
                                 character_column(), character_column())

# gods to children
gods_to_children = db.Table('gods_to_children',
                            god_column(), character_column())

# creatures to related characters
creatures_to_characters = db.Table('creatures_to_characters',
                                   creature_column(), character_column())

# creatures to related myths
creatures_to_myths = db.Table('creatures_to_myths',
                              creature_column(), myth_column())

# myths to main characters
myths_to_characters = db.Table('myths_to_characters',
                               myth_column(), character_column())

# myths to related gods
myths_to_gods = db.Table('myths_to_gods', myth_column(), god_column())


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    parents = db.relationship('Character', secondary=characters_to_parents)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Character %r>' % self.name


class God(Character):
    power = db.Column(db.String)
    olympian = db.Column(db.Boolean)
    children = db.relationship('Character', secondary=gods_to_children,
                               backref=db.backref('parents', lazy='dynamic'))
    symbol = db.Column(db.String)
    roman_counterpart = db.Column(db.String)

    def __init__(self, name, power, olympian, symbol, roman_counterpart):
        super().__init__(self, name)
        self.power = power
        self.olympian = olympian
        self.symbol = symbol
        self.roman_counterpart = roman_counterpart

    def __repr__(self):
        return '<God %r>' % self.name


class Hero(Character):
    hero_type = db.Column(db.String)
    strength_or_power = db.Column(db.String)
    death = db.Column(db.String)
    hero_origins = db.Column(db.String)

    def __init__(self, name, hero_type, strength_or_power, death, hero_origins):
        super().__init__(self, name)
        self.hero_type = hero_type
        self.strength_or_power = strength_or_power
        self.death = death
        self.hero_origins = hero_origins

    def __repr__(self):
        return '<Hero %r>' % self.name


class Creature(Character):
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