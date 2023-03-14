def selection_sort(arr: list) -> list:

    length = len(arr)

    for i in range(length):
        min_index = i

        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [0, 1, 2, 3, 4, 5]
print(len(arr))
