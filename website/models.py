# create database models
# one for users, one for notes (will be exercise log)

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # func.now get current time that note is made and assocites it with the note
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # associate note with user so set up realtion between note object and user object
    # foriegn key is a column of 1 database that always references a column of another database to link them
    # one to many relationship -- 1 object w many children -- 1 user w many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    # need primary key, ie a way to differentiate all users if they can have info like thier name so need a unique id
    id = db.Column(db.Integer, primary_key=True)
    # string(max length of string). unique is true so no same emails can be used
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # add notes id when user creates it so can see all notes one user created
    notes = db.relationship('Note')
    # argument is class name you are creating relationship with
    workouts = db.relationship('Workout')


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(10000))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # if adding new column to class after first creation need to delete the whole DB file?? added date this way to workout and it worked, got error from SQL before deleting the file
