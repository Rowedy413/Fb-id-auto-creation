from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return []

def save_user(user):
    users = load_users()
    users.append(user)
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        password = request.form.get("password")

        if name and phone and password:
            save_user({"name": name, "phone": phone, "password": password})
            return "<h3>✅ User Registered Successfully!</h3><a href='/'>Back</a>"

        return "<h3>❌ All fields required!</h3><a href='/'>Back</a>"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
