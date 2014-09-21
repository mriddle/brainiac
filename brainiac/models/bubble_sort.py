class BubbleSort:

    def sort(self, toSort):
        for i in range(len(toSort) - 1):
            if toSort[i] > toSort[i + 1]:
                toSort[i], toSort[i + 1] = toSort[i + 1], toSort[i]
                self.sort(toSort)
        return toSort
