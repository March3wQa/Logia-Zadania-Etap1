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

	### OKNA ###
	t.fillcolor('cyan')

	t.goto(pos[0]+20, pos[1]+20)
	t.pd()
	t.begin_fill()
	t.goto(pos[0]+40, pos[1]+20)
	t.goto(pos[0]+40, pos[1]+40)
	t.goto(pos[0]+20, pos[1]+40)
	t.goto(pos[0]+20, pos[1]+20)
	t.end_fill()
	t.pu()

	t.goto(pos[0]+60, pos[1]+20)
	t.pd()
	t.begin_fill()
	t.goto(pos[0]+80, pos[1]+20)
	t.goto(pos[0]+80, pos[1]+40)
	t.goto(pos[0]+60, pos[1]+40)
	t.goto(pos[0]+60, pos[1]+20)
	t.end_fill()
	t.pu()

	t.goto(pos[0]+60, pos[1]+60)
	t.pd()
	t.begin_fill()
	t.goto(pos[0]+80, pos[1]+60)
	t.goto(pos[0]+80, pos[1]+80)
	t.goto(pos[0]+60, pos[1]+80)
	t.goto(pos[0]+60, pos[1]+60)
	t.end_fill()
	t.pu()

	t.goto(pos[0]+20, pos[1]+60)
	t.pd()
	t.begin_fill()
	t.goto(pos[0]+40, pos[1]+60)
	t.goto(pos[0]+40, pos[1]+80)
	t.goto(pos[0]+20, pos[1]+80)
	t.goto(pos[0]+20, pos[1]+60)
	t.end_fill()
	t.pu()
	############







domki(0)
while 1:
	pass