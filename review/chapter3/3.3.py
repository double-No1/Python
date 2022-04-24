# dayup = 1.0
# for i in range(365):
#     if i % 10 in [0, 1, 2, 7, 8, 9]:
#         dayup = dayup
#     else:
#         dayup = dayup * (1 + 0.01)
#
# print("连续学习365天后的能力值为: {:.3f}.".format(dayup))



dayup = 1.0
for i in range(365): #以15天为单位计算能力增加值
        if i % 15 in [0, 1, 2, 7, 8, 9, 14]:
                dayup = dayup #第1，2，3，8，9，10，15天能力不变
        else:
                dayup *= (1+0.01) #第4-7，11-14天能力在之前基础上增加1%
print("连续学习365天后能力值为{:<.3f}".format(dayup))
