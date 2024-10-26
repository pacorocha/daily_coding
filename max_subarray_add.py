def max_subarray(nums):
    res = nums[0]
    maxEnding = nums[0]

    for i in range(1, len(nums)):

        # Find the maximum sum ending at index i by either extending
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + nums[i], nums[i])

        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)

    return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print(max_subarray(nums))

    print(nums[2])
    print(nums[4])
    print(nums[2:4])
    print(sum([-3, 4, -1]))

