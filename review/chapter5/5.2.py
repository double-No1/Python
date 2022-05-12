# def isOdd(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
# n = int(input ("请输入一个整数:"))
# a = isOdd(n)
# print(a)

def isOdd(num):
    try:
        if type(num) == type(0.):
            raise TypeError
        if num % 2 == 0:
            return False
        else:
            return True
    except TypeError:
        print('这不是一个有效的整数！')
print(isOdd(4))
print(isOdd(3))
print(isOdd(-1))
print(isOdd('str'))
print(isOdd(3.))