from flask import render_template
from flask.ext.login import login_required, current_user
from app import app

@app.route('/')
def index():
    return render_template("/home/index.html")    

@app.route('/home')
def home():
    return render_template("/home/index.html")    