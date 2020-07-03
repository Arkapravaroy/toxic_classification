from flask import Flask, render_template
from classifier import predict
import matplotlib as plt
import os


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
    # plt.show()
    os.remove("templates\image2.png")
    #Now save the new image file
    fig.savefig("templates\image2.png")
#     fig.savefig('image2.png')
    
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify)



if __name__ == '__main__':
    app.run()
