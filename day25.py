test = False

def read_input():
    global test
    filename = "inputs/day25-input.txt"
    if test:
        filename = "inputs/day25-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def snafu_digitval(char):
    try:
        val = int(char)
    except ValueError:
        if char == "-":
            return -1
        elif char == "=":
            return -2
        raise
    assert val in range(0, 3)
    return val

def snafu_digitchar(val):
    assert val in range (0, 5)
    if val == 3:
        return "="
    if val == 4:
        return "-"
    return str(val)

def snafu_divmod(num, carry):
    num, rem = divmod(num, 5)
    rem += carry
    carry, rem = divmod(rem, 5)
    if rem == 3:
        carry += 1
    elif rem == 4:
        carry += 1
    return num, rem, carry

def snafu_to_dec(num):
    return sum([snafu_digitval(digit) * (5 ** i) for i, digit in enumerate(reversed(num))])

def dec_to_snafu(num):
    result = ""
    carry = 0
    while num:
        num, rem, carry = snafu_divmod(num, carry)
        result += snafu_digitchar(rem)
    if carry:
        result += str(carry)
    return result[::-1]


def main():
    nums = read_input()
    print(dec_to_snafu(sum([snafu_to_dec(num) for num in nums])))

  
if __name__ == "__main__":
    main()
