from flask import Flask, render_template, request
import ml
import pandas
app = Flask(__name__, template_folder='template')


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/page", methods=['POST'])
def submit():
    if request.method == "POST":
        name = request.form["movies"]
        predict = ml.recommend(name)
        ans = predict
    return render_template("page.html", movie_names=ans)


if __name__ == "__main__":
    app.run(debug=True)
