from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/chats")
def chats():
    return render_template("chats.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)
