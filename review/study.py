def func(*ls):
    sum = 0
    for i in ls:
        sum += i
    return ls, sum

ls = [1, 2, 3, 4, 5]
retls, retsum = func(*ls[:4])
print(retls, retsum)