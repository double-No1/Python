# 文本字符分析
str = input("请输入要分析的字符串，回车表示结束：")
while str != '':
    counts = {}   # 创建字典类型保存结果
    for ch in str:     # 扫描字符串，统计出现频率
        counts[ch] = counts.get(ch, 0) + 1
    items = list(counts.items())    # 改变类型为列表类型，按照出现频率降序排列
    items.sort(key=lambda x: x[1], reverse=True)    # 利用sort函数排序
    for i in range(len(items)):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
    str = input("请输入要分析的字符串，回车表示结束：")