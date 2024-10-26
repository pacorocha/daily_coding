def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    prod = 1
    for i in range(n):
        result[i] = prod
        prod = prod * nums[i]

    prod = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * prod
        prod = prod * nums[i]

    return result

if __name__ == '__main__':
    nums = [1,2,3,4]

    print(productExceptSelf(nums))
