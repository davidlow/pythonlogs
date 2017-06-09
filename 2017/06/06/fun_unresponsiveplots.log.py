# IPython log file

# Wed, 07 Jun 2017 00:12:01
get_ipython().magic('matplotlib tk')
# Wed, 07 Jun 2017 00:12:15
import numpy as np
# Wed, 07 Jun 2017 00:12:33
plt.ion()
# Wed, 07 Jun 2017 00:12:48
from matplotlib import pyplot as plt
# Wed, 07 Jun 2017 00:12:52
plt.ion()
# Wed, 07 Jun 2017 00:13:03
fig, ax = plt.figure()
# Wed, 07 Jun 2017 00:13:13
fig
# Wed, 07 Jun 2017 00:13:16
ax
# Wed, 07 Jun 2017 00:13:27
plt.close()
# Wed, 07 Jun 2017 00:17:01
fig, ax = plt.subplots()
# Wed, 07 Jun 2017 00:17:17
x = np.linspace(0,1,100)
# Wed, 07 Jun 2017 00:17:32
y = np.sin(x*2*pi)
# Wed, 07 Jun 2017 00:17:35
y = np.sin(x*2*np.pi)
# Wed, 07 Jun 2017 00:19:54
line = ax.plot([],[])
# Wed, 07 Jun 2017 00:19:56
line
#[Out]# [<matplotlib.lines.Line2D at 0x7c5a320>]
# Wed, 07 Jun 2017 00:20:57
line[0]
#[Out]# <matplotlib.lines.Line2D at 0x7c5a320>
# Wed, 07 Jun 2017 00:45:52
l = line[0]
# Wed, 07 Jun 2017 00:46:52
import time
for i in range(len(x)):
    l.set_data(x[i],y[i])
    fig.canvas.draw()
    time.sleep(5)
    
# Wed, 07 Jun 2017 00:47:51
import time
for i in range(len(x)):
    l.set_data(x[i],y[i])
    fig.canvas.draw()
    #time.sleep(5)
# Wed, 07 Jun 2017 00:48:22
ax.hold(True)
# Wed, 07 Jun 2017 00:48:36
plt.show(False)
# Wed, 07 Jun 2017 00:48:40
plt.draw()
# Wed, 07 Jun 2017 00:48:59
l = ax.plot(x[0],y[0],'o')[0]
# Wed, 07 Jun 2017 00:49:26
for i in range(len(x)):
    l.set_data(x[i],y[i])
    fig.canvas.draw()
    #time.sleep(5)
    
# Wed, 07 Jun 2017 00:52:28
y = np.sin(x*2*pi)
# Wed, 07 Jun 2017 00:52:33
plt.close()
# Wed, 07 Jun 2017 00:52:38
plt.ion()
# Wed, 07 Jun 2017 00:52:47
plt.show()
# Wed, 07 Jun 2017 00:53:06
fig,ax = plt.subplots()
# Wed, 07 Jun 2017 00:53:38
l = plt.plot(0,0)[0]
# Wed, 07 Jun 2017 00:53:50
l = plt.plot(0,0,'b')[0]
# Wed, 07 Jun 2017 00:53:55
l = plt.plot(0,0,'b')[0]
# Wed, 07 Jun 2017 00:54:00
plt.ion()
# Wed, 07 Jun 2017 00:54:07
plt.show()
# Wed, 07 Jun 2017 00:54:22
l = plt.plot([0,1],[0,1],'b')[0]
# Wed, 07 Jun 2017 00:54:31
l = plt.plot([0,1],[0,1],'b',marker='o')[0]
# Wed, 07 Jun 2017 00:55:00
np.rand
# Wed, 07 Jun 2017 00:55:01
np.random
#[Out]# <module 'numpy.random' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\random\\__init__.py'>
# Wed, 07 Jun 2017 00:55:04
np.random.random
#[Out]# <function RandomState.random_sample>
# Wed, 07 Jun 2017 00:55:53
l.set_ydata(np.random.random)
# Wed, 07 Jun 2017 00:56:02
l.set_ydata(np.random.random())
# Wed, 07 Jun 2017 00:56:08
l.set_ydata(np.random.random())
# Wed, 07 Jun 2017 00:56:09
l.set_ydata(np.random.random())
# Wed, 07 Jun 2017 00:56:11
l.set_ydata(np.random.random())
