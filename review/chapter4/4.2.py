#判断一串字符中英文字符数字空格其他字符个数

str = input("请输入一串字符:")
a, b, c, d = 0, 0, 0, 0
for s in str:
    if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
        a += 1
    elif '0' <= s <= '9':
        b += 1
    elif s == '':
        c += 1
    else:
        d += 1
print("英文字符有{}个，数字有{}个，空格有{}个，其他字符有{}个".format(a, b, c, d))