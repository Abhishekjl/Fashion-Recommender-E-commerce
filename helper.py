import pickle
import os
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
import numpy as np
from numpy.linalg import norm
images_name = pickle.load(open('static/files_name.pkl','rb'))
model = load_model('static/model.h5')


features_list = np.array(pickle.load(open('static\embeddings.pkl', 'rb')))
def recommend(imagepath):
    img = image.load_img(imagepath, target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis = 0)
    preprocessed_image = preprocess_input(expanded_img_array)
    result  = model.predict(preprocessed_image).flatten()
    normalized_result = result/norm(result)
    neighbours = NearestNeighbors(n_neighbors=6,algorithm='brute',metric = 'euclidean')
    neighbours.fit(features_list)
    distances, indices = neighbours.kneighbors([normalized_result])
    
    return indices
    # for file in indices[0]:
    #     file_path = os.path.join('images/',(images_name[file]))
    #     img = cv2.resize(cv2.imread(file_path),(300,300))

    #     cv2.imshow('window',img)
    #     cv2.waitKey(0)

