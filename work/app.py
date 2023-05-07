from flask import Flask,render_template, request
from model import predict_sentiment, find_closest_value


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        quote = request.form['name']
        result = predict_sentiment(quote)
        label = result[0]['label']
        score = result[0]['score']
        closestValue = find_closest_value(result[0]['label'], result[0]['score'])
        return render_template('predict.html',quote=quote, label=label, score=score, closestValue = closestValue)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

