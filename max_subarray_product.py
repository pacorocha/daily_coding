def max_subarray(nums):
    res = nums[0]
    max_end = nums[0]  # This keeps track of the maximum product ending here
    min_end = nums[0]  # This keeps track of the minimum product ending here

    for i in range(1, len(nums)):
        num = nums[i]

        # Temporarily store max_end since it will change
        tmp_max = max_end

        # Update max_end and min_end for the current number
        max_end = max(num, max_end * num, min_end * num)
        min_end = min(num, tmp_max * num, min_end * num)

        # Update the result with the current maximum product
        res = max(res, max_end)

    return res

if __name__ == "__main__":
    nums = [-4,-3,-2]
    print(max_subarray(nums))
