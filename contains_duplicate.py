# set version
def contains_duplicate(nums):
    new_set = set(nums)
    if len(new_set) == len(nums):
        return False
    else:
        return True

