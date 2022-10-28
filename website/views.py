from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Workout, User
from . import db
import json

# blueprints essential define that there are routes(urls) in this file, so not all 'views/urls' are in 1 file. they are organized in normal routes and authenticated routes in 'auth.py'
views = Blueprint('views', __name__)


# below function will run whenever user goes to url, in this case the '/' url or mainpage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


# set up url and what methods will used on page
@views.route('/workout', methods=['GET', 'POST'])
@login_required  # makes this shown after user logs in
def workouts():
    if request.method == 'POST':
        exercise = request.form.get('exercise')  # gets input from forms
        reps = request.form.get('reps')
        weight = request.form.get('weight')

        if len(exercise) < 2:
            flash('Exercise name is too short!', category='error')
        if len(reps) < 1:
            flash('Did you do 0 reps? Do more!', category='error')
        else:
            new_workout = Workout(exercise=exercise, reps=reps,
                                  weight=weight, user_id=current_user.id)  # creating workout object from inputs and id to commit to the database
            db.session.add(new_workout)
            db.session.commit()
            flash('Exercise added!', category='success')
    return render_template("workout.html", user=current_user)


@views.route('/delete-workout', methods=['POST'])
def delete_workout():
    # load json of data, gets specific workout from id and if the workout id equals current user id it can be deleted with onclick javascript command
    workout = json.loads(request.data)
    workoutId = workout['workoutId']
    workout = Workout.query.get(workoutId)
    if workout:
        if workout.user_id == current_user.id:
            db.session.delete(workout)
            db.session.commit()

    return jsonify({})


@views.route('/database', methods=['GET', 'POST'])
def database():
    testuser = User.query.all()
    return testuser
