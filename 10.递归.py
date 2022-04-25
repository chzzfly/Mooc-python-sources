def fn(n):
    if n == 0:
        return 1
    else:
        return n * fn(n - 1)


print(fn(5))


# 将字符串反转
def rev(s):
    if s == "":
        return s
    else:
        # 将字符串的第一个字符放到后面，其他不变
        return rev(s[1:]) + s[0]


print(rev("hello,world!"))


# 斐波那锲序列
def fbnq(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbnq(n - 1) + fbnq(n - 2)


print(fbnq(4))

# 汉诺塔问题，不懂啊！
count = 0


def hannota(n, start, end, mid):
    global count
    if n == 1:
        # 只有一个圆盘的时候，鲜明的步骤打印如下
        print("{}：{}->{}".format(1, start, end))
        count += 1
    else:
        hannota(n - 1, start, mid, end)
        print("{}：{}->{}".format(n, start, end))
        count += 1
        hannota(n - 1, mid, end, start)


hannota(5, 'A', 'C', 'B')
print(count)