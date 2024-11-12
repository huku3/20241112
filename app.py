from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

count = 0


@app.route("/")
def index():
    global count
    return render_template("index.html", count=count)


@app.route("/increment", methods=["POST"])
def increment():
    global count
    count += 1  # count = count + 1
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
