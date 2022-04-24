import random

guess = random.randint(0, 100)
count = 0
while True:
    n = int(input("请输入0-100之间的整数:"))
    count += 1
    if n < guess:
        print("遗憾，太小了！")
        continue
    elif n > guess:
        print("遗憾，太大了！")
        continue
    else:
        print("预测{}次，你猜中了！".format(count))
        break
