def multi(*num):
    if num:
        if 0 in num:
            return 0
        else:
            mul = 1
            for i in num:
                mul *= i
            return mul
    else:
        return None

print(multi(2, 4, 4, 1))