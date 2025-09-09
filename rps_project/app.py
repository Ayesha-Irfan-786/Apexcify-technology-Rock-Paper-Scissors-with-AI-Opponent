from flask import Flask, render_template, request
import random
import webbrowser
import threading

app = Flask(__name__)

CHOICES = ['rock', 'paper', 'scissors']
WIN_MAP = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def decide_winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif WIN_MAP[user] == comp:
        return "You win!"
    else:
        return "Computer wins!"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    comp_choice = ""
    user_choice = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        comp_choice = random.choice(CHOICES)
        result = decide_winner(user_choice, comp_choice)

    return render_template("index.html", result=result, comp=comp_choice, user=user_choice)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
