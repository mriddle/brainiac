import copy


class BubbleSort:

    def sort(self, to_sort, steps=[]):
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                steps.append(copy.copy(to_sort))
                self.sort(to_sort, steps)
        return to_sort

    def sort_steps(self, to_sort):
        steps = []
        self.sort(to_sort, steps)
        return steps

    def compare(self, to_sort, given):
        actual = self.sort_steps(to_sort)
        return actual == given
