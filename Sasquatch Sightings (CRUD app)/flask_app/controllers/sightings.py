from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User

@app.route('/add')
def add_sighting_temp():
    if 'user_id'not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_id(data)
    return render_template('add.html', user = user)

@app.route('/edit/<int:sighting_id>')
def edit_sighting_temp(sighting_id):
    if 'user_id'not in session:
        return redirect('/')
    sighting_data = {
        'id': sighting_id
    }
    sighting = Sighting.get_sighting_by_id(sighting_data)
    data = {
        'id': session['user_id']
    }
    print("A", sighting)
    user = User.get_user_id(data)
    return render_template("edit.html", sighting = sighting, user = user)

@app.route('/sighting/<int:sighting_id>')
def display_sighting(sighting_id):
    if 'user_id'not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    sighting_data = {
        'id': sighting_id
    }
    user = User.get_user_id(user_data)
    sighting = Sighting.get_sighting_with_user(sighting_data)
    print("A", sighting)
    return render_template("show.html", sighting = sighting, user = user)

@app.route('/add', methods=['post'])
def add_sighting():
    if not Sighting.validate_sighting(request.form):
        return redirect('/add')
    data = {
        'location': request.form['location'],
        'date': request.form['date'],
        'amount': request.form['amount'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Sighting.save(data)
    return redirect(f"/home/{session['user_id']}")

@app.route('/edit/<int:sighting_id>', methods=['post'])
def edit_sighting(sighting_id):
    if not Sighting.validate_sighting(request.form):
        return redirect(f"/edit/{sighting_id}")
    data = {
        "id": sighting_id,
        "location": request.form['location'],
        "date": request.form['date'],
        "amount": request.form['amount'],
        "description": request.form['description']
    }
    user_id = session['user_id']
    Sighting.update(data)
    return redirect(f"/home/{user_id}")

@app.route('/delete/<int:sighting_id>')
def sighting_delete(sighting_id):
    data = {
        'id': sighting_id
    }
    Sighting.delete(data)
    user_id = session['user_id']
    return redirect(f"/home/{user_id}")
