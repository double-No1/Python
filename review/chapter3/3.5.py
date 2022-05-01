#田字格的输出.py
a = ' + '
b = ' - '
c = ' | '
d = '   '
for i in range(11):
    if i in [0, 5, 10]:
        print('{0}{1}{0}{1}{0}'.format(a, b*4))
    else:
        print('{0}{1}{0}{1}{0}'.format(c, d*4))


