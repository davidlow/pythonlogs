#working example

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
    fig.canvas.draw()
    time.sleep(1)