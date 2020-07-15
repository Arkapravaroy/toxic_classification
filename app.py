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
    text=text_to_classify
    if len(text_to_classif)!=0:
        pred,scores,classes = predict(text_to_classify)
    
    

        fig = plt.figure()
    #     fig.ylim(0.1)
        ax = fig.add_axes([0,0,1,1])
    #     langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    #     students = [23,17,35,29,12]
        ax.bar(classes,scores,color=(0.5,0.5,0.5,1))
        ax.set_ylim([0,1])
    #     ax.ylim(0,1)
    #     ax.set_facecolor('black')
    #     ax.patch.set_facecolor('white')

        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')
        img_name="image"+ str(time.time())+".png"
        fig.savefig('static/' +img_name,bbox_inches='tight',pad_inches=0.5)
     else:
        pred=['error','error','error','error','error','error']
        fig = plt.figure()
    #     fig.ylim(0.1)
        ax = fig.add_axes([0,0,1,1])
    #     langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    #     students = [23,17,35,29,12]
    #         ax.bar(classes,scores,color=(0.5,0.5,0.5,1))
        ax.set_ylim([0,1])
    #     ax.ylim(0,1)
    #     ax.set_facecolor('black')
    #     ax.patch.set_facecolor('white')

        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')
        img_name="image"+ str(time.time())+".png"
        fig.savefig('static/' +img_name,bbox_inches='tight',pad_inches=0.5)
        text='ERROR: NO INPUT FOUND'


#     plt.show()


      return render_template('results.html', pred=pred, text_to_classify=text, graph=img_name)

    



if __name__ == '__main__':
    app.run()
