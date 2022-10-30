import json

path_to_json = 'posts.json'
def data_from_json(path_to_json='posts.json'):
    """
    Функция загружает json данные и конвертирует их в py формат
    :param path_to_json: принимает название файла json
    :return: возвращает список словарей (посты)
    """
    with open(path_to_json, 'r', encoding='utf-8') as file:
        return json.load(file)


def post_by_word(subword):
    """
    Функция возвращает список словарей (постов) в котором есть
    указанная подстрока
    :param subword: подсрока введеная в форме
    :return: список словарей (постов) у которых в content'e
    есть введеная подстрока
    """
    all_posts = data_from_json()
    posts = []

    for post in all_posts:
        if subword.lower() in post['content'].lower():
            posts.append(post)

    return posts


def alert_if_not_symbols():
    """
    :return: Уведомление о том что пользователь ничего не ввел
    """
    result = """
            <h2>Вы не указали никаких данных для поиска</h2>
             <h1><a href="/" class="link">Назад</a></h1>
            """
    return result


def add_post(post, path_to_json='posts.json'):
    posts = data_from_json()
    posts.append(post)
    with open(path_to_json, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)