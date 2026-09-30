from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Task Manager is running!"

@app.route("/tasks")
def tasks():
    return [
        {"id": 1, "title": "Learn Linux"},
        {"id": 2, "title": "Learn Docker"},
        {"id": 3, "title": "Build Project"}
    ]

app.run()