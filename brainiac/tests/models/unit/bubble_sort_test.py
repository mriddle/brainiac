from django.test import TestCase

import brainiac.models.bubble_sort as bubble_sort


class BubbleSortTest(TestCase):

    def setUp(self):
        self.context = bubble_sort.BubbleSort()

    def test_bubble_sort_result(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = self.context.sort([8, 1, 5, 6, 4, 9, 7, 2, 10, 3])
        self.assertEqual(expected, actual)
