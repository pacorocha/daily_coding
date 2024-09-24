def superDigit(n, k):
    digit_sum = sum(int(char) for char in n)

    total_sum = digit_sum * k

    def compute_super_digit(x):
        if x < 10:
            return x
        else:
            return compute_super_digit(sum(int(char) for char in str(x)))

    return compute_super_digit(total_sum)

if __name__ == "__main__":
    n="9875"
    k = 4
    print(superDigit(n, k))
