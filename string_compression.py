def string_compression(string):
    if not string:
        return ''
    counter = 1
    result = ''
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            counter += 1
        else:
            result += string[i] + str(counter)
            counter = 1
    if len(result) < len(string):
        return result + string[-1] + str(counter)
    else:
        return string

print(string_compression('AAAABBBBCCCCCDDEEEE'))

print(string_compression('AAABCCDDEFF'))
