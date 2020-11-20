import os

# Configure application
app = Flask(__name__)

@app.route("/")
return render_template("index.html")

@app.route("/game")
return render_template("buy.html")

@app.route("/hobbies")
return render_template("history.html")

@app.route("/projects")
return render_template("projects.html")
