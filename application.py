from flask import Flask, render_template, request
from sorting import ml
import pandas

app = Flask(__name__, template_folder='template')


@app.route("/")
def hello():
    return render_template('bootstrap.html')


@app.route("/page", methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        name = request.form["movies"]
        name = name.title()
        predict = try_ml.get_recommendations(name)
        ans = []
        for i in range(len(predict)):
            ans.append(predict.iloc[i][0])
    return render_template("page.html", movie_names=ans, search_name=name)


if __name__ == "__main__":
    app.run(debug=True)
