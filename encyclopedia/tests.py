from django.test import TestCase
from django.urls import reverse

from . import views


class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/index.html')

    def test_entry_view_existing_entry(self):
        response = self.client.get(reverse('entry', args=['python']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

    def test_entry_view_nonexistent_entry(self):
        response = self.client.get(reverse('entry', args=['nonexistent_entry']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/error.html')

    def test_search_view_entry_found(self):
        response = self.client.post(reverse('search'), {'q': 'python'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

    def test_search_view_entry_not_found(self):
        response = self.client.post(reverse('search'), {'q': 'nonexistent_entry'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/error.html')

    def test_new_page_view_get(self):
        response = self.client.get(reverse('new_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/new.html')

    def test_new_page_view_post_existing_title(self):
        response = self.client.post(reverse('new_page'), {'title': 'python', 'content': 'Some content'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/error.html')

    def test_new_page_view_post_new_title(self):
        response = self.client.post(reverse('new_page'), {'title': 'new_entry', 'content': 'Some content'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

    def test_edit_view(self):
        response = self.client.post(reverse('edit'), {'entry_title': 'existing_entry'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/edit.html')

    def test_save_edit_view(self):
        response = self.client.post(reverse('save_edit'), {'title': 'existing_entry', 'content': 'Updated content'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

    def test_rand_view(self):
        response = self.client.get(reverse('rand'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encyclopedia/entry.html')

