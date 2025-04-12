"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, url_for, request
from PlantDiseaseClassifier import app

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
        title='Test Pictures',
        year=datetime.now().year,
        message='Your application test images page.'
    )

@app.route('/classify', methods=['POST'])
def classify():
    test_image = request.form['selected_image']
    return render_template(
        'classified.html',
        title='Classfied',
        year=datetime.now().year,
        message='Your plant is: ',
        test_image=test_image
    )