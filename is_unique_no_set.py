def is_unique_no_set(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            return False
    return True

print(is_unique_no_set([1,2,3,4,5]))

print(is_unique_no_set([1,2,3,2,4,5]))
