from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Category, Post

def create_post(title, slug, text, category, author):
    """
    Create post with the followings parameters as it's
    data values
    """
    return Post.objects.create(title=title, slug=slug, text=text,
                               category=category, author=author)


def create_category(name):
    """
    Create category with the name passed
    """
    return Category.objects.create(name=name)


def create_user(username, password):
    """
    Creates a user with username and password
    """
    return User.objects.create_user(username=username, password=password)


class IndexViewTests(TestCase):
    def test_no_posts(self):
        """
        If no posts have been posted, display message
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts available.")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_single_post(self):
        """
        A single post is visible from the index page
        """
        category = create_category("General")
        sample_user = create_user("user1","password")
        create_post("Test Post 1", "test-post-1", "Test Post 1 Text",
                    category, sample_user)

        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<Post: Test Post 1>']
        )

    def test_two_posts(self):
        """
        A two posts are visible from the index page
        """
        category = create_category("General")
        sample_user = create_user("user1","password")
        create_post("Test Post 1", "test-post-1", "Test Post 1 Text",
                    category, sample_user)
        create_post("Test Post 2", "test-post-2", "Test Post 2 Text",
                    category, sample_user)

        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<Post: Test Post 1>','<Post: Test Post 2>']
        )


class PostDetailViewTests(TestCase):
    def test_post(self):
        """
        A single post is visible from the index page
        """
        category = create_category("General")
        sample_user = create_user("user1","password")
        test_post = create_post("Test Post 1", "test-post-1", "Test Post 1 Text",
                                category, sample_user)

        url = reverse('blog:detail', args=(test_post.slug,))
        response = self.client.get(url)
        self.assertContains(response, test_post.text)
