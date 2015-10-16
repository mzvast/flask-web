# -*- coding: utf-8 -*- 
from flask import render_template,redirect, url_for,request,flash,session,g
# from flask.ext.login import login_required, current_user
from app import app
from app.forms import RegistrationForm
from app.models import User
from app import db
from app.dbconnect import connection
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc
from functools import wraps

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html",error='page_not_found')
    
@app.errorhandler(405)
def method_not_found(e):
    return render_template("error.html",error='method_not_found')

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'is_admin' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def index():
    # flash("flash test!!!!")
    return render_template("/home/index.html")    

@app.route('/login/', methods=["GET", "POST"])
def login():
    error = None
    try:
        c, conn = connection()
        flash("db ok")
        if request.method == "POST":
            flash("method is POST")
            data = c.execute("SELECT * FROM users WHERE username = (%s)",
                             [thwart(request.form['username'])])
            data = c.fetchone()[2]
            name = request.form['username']
            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']
                flash("You are now logged in")
                if name == 'ubuntu':
                    session['is_admin']= True
                    flash("welcome Admin!")
                else:
                    flash("Welcome Standard User")
                return redirect("/")

            else:
                error = "Invalid credentials, try again."
        gc.collect()

        return render_template("register/login.html", error=error)
        
    except Exception as e:
        #flash(e)
        error = "Invalid credentials, try again."
        return render_template('register/login.html',error = error)

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect("/")
    
@app.route('/register/', methods=["GET", "POST"])
def register():
    try:
        form = RegistrationForm(request.form)
        
        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c,conn = connection()
            
            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          [(thwart(username))])
            if int(x) > 0 :
                flash("That username is already taken, please choose another")
                return render_template('register/register.html', form=form)
            else:
                 c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (thwart(username), thwart(password), \
                          thwart(email), thwart("/introduction-to-python-programming/")))
                 conn.commit()
                 flash("Thanks for registering!")
                 c.close()
                 conn.close()
                 gc.collect()
                 session['logged_in'] = True
                 session['username'] = username

                 return redirect("/")

        return render_template("register/register.html", form=form)
                
    except Exception as e:
        return(str(e))
    # form = RegisterForm()
    # if request.method == 'POST' and form.validate():
        
    #     print form.username.data,form.email.data,form.password.data
        
    #     print 'success'

    #     return render_template('register/register_complete.html')
    # return render_template('register/register.html', form=form)