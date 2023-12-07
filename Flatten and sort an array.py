def flatten_and_sort(array):
    n = len(array)
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    array = sorted([element for sublist in array for element in sublist])
    return array