# #DayDayUp365 1
# import math
#
# dayup = math.pow((1.0 + 0.001), 365)           #提高0.001
# daydown = math.pow((1.0 - 0.001), 365)         #放任0.001
# print("向上:{:.2f}, 向下:{:.2f}.".format(dayup, daydown))


# #DayDayUp365 2
# import math
#
# dayfactor = 0.001
# dayup = math.pow((1.0 + dayfactor), 365)           #提高0.001
# daydown = math.pow((1.0 - dayfactor), 365)         #放任0.001
# print("向上:{:.2f}, 向下:{:.2f}.".format(dayup, daydown))


# #DayDayUp365 3
# dayup, dayfactor = 1.0, 0.01
# for i in range(365):
#     if i % 7 in[6, 0]:
#         dayup = dayup * (1 - dayfactor)
#     else:
#         dayup = dayup * (1 + dayfactor)
# print("向上5天，向下2天的力量: {:.2f}.".format(dayup))


#DayDayUp365 4
def DayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while (DayUP(dayfactor) < 37.78):
    dayfactor += 0.001
print("每天努力的参数是: {:.3f}.".format(dayfactor))