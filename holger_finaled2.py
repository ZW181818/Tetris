import turtle
import random
import time

cells, future_cells = [], []
stop = False

def drawScreenBorders(): 
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-350,350)
    pen.pendown()
    for i in range(4):
        pen.forward(700)
        pen.right(90)
def initializeTheCells():
    for i in range(35):
        cells.append([]) 
        for j in range(35):
            newCell = turtle.Turtle()
            newCell.penup()
            newCell.shape("square")
            newCell.shapesize(stretch_wid = 0.9, stretch_len = 0.9)
            rand = random.randint(0, 1)
            newCell.state = rand
            cells[i].append(newCell)

            if rand == 0:
                newCell.color("gray100") 
            else: 
                newCell.color("gray0")

    for i in range(35):
        future_cells.append([])
        for j in range(35):
            future_cells[i].append(0)
def showTheUniverse():
    ycor = 340
    for i in range(35):
        xcor = -340
        for j in range(35):
            cells[i][j].goto(xcor, ycor)
            xcor += 20
        ycor -= 20
def esc():
    global stop
    stop = True
def getNeighbors(i, j):

    if boundaryCondition == 1:
        
        if i == 0 and j == 0: #左上角
            return cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state
        
        elif i == 0 and j == 34: #右上角
            return cells[i][j - 1].state + cells[i + 1][j - 1].state + cells[i + 1][j].state
        
        elif i == 34 and j == 0: #左下角
            return cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state

        elif i == 34 and j == 34: #右下角
            return cells[i][j - 1].state + cells[i - 1][j - 1].state + cells[i - 1][j].state
    
        elif ( i > 0 and i < 34 ) and j == 0: #左
            return cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state

        elif ( i > 0 and i < 34 ) and j == 34: #右
            return cells[i - 1][j].state + cells[i - 1][j - 1].state + cells[i][j - 1].state + cells[i + 1][j - 1].state + cells[i + 1][j].state

        elif i == 0 and ( j > 0 and j < 34 ): #上
            return cells[i][j - 1].state + cells[i + 1][j - 1].state + cells[i + 1][j].state + cells[i + 1][j + 1].state + cells[i][j + 1].state 

        elif i == 34 and ( j > 0 and j < 34 ): #下
            return cells[i][j - 1].state + cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state

        elif ( i > 0 and i < 34 ) and ( j > 0 and j < 34 ): #非邊框區域
            return cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j - 1].state + cells[i][j + 1].state + cells[i + 1][j - 1].state + cells[i + 1][j].state + cells[i + 1][j + 1].state

    elif boundaryCondition == 2:

        if i == 0 and j == 0: #左上角
            return cells[34][34].state + cells[34][j].state + cells[34][j+1].state + cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state + cells[i + 1][34].state + cells[i][34].state
        
        elif i == 0 and j == 34: #右上角
            return cells[34][j - 1].state + cells[34][j].state + cells[34][0].state + cells[i][0].state + cells[i + 1][0].state + cells[i + 1][j].state + cells[i + 1][j - 1].state + cells[i][j - 1].state
        
        elif i == 34 and j == 0: #左下角
            return cells[i - 1][34].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state + cells[0][j + 1].state + cells[0][j].state + cells[0][34].state + cells[i][34].state

        elif i == 34 and j == 34: #右下角
            return cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][0].state + cells[i][0].state + cells[0][0].state + cells[0][j].state + cells[0][j-1].state + cells[i][j - 1].state
    
        elif ( i > 0 and i < 34 ) and j == 0: #左
            return cells[i - 1][34].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state + cells[i + 1][34].state + cells[i][34].state

        elif ( i > 0 and i < 34 ) and j == 34: #右
            return cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][0].state + cells[i][0].state + cells[i + 1][0].state + cells[i + 1][j].state + cells[i + 1][j - 1].state + cells[i][j - 1].state

        elif i == 0 and ( j > 0 and j < 34 ): #上
            return cells[34][j - 1].state + cells[34][j].state + cells[34][j + 1].state + cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state + cells[i + 1][j - 1].state + cells[i][j - 1].state

        elif i == 34 and ( j > 0 and j < 34 ): #下
            return cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state + cells[0][j + 1].state + cells[0][j].state + cells[0][j - 1].state + cells[i][j - 1].state

        elif ( i > 0 and i < 34 ) and ( j > 0 and j < 34 ): #非邊框區域
            return cells[i - 1][j - 1].state + cells[i - 1][j].state + cells[i - 1][j + 1].state + cells[i][j + 1].state + cells[i + 1][j + 1].state + cells[i + 1][j].state + cells[i + 1][j - 1].state + cells[i][j - 1].state

    return 0
def updateCells(destiny,i,j):

    global future_cells

    if cells[i][j].state == 1:

        if destiny < 2 or destiny > 3:
            future_cells[i][j] = 0
            cells[i][j].color("gray50")
        elif destiny == 2 or destiny == 3: 
            future_cells[i][j] = 1
            cells[i][j].color("gray0")
        else: 
            future_cells[i][j] = cells[i][j].state
            cells[i][j].color("gray0")

    elif cells[i][j].state == 0:

        if destiny == 3: 
            future_cells[i][j] = 1
            cells[i][j].color("gray0")
        else: 
            future_cells[i][j] = cells[i][j].state
def color_changer(i, j):

    global cells

    cc = cells[i][j].color()[1]

    if cc == "gray0":
        cells[i][j].color("gray0")
    elif cc == "gray50":
        cells[i][j].color("gray60")
    elif cc == "gray60":
        cells[i][j].color("gray70")
    elif cc == "gray70":
        cells[i][j].color("gray80")
    elif cc == "gray80":
        cells[i][j].color("gray90")
    elif cc == "gray90":
        cells[i][j].color("gray100")
    elif cc == "gray100":
        cells[i][j].color("gray100")
        
#?------------------------------------------------------------------------------------------------------------------------------------------?#

boundaryCondition = int(input("Choose the Boundary Condition? \nEnter 1 for Constant or 2 for Periodic: "))
print("Press ESC to exit")

wn = turtle.Screen()
wn.setup(width = 35*20, height = 35*20)
wn.title("Life Game")
wn.tracer(0)
wn.listen()
wn.onkeypress(esc, "Escape")

drawScreenBorders()
initializeTheCells()
showTheUniverse()

while not stop:

    # update future
    for i in range(35):
        for j in range(35):
            destiny = getNeighbors(i, j)
            updateCells(destiny, i, j)

    # replace from future
    for i in range(35):
        for j in range(35):
            cells[i][j].state = future_cells[i][j]

    # change color
    for i in range(35):
        for j in range(35):
            color_changer(i, j)
    

    wn.update()
    time.sleep(5)
