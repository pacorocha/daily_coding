def is_unique_no_set(lst):
    for i in range(len(lst)):
       for j in range(i+1, len(lst)):
           if lst[i] == lst[j]:
                return False
    return True

print(is_unique_no_set([1,2,3,4,5]))

print(is_unique_no_set([1,2,3,2,4,5]))
