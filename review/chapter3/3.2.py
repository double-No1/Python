dayup = 1.0
for i in range(365):
    if i % 7 in [0, 1, 2]:
        dayup = dayup
    else:
        dayup = dayup * (1 + 0.01)
print("连续学习365天的值为: {:.3f}.".format(dayup))