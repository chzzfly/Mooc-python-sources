#7段数码管的绘制
import turtle


# 绘制七段数码管的一段
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


# 根据数字，绘制单个的七段数码管
def drawDigit(digit):
    #如果是2,3,4,5,6,8,9，我们就需要真实地画出第一条线，其他数字017则飞过去
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    #如果是013456789，我们就需要真实地绘制第二条线，其他数字2则飞过去
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for i in date:
        drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20220425')
    turtle.hideturtle()
    turtle.done()


main()