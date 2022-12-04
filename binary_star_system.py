import matplotlib.animation as ani 
import matplotlib.pyplot as plt
import numpy as np


theta=-np.pi/4
m1, m2 = 1, 5
a1, b1 = 15, 10
a2, b2 = 8, 4
t1 = np.linspace(np.pi, 3*np.pi, 361)
t2 = np.linspace(0, 2*np.pi,361)
x1 = a1*np.cos(t1)-10
y1 = b1*np.sin(t1)
x2 = a2*np.cos(t2)+8
y2 = b2*np.sin(t2)
x3 = ((m1*x1) + (m2*x2))/(m1+m2)
y3 = ((m1*y1) + (m2*y2))/(m1+m2)


"""
Applying Rotational Transformation Equations:
    If x',y' axes are rotating about z' axis and x,y,z are the axes of a non-rotating frame then 
    (x', y', z')=(xcos(t)+ysin(t), -xsin(t)+ycos(t), z)
"""
x1_p = x1*np.cos(theta)+y1*np.sin(theta)
y1_p = -x1*np.sin(theta)+y1*np.cos(theta)
x2_p = x2*np.cos(theta)+y2*np.sin(theta)
y2_p = -x2*np.sin(theta)+y2*np.cos(theta)
x3_p = x3*np.cos(theta)+y3*np.sin(theta)
y3_p = -x3*np.sin(theta)+y3*np.cos(theta)


fig = plt.figure()
ax = plt.axes(xlim=(-30,30), ylim=(-30,30))
s1, = ax.plot(x1_p[0], y1_p[0], marker='o', markersize=30, markerfacecolor='red')
s1_o, = ax.plot(x1_p[0], y1_p[0], color='lime', lw=2)
s2, = ax.plot(x2_p[0], y2_p[0], marker='o', markersize=40, markerfacecolor='blue')
s2_o, = ax.plot(x2_p[0], y2_p[0], color='lime', lw=2)
bc, = ax.plot(x3_p[0],y3_p[0], marker='.', markersize=15, markerfacecolor='brown', label="Barycenter")
bc_o, = ax.plot(x3_p[0],y3_p[0], linestyle="--",color="gold", lw=1.5)


def binary_star(i):
  s1.set_data(x1_p[i], y1_p[i])
  s1_o.set_data(x1_p[:i], y1_p[:i])                          
  s2.set_data(x2_p[i], y2_p[i])
  s2_o.set_data(x2_p[:i], y2_p[:i])                           
  bc.set_data(x3_p[i], y3_p[i]) 
  bc_o.set_data(x3_p[:i], y3_p[:i])                     
  return s1, s2, s1_o, s2_o, bc, bc_o,


"""
Speed of animation governs by:
    1. Frames-Stations
    2. Interval-Number of milliseconds train remains at station
"""
anim=ani.FuncAnimation(fig, binary_star, frames=len(t1), interval= 20, blit=True, repeat=True)


fig.patch.set_facecolor('k')
fig.suptitle("Binary Star System when m2 = 5m1", color="fuchsia")
plt.axis(False)
#plt.rcParams["animation.ffmpeg_path"]= r'C:/ffmpeg/bin/ffmpeg.exe' 
#writervideo = ani.FFMpegWriter(fps=20, metadata={"Artist":"Rishikesh Jha"},bitrate=10000) 
#anim.save("Binary Star System.mp4", writer=writervideo)
plt.legend(loc="best")
plt.annotate("Courtesy Rishikesh Jha", (27,-29), color="fuchsia")
plt.show()
