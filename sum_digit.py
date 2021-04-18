def digital_root(n):
    digit = 0
    for i in str(n):
        digit += int(i)
    return digit if digit < 10 else digital_root(digit)
    # return n if n < 10 else digital_root(sum(map(int,str(n))))


print(digital_root(999999999999))
