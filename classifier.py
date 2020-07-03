import os
import pickle
import numpy as np
from keras import backend as K
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt 


max_features, max_len = 20000, 100


def predict(text):
    K.clear_session()
    data_dir = 'resources/'

    text = np.array(text).reshape(1, )

    with open('resources/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    list_tokenized_test = tokenizer.texts_to_sequences(text)
    x_test = pad_sequences(list_tokenized_test, maxlen=max_len)  # Restrict each row in df to max_len = 100 words

    with open(os.path.join(data_dir, 'model.json'), 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)

    model.load_weights(os.path.join(data_dir, 'weights.h5'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    y_test = model.predict([x_test], verbose=1)
    scores = [i for i in y_test[0]]

#     if len(np.nonzero(y_test > 0.5)[0]) == 0:
#         predictions = ['Non-Toxic']
#     else:
    list_classes = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
#         predictions = [list_classes[idx] for idx in np.nonzero(y_test > 0.5)[1]]
    predictions=[]
    for i in range(len(scores)):
        element= list_classes[i]+':'+str(scores[i])
        predictions.append(element)
#         =[list(x) for x in zip(list_classes, scores)]
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
#     langs = ['C', 'C++', 'Java', 'Python', 'PHP']
#     students = [23,17,35,29,12]
    ax.bar(classes,scores)
#     # plt.show()
#     os.remove("templates\image2.png")
#     #Now save the new image file
#     fig.savefig("templates\image2.png")
    K.clear_session()
    return predictions,scores,list_classes
