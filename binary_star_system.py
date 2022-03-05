import matplotlib.animation as ani 
import matplotlib.pyplot as plt
import numpy as np

a1, b1=15, 7
a2, b2=14, 6
t=np.linspace(0, 2*np.pi,361)
z=np.linspace(np.pi, 3*np.pi, 361)
x1=a1*np.cos(z)-10
y1=b1*np.sin(z)
x2=a1*np.cos(t)+10
y2=b1*np.sin(t)

fig=plt.figure()
ax=plt.axes(xlim=(-30,30), ylim=(-30,30))
s1, =ax.plot(-25,0,marker='o', markersize=35,markerfacecolor='red')
s1_o, =ax.plot(-25,0, color='gold')
s2, =ax.plot(24,0, marker='o', markersize=33,markerfacecolor='blue')
s2_o, =ax.plot(24,0, color='lime')

def binary_star(i):
  s1.set_data(x1[i], y1[i])
  s1_o.set_data(x1[:i], y1[:i])
  s2.set_data(x2[i], y2[i])
  s2_o.set_data(x2[:i], y2[:i])
  return s1, s2, s1_o, s2_o, 

"""Speed of animation governs by:
Frames-Stations
Interval-Number of milliseconds train remains at station
"""
anim=ani.FuncAnimation(fig, binary_star, frames=len(t), interval= 10,blit=True, repeat=True)

fig.patch.set_facecolor('k')
fig.suptitle("Binary Star System")
plt.axis(False)
#plt.rcParams["animation.ffmpeg_path"]= r'C:/ffmpeg/bin/ffmpeg.exe' 
#writervideo = ani.FFMpegWriter(fps=20, metadata={"Artist":"Rishikesh Jha"},bitrate=10000) 
#anim.save("Binary Star System.mp4", writer=writervideo)
plt.show()
  
