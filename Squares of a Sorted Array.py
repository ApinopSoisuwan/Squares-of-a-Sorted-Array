def sortedSquares(nums):
    for i in range(len(nums)) :
        nums[i] = nums[i] ** 2
    return sorted(nums)


a1 = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
b1 = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]
print(sortedSquares(a1))
print(sortedSquares(b1))