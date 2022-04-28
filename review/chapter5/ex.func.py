# def vfunc(a, *b):
#     print(type(b))
#     for n in b:
#         a += n
#     return a
# print(vfunc(1, 2, 3, 4, 5))


# n = 1
# def func(a, b):
#     global n
#     n = b
#     return a * b
# s = func("knock~", 2)
# print(s, n)


# ls = []
# def func(a, b):
#     ls.append(b)
#     return a * b
# s = func("knock~", 2)
# print(s, ls)


ls = []
def func(a, b):
    ls = []
    ls.append(b)
    return a * b
s = func("knock~", 3)
print(s, ls)