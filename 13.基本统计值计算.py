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
def midum(numbers):
    sorted(numbers)

    l = len(numbers)
    if l % 2 != 0:
        return numbers[l // 2]
    else:
        i = (numbers[l // 2] + numbers[len(numbers) // 2 - 1]) / 2
        return i


print(midum([1, 2, 3, 4]))
