import logging

from flask import Blueprint, render_template, request

from functions import find_post


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index_page():
    return render_template('index.html')


@main.route('/search/', methods=['GET'])
def posts_page():
    request_word = request.args.get('s')
    logging.info(f"Search - {request_word}")
    return render_template('posts.html', posts=find_post(request_word), word=request_word)


