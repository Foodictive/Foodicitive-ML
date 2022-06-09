import os
import tensorflow as tf
import numpy as np
import config as cfg
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array


print('Loading Model..')
path = os.path.join(cfg.DIR, cfg.MODEL_FILE)
model = tf.keras.models.load_model(path)
model.trainable = False

def allow_file(filen):
    """
    For checking type`filename` is of type image with 'png', 'jpg', or 'jpeg' extensions
    """
    allowed = {'png', 'jpg', 'jpeg', 'jfif'}
    return ('.' in filen) and (filen.rsplit('.', 1)[1].lower() in allowed)

def prepare_img(img_path):
    """
    Loads image from  `img_path'
    """
    image = load_img(img_path, target_size=(cfg.SIZE, cfg.SIZE))
    return np.expand_dims(preprocess_input(img_to_array(image)), axis=0)


def make_prediction(filen):
    """
    Predicts what food `filename` file
    """
    print('Filename is ', filen)
    full_path = os.path.join(cfg.OUTPUT, filen)
    test_data = prepare_img(full_path)
    predictions = model.predict(test_data)
    print(predictions)
    return cfg.LABELS[np.argmax(predictions[0])]