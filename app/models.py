from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@greekmythology.me:5432/greekmyths'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class God(db.Model):
    """
    Information about a god in Greek mythology.
    """

    __tablename__ = 'gods'

    name = db.Column(db.String, primary_key=True)
    power = db.Column(db.String)
    romanname = db.Column(db.String)
    power = db.Column(db.String)
    symbol = db.Column(db.String)
    father = db.Column(db.String)
    mother = db.Column(db.String)
    # fathergod = db.Column(db.String, db.ForeignKey('god.name'))
    # fatherhero = db.Column(db.String, db.ForeignKey('hero.name'))
    # mothergod = db.Column(db.String, db.ForeignKey('god.name'))
    # motherhero = db.Column(db.String, db.ForeignKey('hero.name'))

    def __init__(self, name, romanname, power, symbol, father, mother):
        self.name = name
        self.power = power
        self.romanname = romanname
        self.power = power
        self.symbol = symbol
        self.father = father
        self.mother = mother

    def __repr__(self):
        return '<God %r>' % self.name


class Hero(db.Model):
    """
    Information about a hero in Greek mythology.
    """

    __tablename__ = 'heroes'

    name = db.Column(db.String, primary_key=True)
    herotype = db.Column(db.String)
    father = db.Column(db.String)
    mother = db.Column(db.String)
    # father_god = db.Column(db.String, db.ForeignKey('god.name'))
    # father_hero = db.Column(db.String, db.ForeignKey('hero.name'))
    # mother_god = db.Column(db.String, db.ForeignKey('god.name'))
    # mother_hero = db.Column(db.String, db.ForeignKey('hero.name'))  
    power = db.Column(db.String)
    home = db.Column(db.String)

    def __init__(self, name, herotype, father, mother, power, home):
        self.name = name
        self.herotype = herotype
        self.father = father
        self.mother = mother
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
    locationtype = db.Column(db.String)
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
    nongods = db.Column(db.String)
    place = db.Column(db.String)
    theme = db.Column(db.String)

    def __init__(self, name, description, other_characters, place, theme):
        self.name = name
        self.description = description
        self.other_characters = other_characters
        self.place = place
        self.theme = theme

    def __repr__(self):
        return '<Myth %r>' % self.name

print(God.query.all())
print(Hero.query.all())