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
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_axes([0,0,1,1])
    ax.bar(classes,scores)
    plt.show()
    image=fig.savefig()
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify, user_image=image)


if __name__ == '__main__':
    app.run()
