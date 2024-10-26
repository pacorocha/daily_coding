def twoSum(nums, target):
    nums_dict = {}  # Stores value and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], i]  # Return the indices
        nums_dict[num] = i  # Add the number to the dictionary

    return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9

    print(twoSum(nums, target))
