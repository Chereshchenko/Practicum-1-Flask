from pyexpat.errors import messages

from flask import render_template, request, redirect, url_for, flash
from datetime import datetime

from app import app

@app.route("/")
def index():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%A, %B %d, %Y, %H:%M:%S")
    return render_template("index.html", current_time=formatted_time)

@app.route("/about")
def about():
    team_members = [

        {'name': 'Ариша', 'role': 'Разработчик'},

        {'name': 'Ашка', 'role': 'Дизайнер'},

        {'name': 'Крысь', 'role': 'Менеджер проекта'}

    ]
    return render_template('about.html', team_list=team_members)

@app.route("/contact")
def contact():
    contact_info = {
        'name': 'Ариша',
        'address': {
            'street': 'улица 1-го мая',
            'city': 'Смоленск',
            'zip': '43242'
        }
    }
    return render_template('contact.html', info=contact_info)

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        flash("Ваше сообщение было успешно отправлено!", "success")
        return redirect(url_for("contact"))
    else:
        return redirect(url_for("contact"))
