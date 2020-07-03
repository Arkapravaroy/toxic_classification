from flask import Flask, render_template
from classifier import predict
import matplotlib.pyplot as plt


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results/<data>')
def results(data):
    text_to_classify = data
    pred,scores,classes = predict(text_to_classify)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
#     langs = ['C', 'C++', 'Java', 'Python', 'PHP']
#     students = [23,17,35,29,12]
    ax.bar(classes,scores)
    img_name="image.png"
    fig.savefig('static/' + img_name)
    
#     plt.show()

    
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify, graph=img_name)



if __name__ == '__main__':
    app.run()
