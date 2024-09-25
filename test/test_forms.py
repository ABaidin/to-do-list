from django import forms
from django.test import TestCase

from tasks.forms import TaskForm, TagForm
from tasks.models import Tag


class TagFormTest(TestCase):
    def test_tag_form_valid(self):
        form = TagForm(data={"name": "Shopping"})
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid(self):
        form = TagForm(data={"name": ""})
        self.assertFalse(form.is_valid())


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Work")

    def test_task_form_valid(self):
        form = TaskForm(
            data={
                "content": "Finish the report",
                "is_done": False,
                "tags": [self.tag.id],
            }
        )
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = TaskForm(data={"content": ""})
        self.assertFalse(form.is_valid())

    def test_task_tag_uses_widget(self):
        form = TaskForm(data={"tags": [self.tag.id]})
        self.assertIsInstance(form.fields['tags'].widget, forms.CheckboxSelectMultiple)
