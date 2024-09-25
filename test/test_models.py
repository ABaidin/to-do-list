from django.test import TestCase
from django.utils import timezone

from tasks.models import Task, Tag


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Shop")
        self.assertEqual(tag.name, "Shop")
        self.assertEqual(str(tag), "Shop")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Work")

    def test_task_creation(self):
        task = Task.objects.create(
            content="Complete project",
            deadline=timezone.now() + timezone.timedelta(days=1),
        )
        task.tags.add(self.tag)
        self.assertEqual(task.content, "Complete project")
        self.assertEqual(task.is_done, False)
        self.assertEqual(str(task), "Complete project")
        self.assertIn(self.tag, task.tags.all())

    def test_task_done_status(self):
        task = Task.objects.create(content="Finish project")
        self.assertFalse(task.is_done)
        task.is_done = True
        task.save()
        self.assertTrue(task.is_done)
