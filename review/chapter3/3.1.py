# #重量计算
# x = eval(input("请输入你的体重："))
# y = 0.165 * x
# for i in range(10):
#     x += 0.5
#     y = 0.165 * x
#     print(x, y)

#重量计算
weight = eval(input('请输入你的体重(kg)：'))
for i in range(10):
        new_weight = weight + 0.5 * (i + 1)
        print('未来第{:^5}年地球体重为{:.3f}kg,月球体重为{:.3f}kg'.format(i+1, new_weight, new_weight*0.165))
