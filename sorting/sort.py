def BubbleSort(similarity):
    n = len(similarity)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if similarity[j] > similarity[j + 1]:
                similarity[j], similarity[j +
                                          1] = similarity[j + 1], similarity[j]


def InsertionSort(similarity):
    for i in range(1, len(similarity)):
        key = similarity[i]
        j = i - 1
        while j >= 0 and key < similarity[j]:
            similarity[j + 1] = similarity[j]
            j -= 1
        similarity[j + 1] = key


def selectionSort(similarity):
    size = len(similarity)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if similarity[i] < similarity[min_idx]:
                min_idx = i
        similarity[step], similarity[min_idx] = (
            similarity[min_idx], similarity[step])
