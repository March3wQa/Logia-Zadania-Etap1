import turtle
import math

t = turtle.Turtle()
t.pu()
t.goto(-300, 225)

def height(a):
    return (a*math.sqrt(3))/2

def shapes(self, shape):
    if shape == 'sqr-b':
        self.pd()
        self.fillcolor('blue')
        self.begin_fill()
        for _ in range(4):
            self.fd(30)
            self.lt(90)
        self.end_fill()
        self.pu()
    if shape == 'sqr-g':
        self.pd()
        self.fillcolor('green')
        self.begin_fill()
        for _ in range(4):
            self.fd(30)
            self.lt(90)
        self.end_fill()
        self.pu()
    if shape == 'trg':
        self.pd()
        self.fillcolor('yellow')
        self.begin_fill()
        for _ in range(3):
            self.fd(30)
            self.lt(120)
        self.end_fill()
        self.pu()

def structures(self, structure):
    if structure == 'hor':
        shapes(self, 'sqr-g')
        self.fd(30)
        shapes(self, 'sqr-g')
        self.bk(30)
        self.lt(90)
        self.fd(30)
        self.rt(90)
        shapes(self, 'trg')
        self.fd(30)
        shapes(self, 'trg')
        self.lt(60)
        self.fd(30)
        self.rt(120)
        shapes(self, 'sqr-b')
        self.fd(30)
        self.rt(30)
        shapes(self, 'trg')
        self.fd(30)
        self.lt(90)
        self.bk(60)
    if structure == 'ver':
        shapes(self, 'sqr-g')
        self.lt(90)
        self.fd(30)
        self.rt(90)
        shapes(self, 'sqr-g')
        self.fd(30)
        self.rt(90)
        shapes(self, 'trg')
        self.bk(30)
        shapes(self, 'trg')
        self.lt(60)
        shapes(self, 'sqr-b')
        self.lt(30)
        self.bk(30)
        shapes(self, 'trg')
        self.rt(90)
        self.fd(60)
        self.lt(90)

def row(self, x, other = False):
    if other == False:
        for _ in range(x):
            structures(self, 'hor')
            self.fd(15)
            self.rt(90)
            self.fd(2*30 + height(30))
            self.lt(90)
            structures(self, 'ver')
            self.rt(90)
            self.fd(30 + height(30))
            self.lt(90)
            self.bk(15)
    if other == True:
        for _ in range(x):
            structures(self, 'ver')
            self.rt(90)
            self.fd(30 + height(30))
            self.lt(90)
            self.bk(15)
            structures(self, 'hor')
            self.fd(15)
            self.rt(90)
            self.fd(2*30 + height(30))
            self.lt(90)

t.row = row

def parkiet():
    for _ in range(3):
        t.row(t, 3)
        t.lt(90)
        t.fd(9*30 + 6*height(30) + 15)
        t.rt(90)
        t.fd(2*30 + height(30))
        t.rt(90)
        t.fd(30)
        t.lt(90)
        t.row(t, 3, True)
        t.lt(90)
        t.fd(9*30 + 6*height(30) + 15)
        t.rt(90)
        t.fd(30 + height(30))

parkiet()