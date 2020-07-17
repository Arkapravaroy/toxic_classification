from flask import Flask, render_template
from classifier import predict
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import datetime
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
    file_name="multipage_rap"+str(time.time())+".pdf"
    fig.savefig('static/'+img_name,bbox_inches='tight',pad_inches=0.5)
    
    statement='Entered comment:'+' '+ text_to_classify
    text=statement+'\n'+'analysis:'+' '
    for i in pred:
      text=text+'\n '+i
    

    with PdfPages(file_name) as pdf:
        firstPage = plt.figure(figsize=(11.69,8.27))
        firstPage.clf()
        txt = str(text)
        firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=24, ha="center")
        pdf.savefig()
        plt.close()

#         fig = plt.figure(figsize=(11.69,8.27))
#         ax = fig.add_axes([0,0,1,1])
#         ax.bar(list_classes,scores,color=(0.5,0.5,0.5,1))
#         # ax.grid(True)
#         ax.set_ylim([0,1])
#         # plt.show()
#         # mpld3.show(fig)
#         # ax.patch.set_facecolor('lemonchiffon')
#         ax.tick_params(axis='x', colors='red')
#         ax.tick_params(axis='y', colors='red')
#         # ax.title('Title')
#         # txt = 'this is an example'
#         # ax.text(0.05,0.95,txt, transform=fig.transFigure, size=24)
#         pdf.savefig(bbox_inches='tight',pad_inches=0.5)
#         plt.close()
    
    return render_template('results.html', pred=pred, text_to_classify=text_to_classify,graph=img_name)
    

if __name__ == '__main__':
    app.run()
