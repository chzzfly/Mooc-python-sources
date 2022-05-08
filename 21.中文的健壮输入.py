# 1.只能是数字 2.可以是浮点数或复数、整数，整数只接收十进制形式 3.平方运算打印结果

from email import charset

a = input()
ls = [
    '+',
    'j',
    '.',
]
flag = True
for i in range(48, 58):
    ls.append(chr(i))
for char in a:
    if char in ls:
        continue
    else:
        flag = False

if flag == False:
    print('输入有误')
else:
    b = eval(a)
    c = b**2
    print(c)