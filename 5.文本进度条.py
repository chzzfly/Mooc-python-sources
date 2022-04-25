# 格式化字符串
import time
# print("{:-^30}".format("开始"))
# start = time.perf_counter()
# print(time.time())
# print(time.ctime())
# print(time.gmtime())
# t = time.gmtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",t))
# print(time.strptime("2022-04-21 12:25:28","%Y-%m-%d %H:%M:%S"))
# print("中间分隔线".center(30,"-"))
# time.sleep(0.11)
# end = time.perf_counter()
# jiangeTime = end - start
# print("间隔时间是：{}".format(jiangeTime))
# print("结束".center(30,"="))

# 打印文本进度条

scale = 55
print("执行开始".center(scale,"="))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{3:.2f}s [{0}->{1}] {2:.0f}%".format(a,b,c,dur),end="")
    time.sleep(0.1)
print("\n{:=^55}".format("执行结束"))