def find(list):
    if len(list) != len(set(list)):
        return True
    else:
        return False
list = []
list = input("请输入一些元素:")
while len(list) == 0:
    list = input("输入为空，请再输入一些元素:")
print(find(list))
