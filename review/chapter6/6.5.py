import random

men = 10000
same = 0
birthday = []
for i in range(men):
    for j in range(23):
        birthday.append(random.randint(1, 365))
    if len(birthday) != len(set(birthday)):
        same += 1
    birthday = []
same = same/men
print("23人中至少两人生日相同的概率是:{:.3f}%".format(same*100))