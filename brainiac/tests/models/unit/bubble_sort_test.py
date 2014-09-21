from django.test import TestCase

import brainiac.models.bubble_sort as bubble_sort


class BubbleSortTest(TestCase):

    def setUp(self):
        self.context = bubble_sort.BubbleSort()

    def test_hello_world(self):
        self.assertEqual("Hell World", self.context.helloWorld())
