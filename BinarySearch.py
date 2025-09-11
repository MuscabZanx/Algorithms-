def BinarySearch(array, target):

    left, right = 0, len(array)-1

    while left <= right:
        Mid = (left + right) // 2

        if array[Mid] == target:
            return Mid
        elif array[Mid] < target:
            left = Mid + 1
        else:
            right = Mid -1

    return -1

print(BinarySearch(array=[-2, 0, 3, 5, 6, 9, 11], target= 2))
