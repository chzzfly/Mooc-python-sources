# 1.TempConvert.py
flag = True
while flag:
    TempStr = input("请输入带有符号的温度值：")
    if TempStr == 'exit':
        flag = False
        break
    if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        print("您输入的是华氏温度，转换后的温度是{:.2f}摄氏度".format(C))
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8 * eval(TempStr[0:-1]) + 32
        print("您输入的是摄氏温度，转换后的温度是{:.2f}华氏度".format(F))
    else:
        print("输入格式有误，请检查！")
