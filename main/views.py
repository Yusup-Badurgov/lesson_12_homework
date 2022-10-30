from flask import Blueprint, render_template, request

from functions import post_by_word, alert_if_not_symbols

main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates')


@main_blueprint.route("/")
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_tag():
    word = request.args.get('s')
    posts = post_by_word(word)

    if not word:
        return alert_if_not_symbols()


    return render_template('post_list.html', posts=posts, word=word)
