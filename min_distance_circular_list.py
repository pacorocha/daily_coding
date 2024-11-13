def distance(len_my_list, idx_1, idx_2):
    i = (idx_1 - idx_2) % len_my_list
    j = (idx_2 - idx_1) % len_my_list
    return min(i, j)

if __name__ == '__main__':
    len_my_list = 6
    idx_1 = 2
    idx_2 = 5
    print(distance(len_my_list, idx_1, idx_2))
    len_my_list = 100
    idx_1 = 99
    idx_2 = 4
    print(distance(len_my_list, idx_1, idx_2))

