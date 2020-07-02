from flask import Flask, render_template
import matplotlib.pyplot as plt
%matplotlib inline
from classifier import predict


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results/<data>')
def results(data):
    text_to_classify = data
    pred,scores,classes = predict(text_to_classify)
    

#     x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
#     energy = [5, 6, 15, 22, 24, 8]
    

    x_pos = [i for i, _ in enumerate(classes)]
    fig, ax = plt.subplots()
    plt.bar(x_pos, scores, color='red')
    plt.xlabel("categories")
    plt.ylabel("Toxicity")
    plt.title("Toxicity measurements")
#     fig.savefig('my_plot.png')
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify)


if __name__ == '__main__':
    app.run()
