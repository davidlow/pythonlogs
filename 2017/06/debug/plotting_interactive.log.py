# IPython log file

# Thu, 08 Jun 2017 01:03:04
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

while True:
    plt.pause(0.05)
    
# Thu, 08 Jun 2017 01:03:29
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)
    
# Thu, 08 Jun 2017 01:03:44
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.01)
    
# Thu, 08 Jun 2017 01:04:08
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:04:27
plt.clear()
# Thu, 08 Jun 2017 01:04:30
plt.cla()
# Thu, 08 Jun 2017 01:04:38
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:06:20
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

for i in range(10):
    y = np.random.random()
    ax.plot(i,y);
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:07:40
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[]);
ys = [];
is = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    is.append(i);
    l.set_xdata(is);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
# Thu, 08 Jun 2017 01:08:00
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[]);
ys = [];
is = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    is.append(i);
    l.set_xdata(is);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
# Thu, 08 Jun 2017 01:08:23
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[])[0];
ys = [];
is = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    is.append(i);
    l.set_xdata(is);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
# Thu, 08 Jun 2017 01:08:31
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[])[0];
ys = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    is.append(i);
    l.set_xdata(is);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
# Thu, 08 Jun 2017 01:08:49
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[])[0];
ys = [];
ms = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    is.append(i);
    l.set_xdata(ms);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
# Thu, 08 Jun 2017 01:09:06
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[])[0];
ys = [];
ms = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    ms.append(i);
    l.set_xdata(ms);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:09:40
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[],'b',marker='o')[0];
ys = [];
ms = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    ms.append(i);
    l.set_xdata(ms);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:10:50
import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

fig,ax = plt.subplots();

l = ax.plot([],[],'b',marker='o')[0];
ax.set_xlim([0,10])
ax.set_ylim([0,1])

ys = [];
ms = [];
for i in range(10):
    y = np.random.random()
    ys.append(y);
    ms.append(i);
    l.set_xdata(ms);
    l.set_ydata(ys);
    plt.pause(0.01)
    time.sleep(1)
    
# Thu, 08 Jun 2017 01:18:47
10*4*10/60
#[Out]# 6.666666666666667
# Thu, 08 Jun 2017 01:34:45
get_ipython().magic('load 06/debug/plotting_interactive4.py')
# Thu, 08 Jun 2017 01:34:46
# %load 06/debug/plotting_interactive4.py
#a slight modification of your code using multiprocessing
import matplotlib
matplotlib.use("qt4agg")
import matplotlib.pyplot as plt 
#import threading
#let's try using multiprocessing instead of threading module:
import multiprocessing
import time

#we'll keep the same plotting function, except for one change--I'm going to use the multiprocessing module to report the plotting of the graph from the child process (on another core):
def plot_a_graph():
    f,a = plt.subplots(1)
    line = plt.plot(range(10))
    print multiprocessing.current_process().name,"starting plot show process" #print statement preceded by true process name
    plt.show() #I think the code in the child will stop here until the graph is closed
    print multiprocessing.current_process().name,"plotted graph" #print statement preceded by true process name
    time.sleep(4)

#use the multiprocessing module to perform the plotting activity in another process (i.e., on another core):
job_for_another_core = multiprocessing.Process(target=plot_a_graph,args=())
job_for_another_core.start()

#the follow print statement will also be modified to demonstrate that it comes from the parent process, and should happen without substantial delay as another process performs the plotting operation:
print multiprocessing.current_process().name, "The main process is continuing while another process deals with plotting."
# Thu, 08 Jun 2017 01:35:18
get_ipython().magic('load 06/debug/plotting_interactive4.py')
# Thu, 08 Jun 2017 01:35:19
# %load 06/debug/plotting_interactive4.py
#a slight modification of your code using multiprocessing
import matplotlib
matplotlib.use("qt4agg")
import matplotlib.pyplot as plt 
#import threading
#let's try using multiprocessing instead of threading module:
import multiprocessing
import time

#we'll keep the same plotting function, except for one change--I'm going to use the multiprocessing module to report the plotting of the graph from the child process (on another core):
def plot_a_graph():
    f,a = plt.subplots(1)
    line = plt.plot(range(10))
    print(multiprocessing.current_process().name,"starting plot show process") #print statement preceded by true process name
    plt.show() #I think the code in the child will stop here until the graph is closed
    print(multiprocessing.current_process().name,"plotted graph")#print statement preceded by true process name
    time.sleep(4)

#use the multiprocessing module to perform the plotting activity in another process (i.e., on another core):
job_for_another_core = multiprocessing.Process(target=plot_a_graph,args=())
job_for_another_core.start()

#the follow print statement will also be modified to demonstrate that it comes from the parent process, and should happen without substantial delay as another process performs the plotting operation:
print(multiprocessing.current_process().name, "The main process is continuing while another process deals with plotting.")

