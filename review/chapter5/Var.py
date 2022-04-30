def LocalVar1(x):
	print('LocalVar1中x的值为：',x)
	x=100
	print('LocalVar1中x修改后的值为：',x)
	#print('LocalVar1中y的值为：',y)
	y=20
	print('LocalVar1中y的值为：',y)
def LocalVar2(): #定义函数LocalVar2
	x=10 #定义局部变量x，将其赋值为10
	print('LocalVar2中调用LocalVar1前x的值为：',x)
	LocalVar1(15) #调用LocalVar1函数
	print('LocalVar2中调用LocalVar1后x的值为：',x)
    # print('LocalVar2中y的值为：',y) 
LocalVar2()
