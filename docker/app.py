from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    phone = request.form["phone"]
    course = request.form["course"]
    return f"Thank you, {name}. Registration submitted!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
