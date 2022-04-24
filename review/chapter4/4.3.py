#求最大公约数和最小公倍数
n1, n2 = eval(input("请输入两个整数:"))
m1 = n1 * n2
if n1 < n2:
    n1, n2 = n2, n1
r = n1 % n2
while(r):
    n1 = n2
    n2 = r
    r = n1 % n2
m2 = m1 / n2
print("这两个数的最大公约数是{}，最小公倍数是{}".format(n2,m2))

