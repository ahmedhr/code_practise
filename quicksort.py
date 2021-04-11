a = [6, 4, 2, 3]


def swap(c, d, array):
    temp = array[c]
    array[c] = array[d]
    array[d] = temp


def quicksort(arr, left, right):
    p = a[right]
    for j in range(left, right):
        if arr[j] <= p:
            swap(left, j, arr)
            left += 1
    swap(left, right, arr)
    return left


def sort(input_arr, left, right):
    if left < right:
        pivot_pos = quicksort(input_arr, left, right)

        sort(input_arr, left, pivot_pos - 1)
        sort(input_arr, pivot_pos + 1, right)
    pass

sort(a, 0, len(a) - 1)
