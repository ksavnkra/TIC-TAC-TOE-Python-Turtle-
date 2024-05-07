from turtle import *
import time
from sys import *
import random

# GAME--------------------------------------------------------
b = [   
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
    ]  # 1 FOR 0 AND 2 FOR X--
turn = 1  # 1 FOR X AND 0 FOR O-------------------------------
# ------------------------------------------------------------

# SCREEN------------------------------------------------------
scr = Screen()
scr.setup(700, 560)
scr.title("TIC TAC TOE")
scr.tracer(1, 0)
# ------------------------------------------------------------

# DECLARING TURTLE--------------------------------------------
pencil = Turtle()
pencil.hideturtle()
pencil.width(2)
# ------------------------------------------------------------


def heading():
    # HEADING-------------------------------------------------
    pencil.up()
    pencil.goto(0, 250)
    pencil.down()
    fontcolor = pencil.color("black")
    pencil.write(
        "WELCOME TO THE TIC TAC TOE", align="center", font=("courier", 20, "bold")
    )
    # --------------------------------------------------------


def reload():
    heading()
    pattern()
    time.sleep(0.5)


def pattern():
    pencil.fillcolor("yellow")
    pencil.up()
    pencil.goto(-150, 50)
    pencil.begin_fill()
    pencil.down()
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.end_fill()
    pencil.up()
    pencil.right(90)
    pencil.goto(-150, -50)
    pencil.up()
    pencil.begin_fill()
    pencil.down()
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.end_fill()
    pencil.up()
    pencil.begin_fill()
    pencil.goto(-50, -150)
    pencil.down()
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.end_fill()
    pencil.right(90)
    pencil.up()
    pencil.begin_fill()
    pencil.goto(50, -150)
    pencil.down()
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(300)
    pencil.right(90)
    pencil.fd(10)
    pencil.end_fill()
    pencil.right(180)


def drawX(x, y):
    pencil.up()
    pencil.goto(x - 2.07106781187, y - 4.2)
    pencil.fillcolor("red")
    pencil.begin_fill()
    pencil.down()
    pencil.left(135)
    pencil.fd(45)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(45)
    pencil.left(90)
    pencil.fd(45)
    pencil.right(90)
    pencil.fd(10)
    pencil.right(90)
    pencil.fd(45)
    pencil.up()
    pencil.goto(x - 2.07106781187, y - 4.2)
    pencil.down()
    pencil.fd(45)
    pencil.left(90)
    pencil.fd(10)
    pencil.left(90)
    pencil.fd(45)
    pencil.right(90)
    pencil.fd(45)
    pencil.left(90)
    pencil.fd(10)
    pencil.left(90)
    pencil.fd(45)
    pencil.end_fill()
    pencil.right(135)


def drawO(x, y):
    pencil.speed(0)
    pencil.fillcolor("blue")
    pencil.up()
    pencil.goto(x + 5, y - 45)
    pencil.down()
    pencil.begin_fill()
    pencil.circle(40)
    pencil.end_fill()
    pencil.up()
    pencil.goto(x + 5, y - 35)
    pencil.fillcolor("white")
    pencil.down()
    pencil.begin_fill()
    pencil.circle(30)
    pencil.end_fill()


def choices():
    heading()
    pencil.up()
    pencil.goto(0, 200)
    pencil.write(
        "WITH WHOM WOULD YOU LIKE TO PLAY?",
        align="center",
        font=("courier", 18, "bold"),
    )
    pencil.goto(0, 120)
    pencil.write("HUMAN", align="center", font=("courier", 18, "bold"))
    pencil.goto(0, 0)
    pencil.write("MACHINE", align="center", font=("courier", 18, "bold"))
    # BOX AROUND HUMAN OPTION---------------------------------
    pencil.up()
    pencil.goto(-52, 150)
    pencil.down()
    pencil.fd(102)
    pencil.right(90)
    pencil.fd(30)
    pencil.right(90)
    pencil.fd(102)
    pencil.right(90)
    pencil.fd(30)
    # --------------------------------------------------------

    # BOX AROUND MACHINE OPTION-------------------------------
    pencil.up()
    pencil.goto(-60, 0)
    pencil.down()
    pencil.fd(30)
    pencil.right(90)
    pencil.fd(115)
    pencil.right(90)
    pencil.fd(30)
    pencil.right(90)
    pencil.fd(115)
    # --------------------------------------------------------


def machine_visual_by_computer():
    time.sleep(0.05)
    global turn
    if turn == 0:
        avaliable = [(i, j) for i in range(3) for j in range(3) if b[i][j] == 0]
        if avaliable:
            row, column = random.choice(avaliable)
            b[row][column] = 1
            turn = 1 - turn
            if row == 0 and column == 0:
                drawO(-100, 100)
            elif row == 0 and column == 1:
                drawO(0, 100)
            elif row == 0 and column == 2:
                drawO(100, 100)
            elif row == 1 and column == 0:
                drawO(-100, 0)
            elif row == 1 and column == 1:
                drawO(0, 0)
            elif row == 1 and column == 2:
                drawO(100, 0) 
            elif row == 2 and column == 0:
                drawO(-100, -100)
            elif row == 2 and column == 1:
                drawO(0, -100)
            elif row == 2 and column == 2:
                drawO(100, -100)
            check()
            onscreenclick(machine_visual_by_player)


