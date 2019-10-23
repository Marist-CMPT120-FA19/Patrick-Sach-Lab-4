from graphics import *
def trafficlight():
	win= GraphWin()
	black=Rectangle(Point(50,20),Point(150,175))
	black.setFill("black")
	black.setOutline("black")
	black.draw(win)
	red= Circle(Point(100,50),20)
	red.setFill("red")
	red.setOutline("black")
	red.draw(win)
	yellow= Circle(Point(100,100),20)
	yellow.setFill("yellow")
	yellow.setOutline("black")
	yellow.draw(win)
	green= Circle(Point(100,150),20)
	green.setFill("green")
	green.setOutline("black")
	green.draw(win)


trafficlight()
