def one_away(s1, s2):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[i+1:] == s2[i+1:]
            return True
    elif len(s1) == len(s2) + 1:
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                return s1[i+1:] == s2[i:]
    elif len(s1) == len(s2) - 1:
        print("passed here")
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[i:] == s2[i+1:]
    else:
        return False

print(one_away("pale", "bale"))
