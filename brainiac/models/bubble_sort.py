import copy


class BubbleSort:

    def sort(self, to_sort, steps=[]):
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                steps.append(copy.copy(to_sort))
                self.sort(to_sort, steps)
        return to_sort

    def verify_sort_steps(self, to_sort):
        steps = []
        self.sort(to_sort, steps)
        return steps
