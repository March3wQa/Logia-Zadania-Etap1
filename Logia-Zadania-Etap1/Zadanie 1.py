### IMPORT ###
import turtle
##############

def domki(n):

	pos = [0, 0]
	t = turtle.Turtle()
	t.pu()

	### FASADA ###
	t.goto(pos)
	t.fillcolor('yellow')
	t.pd()
	t.begin_fill()
	t.goto(pos[0]+100, pos[1]+0)
	t.goto(pos[0]+100, pos[1]+100)
	t.goto(pos[0]+0, pos[1]+100)
	t.goto(pos)
	t.end_fill()
	t.pu()
	##############









domki(0)
while 1:
	pass