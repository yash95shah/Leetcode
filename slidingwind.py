
def maxslidingWindow(nums, k):
    initPtr = 0
    finalPtr = k
    resultantArray =  list()
    while finalPtr <= len(nums):
        max_temp = max(nums[initPtr:finalPtr])
        resultantArray.append(max_temp)
        initPtr += 1
        finalPtr +=1
    return resultantArray


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print (maxslidingWindow(nums , k))

