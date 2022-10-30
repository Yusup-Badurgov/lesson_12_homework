import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__,
                             template_folder='templates')


@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Картина или текст не были отправлены'

    if picture.filename.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
        logging.info('Загруженный файл не картинка')
        return f"""
        <h2>Не подходящее расширение<br></h2>
        <h1><a href='/' class="link">Назад</a></h1>
"""
    try:
        path_to_picture = save_picture(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Не валидный файл'
    post = {'pic': path_to_picture, 'content': content}

    add_post(post)

    return render_template('post_uploaded.html', path=path_to_picture, content=content)