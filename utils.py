import json


def get_posts_all():
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    return posts


def get_posts_by_user(user_name):
    posts = get_posts_all()
    user_posts = [post for post in posts if post['poster_name'] == user_name]
    if not user_posts:
        raise ValueError(f"No posts found for user: {user_name}")
    return user_posts


def get_comments_by_post_id(post_id):
    with open('comments.json', 'r') as f:
        comments = json.load(f)
    post_comments = [comment for comment in comments if comment['post_id'] == post_id]
    if not post_comments:
        raise ValueError(f"No comments found for post ID: {post_id}")
    return post_comments


def search_for_posts(query):
    posts = get_posts_all()
    matching_posts = [post for post in posts if query.lower() in post['content'].lower()]
    return matching_posts


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
    return None
