import unittest
from utils import (
    get_posts_all,
    get_posts_by_user,
    get_comments_by_post_id,
    search_for_posts,
    get_post_by_pk
)


class UtilsTestCase(unittest.TestCase):
    def test_get_posts_all(self):
        posts = get_posts_all()
        self.assertIsNotNone(posts)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)

    def test_get_posts_by_user_existing_user(self):
        user_name = 'john_doe'
        user_posts = get_posts_by_user(user_name)
        self.assertIsNotNone(user_posts)
        self.assertIsInstance(user_posts, list)
        self.assertGreater(len(user_posts), 0)
        for post in user_posts:
            self.assertEqual(post['poster_name'], user_name)

    def test_get_posts_by_user_non_existing_user(self):
        user_name = 'non_existing_user'
        with self.assertRaises(ValueError):
            get_posts_by_user(user_name)

    def test_get_comments_by_post_id_existing_post(self):
        post_id = 1
        comments = get_comments_by_post_id(post_id)
        self.assertIsNotNone(comments)
        self.assertIsInstance(comments, list)
        self.assertGreater(len(comments), 0)
        for comment in comments:
            self.assertEqual(comment['post_id'], post_id)

    def test_get_comments_by_post_id_non_existing_post(self):
        post_id = 999
        with self.assertRaises(ValueError):
            get_comments_by_post_id(post_id)

    def test_search_for_posts_existing_query(self):
        query = 'skypro'
        matching_posts = search_for_posts(query)
        self.assertIsNotNone(matching_posts)
        self.assertIsInstance(matching_posts, list)
        self.assertGreater(len(matching_posts), 0)
        for post in matching_posts:
            self.assertIn(query.lower(), post['content'].lower())

    def test_search_for_posts_non_existing_query(self):
        query = 'non_existing_query'
        matching_posts = search_for_posts(query)
        self.assertEqual(len(matching_posts), 0)

    def test_get_post_by_pk_existing_post(self):
        pk = 1
        post = get_post_by_pk(pk)
        self.assertIsNotNone(post)
        self.assertIsInstance(post, dict)
        self.assertEqual(post['pk'], pk)

    def test_get_post_by_pk_non_existing_post(self):
        pk = 999
        post = get_post_by_pk(pk)
        self.assertIsNone(post)


if __name__ == '__main__':
    unittest.main()
