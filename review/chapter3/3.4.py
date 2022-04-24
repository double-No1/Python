n = input("请输入一位五位数:")
n2 = n[::-1]
if eval(n) == eval(n2):
    print("该数是回文数")
else:
    print("该数不是回文数")
