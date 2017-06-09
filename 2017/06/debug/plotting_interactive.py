import matplotlib
matplotlib.use("qt5agg")
import matplotlib.pyplot as plt
import multiprocessing as mp
import random
import numpy
import time

def worker(q):
    plt.ion()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ln = ax.plot([], [],'b',marker='o')[0]
    fig.canvas.draw()   # draw and show it
    plt.show(block=False)
    #plt.show()

    while True:
        try:
            obj = q.get_nowait()
        except:
            time.sleep(1);
            continue;
        n = obj + 0
        print("sub : got:", n)

        ln.set_xdata(numpy.append(ln.get_xdata(), n))
        ln.set_ydata(numpy.append(ln.get_ydata(), n))
        ax.relim()

        ax.autoscale_view(True,True,True)
        plt.pause(0.1)
        fig.canvas.draw()

#if __name__ == '__main__':
def f():
    queue = mp.Queue()
    p = mp.Process(target=worker, args=(queue,))
    p.start()

    while True:
        n = random.random() * 5
        print("main: put:", n)
        queue.put(n)
        time.sleep(1.0)

# works from cli

# works from ipython run.  
# does not show the worker print statements