def machine_visual_by_player(x, y):
    global row, column, turn
    if y > 50 and y < 150 and turn == 1:
        row = 0
        if x > -150 and x < -50:
            column = 0
            if turn == 1 and b[row][column] == 0:
                drawX(-100, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > -50 and x < 50:
            column = 1
            if turn == 1 and b[row][column] == 0:
                drawX(0, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > 50 and x < 150:
            column = 2
            if turn == 1 and b[row][column] == 0:
                drawX(100, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

    elif y > -50 and y < 50 and turn == 1:
        row = 1
        if x > -150 and x < -50:
            column = 0
            if turn == 1 and b[row][column] == 0:
                drawX(-100, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > -50 and x < 50:
            column = 1
            if turn == 1 and b[row][column] == 0:
                drawX(0, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > 50 and x < 150:
            column = 2
            if turn == 1 and b[row][column] == 0:
                drawX(100, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

    elif y > -150 and y < -50 and turn == 1:
        row = 2
        if x > -150 and x < -50:
            column = 0
            if turn == 1 and b[row][column] == 0:
                drawX(-100, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > -50 and x < 50:
            column = 1
            if turn == 1 and b[row][column] == 0:
                drawX(0, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()

        elif x > 50 and x < 150:
            column = 2
            if turn == 1 and b[row][column] == 0:
                drawX(100, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()
                machine_visual_by_computer()


def choice_select(x, y):
    if x > -52 and x < 50 and y > 120 and y < 150:
        scr.clear()
        scr.tracer(1, 0)
        pencil.right(180)
        reload()
        onscreenclick(human_visual)

    if x > -60 and x < 55 and y > 0 and y < 30:
        scr.clear()
        scr.tracer(1, 0)
        pencil.right(180)
        reload()
        onscreenclick(machine_visual_by_player)


def human_visual(x, y):
    global row, column, turn
    if y > 50 and y < 150:
        row = 0
        if x > -150 and x < -50:
            column = 0
            if turn == 0 and b[row][column] == 0:
                drawO(-100, 100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(-100, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > -50 and x < 50:
            column = 1
            if turn == 0 and b[row][column] == 0:
                drawO(0, 100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(0, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > 50 and x < 150:
            column = 2
            if turn == 0 and b[row][column] == 0:
                drawO(100, 100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(100, 100)
                b[row][column] = 2
                turn = 1 - turn
                check()

    elif y > -50 and y < 50:
        row = 1
        if x > -150 and x < -50:
            column = 0
            if turn == 0 and b[row][column] == 0:
                drawO(-100, 0)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(-100, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > -50 and x < 50:
            column = 1
            if turn == 0 and b[row][column] == 0:
                drawO(0, 0)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(0, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > 50 and x < 150:
            column = 2
            if turn == 0 and b[row][column] == 0:
                drawO(100, 0)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(100, 0)
                b[row][column] = 2
                turn = 1 - turn
                check()

    elif y > -150 and y < -50:
        row = 2
        if x > -150 and x < -50:
            column = 0
            if turn == 0 and b[row][column] == 0:
                drawO(-100, -100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(-100, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > -50 and x < 50:
            column = 1
            if turn == 0 and b[row][column] == 0:
                drawO(0, -100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(0, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()

        elif x > 50 and x < 150:
            column = 2
            if turn == 0 and b[row][column] == 0:
                drawO(100, -100)
                b[row][column] = 1
                turn = 1 - turn
                check()

            elif turn == 1 and b[row][column] == 0:
                drawX(100, -100)
                b[row][column] = 2
                turn = 1 - turn
                check()


def check():
    if b[0][0] == 2 and b[0][1] == 2 and b[0][2] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[1][0] == 2 and b[1][1] == 2 and b[1][2] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[2][0] == 2 and b[2][1] == 2 and b[2][2] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][0] == 2 and b[1][0] == 2 and b[2][0] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][1] == 2 and b[1][1] == 2 and b[2][1] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][2] == 2 and b[1][2] == 2 and b[2][2] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][0] == 2 and b[1][1] == 2 and b[2][2] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][2] == 2 and b[1][1] == 2 and b[2][0] == 2:
        scr.clear()
        scr.tracer(1, 0)
        drawX(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][0] == 1 and b[0][1] == 1 and b[0][2] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[1][0] == 1 and b[1][1] == 1 and b[1][2] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[2][0] == 1 and b[2][1] == 1 and b[2][2] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][0] == 1 and b[1][0] == 1 and b[2][0] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][1] == 1 and b[1][1] == 1 and b[2][1] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][2] == 1 and b[1][2] == 1 and b[2][2] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    elif b[0][2] == 1 and b[1][1] == 1 and b[2][0] == 1:
        scr.clear()
        scr.tracer(1, 0)
        drawO(-100, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("WIN", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()

    draw_flag = all(b[i][j] != 0 for i in range(3) for j in range(3))

    if draw_flag == True:
        scr.clear()
        scr.tracer(1, 0)
        pencil.up()
        pencil.goto(0, -20)
        pencil.down()
        pencil.write("DRAW", align="center", font=("Courier", 28, "bold"))
        pencil.up()
        pencil.goto(0, 100)
        pencil.write(
            "THE END\nTHANKS FOR PLAYING!\n\nGAME WILL END IN 1 SECOND!",
            align="center",
            font=("Courier", 28, "bold"),
        )
        time.sleep(2.0)
        exit()


choices()
onscreenclick(choice_select)
done()
