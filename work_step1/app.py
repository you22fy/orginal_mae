from flask import Flask,render_template, request
from model import <ここに回答を記入>


app = <ここに回答を記入>

@app.route("/")
def index():
    return <ここに回答を記入>

@app.route("/predict", methods = <ここに回答を記入>)
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        quote = request.form['name']
        result = predict_sentiment(quote)
        label = result[0]['label']
        score = result[0]['score']
        return render_template('predict.html',quote=<ここに回答を記入>, label=<ここに回答を記入>, score=<ここに回答を記入>)


if __name__ == "__main__":
    app.run(debug=True)

