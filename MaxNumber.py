
def MaxNumber(array):
    left, right = 0, len(array)-1
    MaxNum = 0
    for num in array:
        if MaxNum < num:
            MaxNum = num
    # while left <= right:
    #     if MaxNum < array[left]:
    #         MaxNum = array[left]
    #     elif MaxNum < array[right]:
    #         MaxNum = array[right]

    #     left += 1
    #     right -= 1

    return MaxNum

print(MaxNumber(array=[4,3,1,5,4,3,2,7,5,9,2]))