def ArraySum(array):
    left, right = 0, len(array)-1
    TotalSum = 0
    while left < right:
        TotalSum += array[left] + array[right]
        left += 1
        right -= 1
    if left == right:
        TotalSum += array[left]

    return TotalSum

print(ArraySum(array=[1,2,3,4,5]))