# 1.读取文件，读取每一行， 2.读取每一行的字符，将空格删除后，重新以,号组装起来。
f = open('data.csv', encoding='utf-8')
lines = f.readlines()

str2 = ''
for line in lines:
    str1 = ''
    for char in line:
        if char == ' ':
            char = ''
            str1 += char
        else:
            str1 += char

    # if str1[-1] == '\n':
    #     print(str1[:-1])
    # else:
    #     print(str1)

    str2 += str1
str3 = str2[::-1]
print(str3.replace(',', ';'))
f.close()