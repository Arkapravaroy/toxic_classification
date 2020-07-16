from flask import Flask, render_template
from classifier import predict
import matplotlib.pyplot as plt
import time



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results/<data>')
def results(data):
    

    text_to_classify = data
    pred,scores,list_classes = predict(text_to_classify)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(list_classes,scores,color=(0.5,0.5,0.5,1))
    ax.set_ylim([0,1])
    img_name="image"+ str(time.time())+".png"
    file_name="file"+str(time.time())+".txt"
    fig.savefig('static/'+img_name,bbox_inches='tight',pad_inches=0.5)
    with open("static/"+file_name, "w") as output:
        output.write(str(pred))
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify,graph=img_name)
    

if __name__ == '__main__':
    app.run()
