from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.save(data)
    return redirect('/')

@app.route('/login', methods=['post'])
def login():
    user = User.get_user_email(request.form)
    if not user:
        flash("Login Attempt failed: Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Login Attempt failed: Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    user_id = session['user_id']
    return redirect(f"/home/{user_id}")

@app.route("/home/<int:user_id>")
def home(user_id):
    if 'user_id'not in session:
        return redirect('/')
    data = {
        'id': user_id
    }
    user = User.get_user_id(data)
    sightings = Sighting.get_all()
    User.get_sighting_from_user(data)
    return render_template("home.html", user = user, sightings = sightings)

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')