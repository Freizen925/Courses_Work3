import logging
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(filename='logs/api.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')


# Главная страница
@app.route('/')
def index():
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    return render_template('index.html', posts=posts)


# Представление для просмотра одного поста
@app.route('/posts/<int:postid>')
def view_post(postid):
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    post = next((p for p in posts if p['pk'] == postid), None)
    if post:
        with open('comments.json', 'r') as f:
            comments = json.load(f)
        post_comments = [comment for comment in comments if comment['post_id'] == postid]
        return render_template('post.html', post=post, comments=post_comments)
    return "Post not found", 404


# Представление для вывода постов конкретного пользователя
@app.route('/users/<username>')
def user_feed(username):
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    user_posts = [post for post in posts if post['poster_name'] == username]
    if user_posts:
        return render_template('user-feed.html', username=username, posts=user_posts)
    return "User not found", 404


# API для получения полного списка постов
@app.route('/api/posts')
def get_posts():
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    logging.info('API request - get_posts')
    return jsonify(posts)


# API для получения одного поста
@app.route('/api/posts/<int:post_id>')
def get_post(post_id):
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    post = next((p for p in posts if p['pk'] == post_id), None)
    if post:
        logging.info(f'API request - get_post: post_id={post_id}')
        return jsonify(post)
    return "Post not found", 404


# Обработчик ошибки 404 (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return "Page not found", 404


# Обработчик ошибки 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500


if __name__ == '__main__':
    app.run()
