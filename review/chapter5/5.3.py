def isNum(n):

    try:
        s = type(eval(n))
        if s == int or s == float or s == complex:
            return True
    except:
        return False
m = eval(input("请输入一个字符串:"))
print(isNum('m'))
