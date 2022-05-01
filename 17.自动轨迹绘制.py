# import turtle as t

# t.title("自动轨迹绘制")
# t.setup(800, 600, 0, 0)
# t.pencolor('red')
# t.pensize(5)

# # 数据读取。假定数据为，300,1,144,0,1,0\n 代表长度、是否转向，转向角度，rgb颜色
# datals = []
# f = open('data.txt')
# for line in f:
#     line = line.replace('\n', '')
#     datals.append(list(map(eval, line.split(','))))
# f.close()

# # 自动绘制
# for i in range(len(datals)):
#     t.pencolor(datals[i][3], datals[i][4], datals[i][5])
#     t.fd(datals[i][0])
#     if datals[i][1]:
#         t.right(datals[i][2])
#     else:
#         t.left(datals[i][2])

# t.done()

#--------------#
import turtle

#读取文档所存放的数据
f = open('data.txt', 'r', encoding='utf-8')
lines = f.readlines()
ls = []
for line in lines:
    line = line.replace('\n', '')
    ls.append(list(map(eval, line.split(','))))

print(ls)
#根据数据画图