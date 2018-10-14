import serial
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw,ion
import matplotlib.animation as animation
from matplotlib import style,patches,colors
import statistics
import math
global smoothy,smoothx
mydatax = list()
mydatay = list()
smoothx = list()
smoothy = list()
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)
ax3 = fig.add_subplot(1,1,1)
ax4 = fig.add_subplot(1,1,1)
rectangle = patches.Rectangle((18,18),8,8,fill=False,linewidth = 2.0,edgecolor='r')

def scoreRectangle(x,y,h,w):
    global smoothx,smoothy
    sx = smoothx
    sy = smoothy
    for i in range(1,89):
        dx = max(abs(sx[i] - (x+w/2)) - w / 2, 0)
        dy = max(abs(sy[i] - (y+h/2)) - h / 2, 0)
    return math.sqrt(dx * dx + dy * dy)*10

def smooth(data, window):
    count = 0
    size = len(data)
    smoothed = []
    while(count < size-window):
        
        sub = data[count:count+window]
        sub.sort()
        if sub != None:
            smoothed.append(statistics.median(sub))
        prev = count
        count += 1
      
    return smoothed
def getData():
        global smoothx,smoothy
        data = None
        while(arduino.inWaiting() > 0):
            data = str(arduino.readline())
            data = data.replace("\\","")
            data = data.replace("\'", "")
            data = re.sub('[brn]', '', data)
            size = len(data)
            data = data.replace("x", "")
            try:
                if size > len(data):
                    if len(data) != 0:
                      mydatax.append(float(data))
                      
                else:
                  
                  data = data.replace("y", "")
                  if len(data) != 0:
                      mydatay.append(float(data))
                      
            except:
                print("Bad data point")
        return data
    
def animate(i):
        global smoothx,smoothy
        score = 0
        getData()
        smoothx = smooth(mydatax[-100:], 10)
        smoothy = smooth(mydatay[-100:], 10)
        ax1.clear()
        smoothx = smoothx[-90:]
        smoothy = smoothy[-90:]
        ax1.set_xlim(0,60)
        ax1.set_ylim(0,60)
        if(len(smoothx) >= 90 and len(smoothy) >= 90):
            score = scoreRectangle(18,18,8,8)
        fig.suptitle("score %d" % score)
        ax1.scatter(smoothy[0:len(smoothx)], smoothx[0:len(smoothy)])
        ax2.plot(smoothx)
        ax3.plot(smoothy)
        ax4.add_patch(rectangle)
        

try:
    arduino = serial.Serial("COM3", baudrate = 250000, timeout = 1)
except:
    print("invalid port")

ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()

        

