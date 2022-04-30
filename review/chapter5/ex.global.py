def GlobalVar1():
	print('GlobalVar1中x的值为：',x)
def GlobalVar2():
	x=100
	print('GlobalVar2中x的值为：',x)
x=20
GlobalVar1()
GlobalVar2()
GlobalVar1()