def TwoSum(array):
    left, right = 0, len(array)-1
    TargetSum = 4
    while left < right:
        TwoSum = array[left] + array[right]
        # right -=1
        # left +=1
        if TwoSum == TargetSum:
            print(left, right)
            break
        elif TwoSum > TargetSum:
            right -=1
        elif TwoSum < TargetSum:
            left +=1
        
    return 

print(TwoSum(array=[1,2,3,4,5,6,7]))
        