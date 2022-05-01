def isOdd(n):
    if n % 2 == 1:
        return True
    else:
        return False
n = int(input ("请输入一个整数:"))
a = isOdd(n)
print(a)