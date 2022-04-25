# pythonDraw.py
import turtle as t

# import turtle
# # 1. 绘制蟒蛇
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("pink")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40 * 2/3)
# turtle.done()

# 2.绘制Z字
# turtle.setup(800,400)
# turtle.penup()
# turtle.left(135)
# turtle.fd(100)
# turtle.pendown()
# turtle.seth(0)
# turtle.fd(150)
# turtle.right(135)
# turtle.fd(300)
# turtle.left(135)
# turtle.fd(150)

# 课后作业1

# t.pensize(20)
# t.pencolor("blue")
# t.setheading(-40)
# for i in range(4):
#     t.circle(40, 80)
#     t.circle(-40, 80)
# t.circle(40, 80/2)
# t.fd(40)
# t.circle(16, 180)
# t.fd(40 * 2/3)
# t.done()

# 课后作业2
# t.pensize(3)
# t.pencolor("black")
# for i in range(4):
#     t.fd(90)
#     t.left(90)
#
# t.done()

# 课后作业4
# t.pensize(3)
# t.pencolor("black")
# for i in range(9):
#     t.fd(100)
#     t.left(80)
# t.done()

# 课后作业5

t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
t.fd(150)
t.right(90)
t.circle(-150,45)
t.goto(0,0)
t.done()