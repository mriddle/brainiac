class BubbleSort:

    def sort(self, to_sort):
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                self.sort(to_sort)
        return to_sort

