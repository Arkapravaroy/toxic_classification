from flask import Flask, render_template
from classifier import predict
import matplotlib as plt


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results/<data>')
def results(data):
    text_to_classify = data
    pred,scores,classes = predict(text_to_classify)
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify)


if __name__ == '__main__':
    app.run()
