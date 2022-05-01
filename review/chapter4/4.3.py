# #求最大公约数和最小公倍数
# n1, n2 = eval(input("请输入两个整数:"))
# m1 = n1 * n2
# if n1 < n2:
#     n1, n2 = n2, n1
# r = n1 % n2
# while(r):
#     n1 = n2
#     n2 = r
#     r = n1 % n2
# m2 = m1 / n2
# print("这两个数的最大公约数是{}，最小公倍数是{}".format(n2, m2))


#最大公约数与最小公倍数
a, b = eval(input('请输入两个需要求解的数(用逗号隔开)：'))
c = max(a, b)
d = min(a, b)
while c % d != 0:
        e = c % d
        c = d
        d = e #辗转相除法
f = (a*b)/e
print('最大公约数是{},最小公倍数是{}'.format(e, int(f)))
