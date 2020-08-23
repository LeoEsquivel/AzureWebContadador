from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def countdown():
    
    launchTime = datetime(2021, 6, 14)
    currentTime = datetime.now()
    diff = launchTime - currentTime
    numberOfMillisenconds = int(diff.total_seconds() * 1000)

    return render_template(
        "countdown.html",
        time = numberOfMillisenconds
    )