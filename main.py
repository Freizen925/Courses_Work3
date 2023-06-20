from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')


# API для получения данных о постах
@app.route('/posts')
def get_posts():
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    return jsonify(posts)


# API для получения данных о комментариях
@app.route('/comments')
def get_comments():
    with open('comments.json', 'r') as f:
        comments = json.load(f)
    return jsonify(comments)


if __name__ == '__main__':
    app.run()
