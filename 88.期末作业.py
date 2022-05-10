# 1。读入字典类型的字符串，2.判断是否是字典类型，不是提示，3.翻转键值对，输出

s = input()
# s = '{"a": 1, "b": 2}'
s1 = {"a": 1, "b": 2}
ds = eval(s)

if type(ds) == type(s1):
    d = {}
    for key in ds:
        d[ds[key]] = key
    print(d)
else:
    print('输入错误')

# print(type(ds), type(d))

# 《沉默的羔羊》之最多单词
import jieba
with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) >= 2:
            counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    word, num = items[0]
    print(word)