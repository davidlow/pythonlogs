import matplotlib.pyplot as plt
import numpy as np
import datetime

plt.ion()

temperatures = []
heateroutputs = []
times = []
setpoints = []
for i in range(3):
    temperatures.append(lakeshore.chan6.T)
    setpoints.append(lakeshore.pid_setpoint)
    heateroutputs.append(float(lakeshore.ask('HTR?')))
    times.append(datetime.datetime.now())

fig = plt.figure()
ax_h = fig.add_subplot(211)
ax_t = fig.add_subplot(212, sharex=ax_h)


holine = ax_h.plot(times, heateroutputs, label='heater out (%)')[0] 
tsline = ax_t.plot(times, temperatures, label='temperature (K)')[0]
tpline = ax_t.plot(times, setpoints, label='setpoint (K)')[0]

fig.autofmt_xdate()
ax_h.autoscale(enable=True, axis='both')
ax_t.autoscale(enable=True, axis='both')

ax_t.set_xlabel('Time')
ax_t.set_ylabel('Temperature (K)')
ax_h.set_ylabel('Heater output (%)')

def do():
    while True:
        try:

            temperatures.append(lakeshore.chan6.T)
            setpoints.append(lakeshore.pid_setpoint)
            heateroutputs.append(float(lakeshore.ask('HTR?')))
            times.append(datetime.datetime.now())
            #print(len(temperatures), 
            #      len(setpoints), len(heateroutputs), len(times))

            plt.pause(.1)
            holine.set_xdata(times)
            holine.set_ydata(heateroutputs)
            tsline.set_xdata(times)
            tsline.set_ydata(temperatures)
            tpline.set_xdata(times)
            tpline.set_ydata(setpoints)
            ax_h.relim()
            ax_h.autoscale_view(True,True,True)
            ax_t.relim()
            ax_t.autoscale_view(True,True,True)

            fig.canvas.draw()
        except KeyboardInterrupt:
            print("User Escape")
            break
