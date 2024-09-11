

def is_number(string) -> bool:
    no_numbers = 0
    for i in range(len(string)):
        if not(string[i].isdigit()):
            no_numbers += 1
    if no_numbers > 0:
        return False
    else:
        return True

if __name__ == "__main__":
    list = [
        "10",
        "-10",
        "10.1",
        "-10.1",
        "1e5",
    ]

    for el in list:
        print(is_number(el))
