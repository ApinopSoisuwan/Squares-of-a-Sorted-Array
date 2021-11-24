def sortedSquares(nums):
    l,n = 0,len(nums) - 1
    p = []
    while l <= n :
        if nums[l] ** 2 >= nums[n] ** 2:
            p.append(nums[l]** 2)
            l += 1
        else:
            p.append(nums[n] ** 2)
            n -= 1
    return sorted(p)

a1 = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
b1 = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]
print(sortedSquares(a1))
print(sortedSquares(b1))