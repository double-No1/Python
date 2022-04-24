# #方法一
# weekstr = "星期一星期二星期三星期四星期五星期六星期日"
# weekid = eval(input("请输入数字1-7："))
# pos = (weekid - 1) * 3
# print(weekstr[pos:pos+3])


# #方法二
# weekstr = "一二三四五六日"
# weekid = eval(input("请输入数字1-7："))
# print("星期" + weekstr[weekid - 1])


weekstr = "一二三四五六日"
for s in weekstr:
    print("星期" + s, end="  ")