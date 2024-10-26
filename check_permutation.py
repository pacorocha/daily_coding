def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char not in str2:
            return False
    return True

print(check_permutation("chair", "archi"))

print(check_permutation("rich", "door"))
