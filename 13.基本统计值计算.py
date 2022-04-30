#CalStatisticsV1.py


# 用户输入功能
def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums


# 求平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)


# 求标准方差
def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1), 0.5)


# 求中位数
def medium(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 != 0:
        return numbers[size // 2]
    else:
        med = (numbers[size // 2] + numbers[size // 2 - 1]) / 2
        return med


n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2f}，中位数：{}。".format(m, dev(n, m), medium(n)))