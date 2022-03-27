from flask import Blueprint, request, render_template, send_from_directory
from functions import *
loader = Blueprint('loader', __name__, template_folder='templates')


@loader.route('/post/')
def post_form():
    return render_template('post_form.html')


@loader.route('/post/load/', methods=['POST'])
def post_uploaded():
    if request.method == "POST":
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        image = request.files.get('picture')
        text = request.form.get('content')
        filename = image.filename
        extension = filename.split('.')[-1]
        if extension in ALLOWED_EXTENSIONS and filename and text and add_post(filename, text):
            image.save(f'static/uploads/images/{filename}')
            return render_template('post_uploaded.html', path=f'uploads/images/{filename}', text=text)
        else:
            return "Post was not added"


@loader.route('/search/static/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('static/uploads', path)
