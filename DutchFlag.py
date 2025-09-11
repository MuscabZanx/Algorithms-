def DutchFlag(array):
    low, mid, high = 0, 0, len(array) -1

    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low +=1
            mid +=1
        elif array[mid] == 1:
            mid +=1
        else:
            array[mid] == 2
            array[mid], array[high] = array[high], array[mid]
            high -=1

    return array

print(DutchFlag([1,2,0,2,1,2,0,2]))
