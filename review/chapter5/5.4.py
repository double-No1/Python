def multi(*num):
    if num:
        if not all(num):
            return 0
        else:
            mul = 1
            for i in num:
                mul *= i
            return mul
    else:
        return None
print(multi(1, 2, 3, 4))