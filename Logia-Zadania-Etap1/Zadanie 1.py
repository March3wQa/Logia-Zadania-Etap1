### IMPORT ###
import turtle
##############

def domki(n):
	try:
		if n<2 or n>7:
			raise ValueError('Błędna liczba. Akceptowane liczby to od 2 do 7.')
	except ValueError as err:
		print(err)
		return(err)
	else:
		### INIT ###
		iteration = 0
		pos = [-(100*n)/2, 0]
		t = turtle.Turtle()
		t.pu()
		############

		for _ in range(n):
			### FASADA ###
			t.goto(pos)
			t.fillcolor('yellow')
			t.pd()
			t.begin_fill()
			t.goto(pos[0]+100, pos[1])
			t.goto(pos[0]+100, pos[1]+100)
			t.goto(pos[0], pos[1]+100)
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

			### DACH ###
			t.fillcolor('red')
			t.goto(pos[0], pos[1]+100)
			t.pd()
			t.begin_fill()
			t.goto(pos[0]+100, pos[1]+100)
			t.goto(pos[0]+140, pos[1]+140)
			t.goto(pos[0]+40, pos[1]+140)
			t.goto(pos[0], pos[1]+100)
			t.end_fill()
			t.pu()
			############

			### ŚCIANA ###
			t.fillcolor('gray')
			t.goto(pos[0]+100, pos[1])
			t.pd()
			t.begin_fill()
			t.goto(pos[0]+140, pos[1]+40)
			t.goto(pos[0]+140, pos[1]+140)
			t.goto(pos[0]+100, pos[1]+100)
			t.goto(pos[0]+100, pos[1])
			t.end_fill()
			t.pu()
			##############

			### ZMIANA ###
			pos = [t.xcor(), t.ycor()]
			if iteration == 0:
				pos = [pos[0]+40, pos[1]+40]
				iteration = 1
			else:
				pos = [pos[0]-40, pos[1]-40]
				iteration = 0
			##############