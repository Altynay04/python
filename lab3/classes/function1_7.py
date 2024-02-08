def kas(nums):
    for i in range(0,len(nums)-1):
        if(nums[i] == nums[i+1] == 3):
            print("True")
            return True
    print("False")
    return False

kas([1, 3, 3])
kas([1, 3, 1, 3])
kas([3, 3, 1, 3])
'''
ans
True
False
True
'''