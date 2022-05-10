# 获取文件的有效行数，空行不算，输出“共xx行。
# 1.读取文件  2.判断是否为空行，如果不是则+1行；判断什么时候结束   3.输出结果
f = open('latex.log', 'rt', encoding='utf-8')
lines = f.readlines()
hangshu = 0
for line in lines:
    if line[0] == line[-1]:
        continue
    elif line[-1] == "\n":
        hangshu += 1

print("共{}行".format(hangshu))
f.close()

# ------------------------------------- #

#统计小写字母a-z的分布，输出结果
#1.读取文件，读取所有内容  2.设置空字典，字母为键，出现次数为值  3.遍历所有字符，如果有a就+1  4.按照a-z的key排序，怎么操作？
f = open('latex.log', encoding='utf-8')
chars = f.read()
# print(chars[0:500])
zidian = {}
for char in chars:
    if char in [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]:
        zidian[char] = zidian.get(char, 0) + 1

# 对键排序
lsKeys = zidian.keys()
str1 = ''
for i in sorted(lsKeys):
    str1 += "{}:{},".format(i, zidian[i])

# print(str1[0:-1])
# 统计一共包含的字符数量
zidian1 = {}
for char in chars:
    zidian1[char] = zidian1.get(char, 0) + 1
lsValues1 = zidian1.values()
sum = 0
for j in lsValues1:
    sum += j
# print(sum)

print("共{}字符,".format(sum) + str1[0:-1])
# print(type(lsKey), lsKey)
# print(zidian)
f.close()

# -------------------------------- #
# 1.读取文件，读取每一行 2.比较每一行，其实可以用集合的方式去重，算下集合的元素就OK了

f = open('latex.log', encoding='utf-8')
lines = f.readlines()
set1 = set(lines)
n = len(set1)
print("共{}独特行".format(n))
print(set1)

# ---------------------- #
# 1.打开文件，读取每一行， 2.将行内的元素反转 3.输出到新文件。问题在于 [::-1]中的逗号空格无法处理，reversed函数只返回了地址。

f = open('data.csv', encoding="utf-8")
lines = f.readlines()  #列表类型的每一行
for line in lines:
    if line[-1] == "\n":
        line = line[:-1]
    line = line[::-1]
    print(line)

# ----------------------------- #
# 1.读取文件，读取每一行， 2.读取每一行的字符，将空格删除后，重新以,号组装起来。
f = open('data.csv', encoding='utf-8')
lines = f.readlines()

for line in lines:
    str1 = ''
    for char in line:
        if char == ' ':
            char = ''
            str1 += char
        else:
            str1 += char

    if str1[-1] == '\n':
        print(str1[:-1])
    else:
        print(str1)

f.close()

#-----------------------#
# 1.打开文件，读取每一行， 2.将行内的元素反转 3.输出到新文件。问题在于 [::-1]中的逗号空格无法处理，reversed函数只返回了地址。 4.往反转后的字符串恢复成原本的空间状态，太复杂了。

f = open('data.csv', encoding='utf-8')
lines = f.readlines()
strSum = ''
for line in lines:
    str1 = ''
    for char in line:
        if char == ' ':
            char = ''
            str1 += char
        else:
            str1 += char

    strSum += str1
# if str1[-1] == '\n':
#     str2 = str1[:-1]
#     strSum += str2
#     # print(str2[::-1])
# else:
#     strSum += str1
#     # print(str1[::-1])
print(repr(strSum))
