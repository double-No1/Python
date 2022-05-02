# textFile = open("7.1.txt", "rt", encoding="utf-8")
# print(textFile.readline())
# textFile.close()
# bindFile = open("7.1.txt", "rb")
# ss = bindFile.readline()
# bindFile.close()
#
# print(ss)
# s = open("test.txt", "wb")
# s.write(ss)
#
# textFile = open("7.1.txt", "rt", encoding="utf-8")
# m = textFile.read(2)
# textFile.close()
# print(m)


fname = input("请输入要写入的文件:")
fo = open(fname, "w+", encoding="utf-8")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
