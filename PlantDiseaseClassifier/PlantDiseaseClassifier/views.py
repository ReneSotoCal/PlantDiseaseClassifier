"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, url_for, request
from PlantDiseaseClassifier import app
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        test_images='test_images',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/test_images')
def test_images():
    """Renders the test_images page."""
    image_folder = os.path.join(app.root_path, 'static', 'test_images')
    images = os.listdir(image_folder)
    images = [os.path.join('static', 'test_images', image) 
              for image in images if image.lower().endswith(('png', 'jpg', 'jpeg'))]
    return render_template(
        'test_images.html',
        images=images,
        title='Test Images',
        year=datetime.now().year,
        message='Pick an Image to Classify:'
    )

@app.route('/classify', methods=['POST'])
def classify():
    img_size = (224,224)
    test_image_path = request.form['selected_image']
    image_path = os.path.join(app.root_path, test_image_path)
    parent_dir = os.path.dirname(app.root_path)
    model_path = os.path.join(app.root_path,'static' , 'model', 'plant_model_test_conv_output_3.keras')
    image_folder = os.path.join(app.root_path, 'static', 'test_images')
    class_labels = [num for num in range(0, 37)]
  
    img = load_img(image_path, target_size=img_size)
    img_array = img_to_array(img)
    normalized_img = img_array/255.0

    model = load_model(model_path)
    predictions = model.predict(np.expand_dims(normalized_img, axis=0))
    predicted_index = np.argmax(predictions[0])
    predicted_label = class_labels[predicted_index]

   # prediction = model.predict(normalized_img.flow_from_directory())
    return render_template(
        'classified.html',
        title='Classfied',
        prediction=predicted_label,
        year=datetime.now().year,
        message=f'Your plant is: {predicted_label}',
        test_image=test_image_path
    )

def get_predicted_label(index):
    match index:
        case i if 0 <= i <= 3: 
            label = 'Apple Cedar Rust'
    return list(gen.class_indices.keys())

def get_class_label():
    labels = [ ]
    return labels