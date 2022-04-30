#CalHamletV1.py


#获取文本文件，把单词转为小写，特殊符号替换为空格，归一化处理
def getText():
    txt = open("hamlet.txt", 'r').read()
    txt = txt.lower()
    for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_{|}~'":
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    if word in [
            'the', 'and', 'to', 'of', 'you', 'i', 'a', 'my', 'in', 'it',
            'that', 'is', 'not', 'his', 'this', 'but', 'with', 'for', 'your',
            'me', 'be', 'as', 'he', 'what', 'him'
    ]:
        continue
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
#使用多元选项的第二个列，作为排序列，从大到小
items.sort(key=lambda x: x[1], reverse=True)
for i in range(1000):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
