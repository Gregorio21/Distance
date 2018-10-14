import serial
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw,ion
import matplotlib.animation as animation
from matplotlib import style
import statistics
global smoothy,smoothx
mydatax = list()
mydatay = list()
smoothx = list()
smoothy = list()
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
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
def animate(i):
        global smoothx,smoothy
        data = str(arduino.readline())
        print(data)
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
                  mydatay.append(float( data))
        except:
            print("Bad data point")
        smoothx = smooth(mydatax[-100:], 10)
        smoothy = smooth(mydatay[-100:], 10)
        ax1.clear()
        smoothx = smoothx[-90:]
        smoothy = smoothy[-90:]
        ax1.set_xlim(3,20)
        ax1.set_ylim(3,20)
        ax1.scatter(smoothy[0:len(smoothx)], smoothx[0:len(smoothy)])
        


try:
    arduino = serial.Serial("COM3", baudrate = 250000, timeout = 1)
except:
    print("invalid port")

ani = animation.FuncAnimation(fig, animate, interval=10, save_count = 200)
plt.show()

        

