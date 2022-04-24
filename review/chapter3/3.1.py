x = eval(input ("请输入你的体重："))
y = 0.165 * x
for i in range(10):
    x += 0.5
    y = 0.165 * x
    print(x, y)
