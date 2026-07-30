from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostDetail, PostList

# Create your tests here.


class TestUrl(TestCase):

    def test_blog_index_resolve(self):
        url = reverse("blog:CBV-index")
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_blog_post_list_resolve(self):
        url = reverse("blog:post-list")
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_blog_post_detail_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetail)
