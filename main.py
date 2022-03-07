import turtle
import math

def drawSineCurve(myturtle=None):
  for angle in range(-360, 360):
    y = math.sin(math.radians(angle))
    fred.goto(angle, y)
  fred.penup()
  
def setupWindow(mywindow=None):
  wn = turtle.Screen()
  fred = turtle.Turtle()
  turtle.bgcolor("lightgreen")
  turtle.setworldcoordinates(-360, -1.5, 360, 1.5)

def setupAxis(myturtle=None):
  fred.goto(-360, 0)
  fred.goto(360, 0)
  fred.goto(0,0)
  fred.goto(0, -1.5)
  fred.goto (0, 1.5)
  fred.goto(0,0)

def drawCosineCurve(myturtle=None):
  fred.pendown()
  for angle in range(-360,361):
    y=math.cos(math.radians(angle))
    fred.goto(angle, y)
  fred.penup()

def drawTangentCurve(myturtle=None):
  fred.speed(0)
  fred.pendown()
  for angle in range(-360, 361):
    y=math.tan(math.radians(angle))
    fred.goto(angle,y)

setupWindow()
setupAxis()
drawSineCurve()
drawCosineCurve()
drawTangentCurve()


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
