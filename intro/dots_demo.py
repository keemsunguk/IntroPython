######################################################
# Struct Example:  dotsDemo
######################################################

import random
#from structClass import Struct # defined above (saved in structClass.py)
from tkinter import *

class Dot(object):
    def __init__(self, x, y, clickCount=0):
        self.x = x
        self.y = y
        self.r = random.randint(20,60)
        self.fill = random.choice(['pink', 'orange', 'yellow','green','cyan','purple'])
        self.click_count = clickCount

    def dotContainsPoint(self, dot, x, y):
        d = ((dot.x - x)**2 + (dot.y - y)**2)**0.5
        return (d <= dot.r)

    def draw(self, canvas):
#        print(self.x, self.y, self.fill)
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = self.fill)
        canvas.create_text(self.x, self.y, text=str(self.click_count))


def init(data):
    data.dots = []

def mousePressed(event, data):
    for dot in reversed(data.dots):
        if (dot.dotContainsPoint(dot, event.x, event.y)):
            dot.click_count += 1
            print(dot.click_count)
            return

    data.dots.append(Dot(x=event.x, y=event.y, clickCount=0))

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.draw(canvas)
def keyPressed(event, data):
    pass

def timerFired(data):
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)