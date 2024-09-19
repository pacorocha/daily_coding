def superDigit(n, k):
    n_int = [int(char) for char in n] * k
    super_digit = sum(n_int)
    if super_digit >= 10:
        return superDigit(str(super_digit), 1)
    return super_digit

if __name__ == "__main__":
    n="9875"
    k = 4
    print(superDigit(n, k))
