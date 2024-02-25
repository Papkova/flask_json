from app import app
from flask import render_template
from datetime import timedelta, date


@app.route("/")
def main():
    mock = {}
    for item in range(5):
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        mock[date_str] = ["event 1", "event 2"]
    return render_template("main.html")
