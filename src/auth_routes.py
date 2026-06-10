from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, UserNote 
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_exists = User.query.filter((User.username == username) | (User.email == email)).first()
        if user_exists:
            return "El usuario o correo electrónico ya está registrado.", 400
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('auth.dashboard'))
        else:
            return "Credenciales incorrectas. Inténtalo de nuevo.", 401
    return render_template('login.html')


@auth_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_note = UserNote(title=title, content=content, user_id=session['user_id'])
        db.session.add(new_note)
        db.session.commit()
        
        return redirect(url_for('auth.dashboard'))
     
    my_notes = UserNote.query.filter_by(user_id=session['user_id']).order_by(UserNote.created_at.desc()).all()
    return render_template('dashboard.html', username=session['username'], notes=my_notes)


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))