import time
for i in range(4):
        # scale = i//30
        a = '.' * i
        print('\rStarting {}'.format(a), end='')
        time.sleep(1)
print(' Done!')


# from time import sleep
#
# print("Starting", end="")
# for i in range(10):
#     print("..", end="")
#     sleep(0.5)
# print("Done!")