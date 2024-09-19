def is_number(string) -> bool:
    if len(string) == 1:
        return string.isdigit()
    for i in range(len(string)):
        c = string[i]
        if c != "-" and c != "." and c != "e" and not(c.isdigit()):
            return False
    if string.count("e") == 1:
        return True
    if string.count("-") == 1 and string[0] != "-":
        return False
    return True

# TODO: ok for example proposed, a deeper more efficient function will require more time

if __name__ == "__main__":
    list = [
        "10",
        "-10",
        "10.1",
        "-10.1",
        "1e5",
        "a",
        "3-12",
        "x 1",
        "a -2",
        "-",
    ]

    for el in list:
        print(el, is_number(el))

    s = "string"
    for i in range(len(s)):
        print(s[:i] + s[i+1:])
