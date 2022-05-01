#coding=utf-8
from datetime import datetime as dt
DOB = dt(2001, 10, 17, 19, 0, 0)

print(DOB.strftime("%Y-%m-%d %H:%M:%S"))
print(DOB.strftime("%Y,%B,%d %H:%M:%S"))
print(DOB.strftime("%Y-%b-%d %H:%M:%S"))
print(DOB.strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(DOB.strftime("%Y-%m-%d %I%p"))
print(DOB.strftime("%Y年%m月%d日 %A"))
print(DOB.strftime("%Y年%m月%d日 %a"))
