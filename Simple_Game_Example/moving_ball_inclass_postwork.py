from tkinter import * #you don't need the tk.


'''
Shapely Documentation
https://pypi.org/project/Shapely/
https://gis.stackexchange.com/questions/90055/finding-if-two-polygons-intersect-in-python
'''

from random import randint

#We are storing the directional data of the ball here.  We could store it inside
#the function, but if there are other functions that need access them they need 
#to be placed here.  Another important thing to be aware of is that we are limited
#in some respects because we are not using something called object oriented programming.
#There is a much better way to do this, but is more involved from a coding persepective

ball1data = [-1,2]

def move_ball():

	canvas.move(ball1, ball1data[0], ball1data[1])
	#canvas.move(ball2, ball2data[0], ball2data[1])

	b1 = canvas.coords(ball1)
	bx1 = b1[0]
	by1 = b1[1]
	bx2 = b1[2]
	by2 = b1[3]


	if (bx1 < 5):
		ball1data[0] = 1
	if (by2 > 295):
		ball1data[1] = -2
	if (bx2 > 295):
		ball1data[0] = -1
	if (by1 < 5):
		ball1data[1] = 2

	#print(bx1)
	root.after(10,move_ball)

def move(event):
	print("MOVE")
	b1 = canvas.coords(ball1)
	bx1 = b1[0]
	by1 = b1[1]
	bx2 = b1[2]
	by2 = b1[3]

def click(event):
	print("CLICK")
	b1 = canvas.coords(ball1)
	bx1 = b1[0]
	by1 = b1[1]
	bx2 = b1[2]
	by2 = b1[3]

root = Tk()
root.title("Moving Balls")
root.resizable(False,True);

#Notice that whenever I make an element
canvas = Canvas(root,width = 300, height = 300);
canvas.pack()

#Two things
# 1. I have to set up a timed interval to run a function
# 2. I have to tell the ball to move
ball1 = canvas.create_oval(50, 50, 60, 60, fill="red")
wall = canvas.create_rectangle(3,3,300,300)
print(ball1)


#Create a function that is called on timed intervals
root.after(10,move_ball)
root.bind("<Motion>",move)
root.bind("<Button-1>",click)
#What happens with the below line is it creates a game loop that runs and 
#waits for an event. 
root.mainloop();

print("DONE GAME")

