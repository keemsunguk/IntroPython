
from tkinter import *
import math
import time

####################################
# customize these functions
####################################
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    data.r = min(data.width, data.height)/3
    data.cx = data.width/2
    data.cy = data.height/2
    data.x0 = data.cx - data.r
    data.y0 = data.cy - data.r
    data.x1 = data.cx + data.r
    data.y1 = data.cy + data.r
    data.mrg = 5

    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    h = time.localtime().tm_hour
    m = time.localtime().tm_min

    canvas.create_rectangle(data.x0-data.mrg, data.y0-data.mrg, data.x1+data.mrg, data.y1+data.mrg, outline="black", width=1, fill=rgbString(23,200, 231))
    drawClock(canvas, data.x0, data.y0, data.x1, data.y1, data.r, h, m)

    pass

def drawClock(canvas, x0, y0, x1, y1, r, hour, minute):

    # find relevant values for positioning clock
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2

    # draw the clock face
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", 
                        width=2, fill="yellow")
    r *= 0.85 # make smaller so time labels lie inside clock face
    for hr in range(12):
        hourAngle = math.pi/2 - (2*math.pi)*(hr/12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)
        label = str(hr if (hr > 0) else 12)
        canvas.create_text(hourX, hourY, text=label, font="Arial 16 bold")
        
    # adjust the hour to take the minutes into account
    hour += minute/60.0

    # find the hourAngle and draw the hour hand
    # but we must adjust because 0 is vertical and
    # it proceeds clockwise, not counter-clockwise!
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill="black", width=1)

    # repeat with the minuteAngle for the minuteHand
    minuteAngle = math.pi/2 - 2*math.pi*minute/60
    minuteRadius = r*9/10
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle) 
    canvas.create_line(cx, cy, minuteX, minuteY, fill="black", width=1)
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

run(400, 200)