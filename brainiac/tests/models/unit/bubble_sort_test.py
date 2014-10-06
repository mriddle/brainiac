from django.test import TestCase

import brainiac.models.bubble_sort as bubble_sort


class BubbleSortTest(TestCase):

    def setUp(self):
        self.subject = bubble_sort.BubbleSort()
        self.to_sort = [8, 1, 5, 6, 4, 9, 7, 2, 10, 3]

    def test_bubble_sort_result(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = self.subject.sort(self.to_sort)
        self.assertEqual(expected, actual)

    def test_sort_steps(self):
        expected = [
            [1, 8, 5, 6, 4, 9, 7, 2, 10, 3],
            [1, 5, 8, 6, 4, 9, 7, 2, 10, 3],
            [1, 5, 6, 8, 4, 9, 7, 2, 10, 3],
            [1, 5, 6, 4, 8, 9, 7, 2, 10, 3],
            [1, 5, 4, 6, 8, 9, 7, 2, 10, 3],
            [1, 4, 5, 6, 8, 9, 7, 2, 10, 3],
            [1, 4, 5, 6, 8, 7, 9, 2, 10, 3],
            [1, 4, 5, 6, 7, 8, 9, 2, 10, 3],
            [1, 4, 5, 6, 7, 8, 2, 9, 10, 3],
            [1, 4, 5, 6, 7, 2, 8, 9, 10, 3],
            [1, 4, 5, 6, 2, 7, 8, 9, 10, 3],
            [1, 4, 5, 2, 6, 7, 8, 9, 10, 3],
            [1, 4, 2, 5, 6, 7, 8, 9, 10, 3],
            [1, 2, 4, 5, 6, 7, 8, 9, 10, 3],
            [1, 2, 4, 5, 6, 7, 8, 9, 3, 10],
            [1, 2, 4, 5, 6, 7, 8, 3, 9, 10],
            [1, 2, 4, 5, 6, 7, 3, 8, 9, 10],
            [1, 2, 4, 5, 6, 3, 7, 8, 9, 10],
            [1, 2, 4, 5, 3, 6, 7, 8, 9, 10],
            [1, 2, 4, 3, 5, 6, 7, 8, 9, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]
        actual = self.subject.sort_steps(self.to_sort)
        self.assertEqual(expected, actual)

    def test_compare(self):
        unsorted = [4, 1, 3, 2]
        expected = [[1, 4, 3, 2], [1, 3, 4, 2], [1, 3, 2, 4], [1, 2, 3, 4]]
        result = self.subject.compare(unsorted, expected)
        self.assertEqual(True, result)
