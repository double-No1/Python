# import random as r
#
# a = ["1", "2", "3", "4"," 5"," 6"," 7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", \
#      "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", \
#      "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", \
#      "C", "V", "B", "N", "M"]
# def code():
#     mi = ""
#     global a
#     for i in range(8):
#         n = r.randint(0, 61)
#         mi = mi + a[n]
#     return mi
# def main():
#     for i in range(1, 11):
#         print("the {} code is {} ".format(i,code()))
# main()


import random

list = []     #字符列表
m = []       #密码列表
for i in range(10):
    list.append(str(i))
for i in range(65, 91):
    list.append(chr(i))
for i in range(97, 123):
    list.append(chr(i))
for i in range(10):
    for j in range(8):
        m.append(random.choice(list))
    print("".join(m))
    m = []