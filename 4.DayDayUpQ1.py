# DayDayUpQ1.py
# dayfactor = 0.005
# dayup = pow(1+dayfactor,365)
# daydown = pow(1-dayfactor,365)
#
# print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

# DayDayUpQ3.py 工作日的力量
dayfactor = 0.01
dayup = 1
for i in range(365):
    if i%7 in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)

print("向上的力量：{:.2f}".format(dayup))

# 打印星座字符
for i in range(12):
    print(chr(9800 + i),end=' ')