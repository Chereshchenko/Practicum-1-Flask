from pyexpat.errors import messages

from flask import render_template, request, redirect, url_for, flash
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

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
