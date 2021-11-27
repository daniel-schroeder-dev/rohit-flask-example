from flask import Flask, render_template, redirect, url_for, request, session
from login import validate_user
from user import get_user
from passwords import update_column

app = Flask(__name__)
app.secret_key = "$IxgT$i@V8t+<M<$p2Fw<>#KxoVZx6"

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("id"):
        return redirect(url_for("home"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = validate_user(username, password)
        
        if user:
            session["id"] = user["id"]
            return redirect(url_for("update_passwords"))
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["id"] = None
    return redirect(url_for("login"))



@app.route("/update_passwords", methods=["GET", "POST"])
def update_passwords():
    if not session.get("id"):
        return redirect(url_for("login"))

    user = get_user(session.get("id"))
    if request.method == "POST":
        column_to_update = request.form["column_to_update"]
        new_column_value = request.form["new_column_value"]
        update_column(column_to_update, user["username"], new_column_value)
        return redirect(url_for("update_passwords"))

    return render_template("update_passwords.html", user=dict(user))
