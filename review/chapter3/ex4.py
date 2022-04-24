# #ex4.1
# import time
#
# scale = 10
# print("------执行开始------")
# for i in range (scale + 1):
#     a, b = '**' * i, '..' * (scale + 1)
#     c = (i / scale) * 100
#     print("%{:^3.0f}[{}->{}]".format(c, a, b))
#     time.sleep(0.1)
# print("------执行结束------")


# #ex4.2 单行动态刷新
# import time
#
# for i in range (101):
#     print("{:2}%".format(i),end=" ")
#     time.sleep(0.05)


#ex4.3带刷新的文本进度条
import time

scale = 50
print("执行开始".center(scale // 2, '-'))
t = time.perf_counter()
for i in range (scale + 1):
    a = '*' * i
    b = '.' * (scale - 1)
    c = (i / scale) * 100
    t -= time.perf_counter()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, -t), end=" ")
    time.sleep(0.05)
print("\n" + "执行结束".center(scale // 2, '-'))