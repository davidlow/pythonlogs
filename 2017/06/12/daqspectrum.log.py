# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Tue, 13 Jun 2017 00:05:47
get_ipython().magic('load qtconsole/2017/06/setups/main_20170608.py')
# Tue, 13 Jun 2017 00:05:57
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
# pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Tue, 13 Jun 2017 00:10:07
get_ipython().magic('load qtconsole/2017/06/setups/setup_20170606.py')
# Tue, 13 Jun 2017 00:10:29
# %load qtconsole/2017/06/setups/setup_20170606.py
### Setup script, modified from gmf57.  
###
###  +-----------------+
###  |  DO NOT MODIFY  |
###  +-----------------+
###
### Make a copy and rename with today's date
###
### Author: david low (dhl88)

from matplotlib import pyplot as plt
plt.ion()
#plt.style.use("notebook")
from Nowack_Lab.Instruments import NIDAQ, SR830, SR5113, Piezos, Montana, Attocube, SquidArray
from Nowack_Lab.Procedures import Planefit

# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")
daq.outputs = {
    'x':0,
    'y':1,
    'z':2
}
daq.inputs = {
    'cap':0,
    'theta':1,
    'capx':2, # disconnected
    'capy':3, # disconnected
    'acx':4,
    'acy':5,
    'dc':6
}

# Initialize other measurement equipment
pa = SR5113(port="COM3")
liC = SR830(gpib_address=12)
liS = SR830(gpib_address=13)
pz = Piezos(daq)
montana = Montana()
atto = Attocube(montana)

s = SquidArray(visaResource='COM1')

# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
    'montana':montana,
    'piezos':pz,
    'lockin_cap':liC,
    'atto': atto,
    'preamp': pa,
    'lockin_squid': liS,
    'squidarray': s
}

# Tue, 13 Jun 2017 00:10:37
s.tune()
# Tue, 13 Jun 2017 00:10:49
s.tune()
# Tue, 13 Jun 2017 00:11:49
s.sensitivity = 'Med'
# Tue, 13 Jun 2017 00:11:55
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xf918ac8>
# Tue, 13 Jun 2017 00:11:58
pa.gain
#[Out]# 1
# Tue, 13 Jun 2017 00:12:03
pa.gain=2
# Tue, 13 Jun 2017 00:12:05
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xf918ac8>
# Tue, 13 Jun 2017 00:12:06
pa.gain
#[Out]# 2
# Tue, 13 Jun 2017 00:12:09
pa.gain=1
# Tue, 13 Jun 2017 00:13:59
pa.filter
#[Out]# (1, 100000)
# Tue, 13 Jun 2017 00:14:43
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:14:59
CAP_I = instruments['lockin_cap'].R
# Tue, 13 Jun 2017 00:15:01
CAP_I
#[Out]# 1.00211e-06
# Tue, 13 Jun 2017 00:15:05
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:15:17
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''baseline, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 00:17:48
pa.gain=2
# Tue, 13 Jun 2017 00:17:55
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''baseline, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 00:19:22
pa.gain=10
# Tue, 13 Jun 2017 00:19:37
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''baseline, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 00:22:26
pa.gain
#[Out]# 100
# Tue, 13 Jun 2017 00:22:32
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''baseline, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 00:24:46
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''baseline, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 00:29:45
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:35:15
pa.filter
#[Out]# (1, 100000)
# Tue, 13 Jun 2017 00:35:23
pa.filter = (1,1e5)
# Tue, 13 Jun 2017 00:35:25
pa.filter
#[Out]# (1, 100000)
# Tue, 13 Jun 2017 00:35:40
pa.filter
#[Out]# (1, 10000)
# Tue, 13 Jun 2017 00:35:55
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:37:56
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:41:14
pa.gain=1
# Tue, 13 Jun 2017 00:41:22
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 00:45:32
pa.filter=(1,1000)
# Tue, 13 Jun 2017 00:45:34
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 15:47:21
pa.__getstate__()
#[Out]# {'filter': (1, 1000), 'gain': 1}
# Tue, 13 Jun 2017 15:47:56
spectrum
#[Out]# <Nowack_Lab.Procedures.daqspectrum.SQUIDSpectrum at 0x110c0d68>
# Tue, 13 Jun 2017 15:48:10
fig,ax = plt.subplots()
# Tue, 13 Jun 2017 15:48:47
ax.plot(spectrum.V)
#[Out]# [<matplotlib.lines.Line2D at 0x1101ce80>]
# Tue, 13 Jun 2017 15:53:33
v = spectrum.V
# Tue, 13 Jun 2017 15:53:34
v
#[Out]# array([-0.01186078, -0.006063  , -0.01057238, ..., -0.0070293 ,
#[Out]#        -0.00992819, -0.00799559])
# Tue, 13 Jun 2017 15:54:36
np
#[Out]# <module 'numpy' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\__init__.py'>
# Tue, 13 Jun 2017 15:54:48
h = np.histogram(v,int(2**16))
# Tue, 13 Jun 2017 15:54:58
fig,ax = plt.subplots()
# Tue, 13 Jun 2017 15:55:02
ax.plot(h)
# Tue, 13 Jun 2017 15:55:22
[h, edges] = np.histogram(v,int(2**16))
# Tue, 13 Jun 2017 15:55:23
h
#[Out]# array([1, 0, 0, ..., 0, 0, 2], dtype=int64)
# Tue, 13 Jun 2017 15:55:26
edges
#[Out]# array([-0.01862486, -0.01862458, -0.01862431, ..., -0.00058787,
#[Out]#        -0.00058759, -0.00058732])
# Tue, 13 Jun 2017 15:55:48
ax.plot(edges,h)
# Tue, 13 Jun 2017 15:56:24
ax.plot(h)
#[Out]# [<matplotlib.lines.Line2D at 0x6317470>]
# Tue, 13 Jun 2017 15:57:40
ax.plot(edges,h[0:-1])
# Tue, 13 Jun 2017 15:58:49
ax.plot(edges[0:-1],h)
#[Out]# [<matplotlib.lines.Line2D at 0x1148de80>]
# Tue, 13 Jun 2017 15:58:58
fig,ax = plt.subplots()
# Tue, 13 Jun 2017 15:59:02
ax.plot(edges[0:-1],h)
#[Out]# [<matplotlib.lines.Line2D at 0x1112b9b0>]
# Tue, 13 Jun 2017 16:00:00
.00928384 - 00896211
# Tue, 13 Jun 2017 16:00:04
.00928384 - .00896211
#[Out]# 0.00032172999999999924
# Tue, 13 Jun 2017 16:06:46
.00928398 - .00896197
#[Out]# 0.00032201000000000105
# Tue, 13 Jun 2017 16:08:28
pa.gain=500
# Tue, 13 Jun 2017 16:08:59
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 16:12:16
get_ipython().magic('run -i qtconsole/2017/06/analyze/daqspectrum_daqsteps.py')
# Tue, 13 Jun 2017 16:12:25
get_ipython().magic('run -i qtconsole/2017/06/analyze/daqspectrum_daqsteps.py')
# Tue, 13 Jun 2017 16:12:44
get_ipython().magic('run -i qtconsole/2017/06/analyze/daqspectrum_daqsteps.py')
# Tue, 13 Jun 2017 16:13:07
get_ipython().magic('load qtconsole/2017/06/analyze/daqspectrum_daqsteps.py')
# Tue, 13 Jun 2017 16:13:10
# %load qtconsole/2017/06/analyze/daqspectrum_daqsteps.py
v = spectrum.V;
[h,edges] = np.histogram(v,int(2**16));
[fig,ax] = plt.subplots();
ax.plot(edges[0:-1],h)

#[Out]# [<matplotlib.lines.Line2D at 0x11174d30>]
# Tue, 13 Jun 2017 16:14:21
ax.set_ylabel('num occurence')
#[Out]# <matplotlib.text.Text at 0x12185908>
# Tue, 13 Jun 2017 16:14:27
ax.set_xlabel('V')
#[Out]# <matplotlib.text.Text at 0x1217e828>
# Tue, 13 Jun 2017 16:15:50
.00466084 - .00466151
#[Out]# -6.699999999994904e-07
# Tue, 13 Jun 2017 16:15:58
(.00466084 - .00466151)*500
#[Out]# -0.0003349999999997452
# Tue, 13 Jun 2017 16:34:01
s.sensitivity='high'
# Tue, 13 Jun 2017 16:41:10
get_ipython().magic('run -i qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 16:45:14
s.unlock
#[Out]# <bound method PFL102.unlock of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CF64908>>
# Tue, 13 Jun 2017 16:45:18
s.unlock()
# Tue, 13 Jun 2017 16:45:23
s.sensitivity = 'Med
# Tue, 13 Jun 2017 16:45:24
s.sensitivity = 'Med'
# Tue, 13 Jun 2017 16:45:32
s.__getstate__()
#[Out]# {'Array bias': 43.0,
#[Out]#  'Array flux': 15.0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 450.0,
#[Out]#  'SQUID flux': 8.0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Auto',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Tue, 13 Jun 2017 16:45:47
s.testSignal = 'On'
# Tue, 13 Jun 2017 16:46:22
s.S_bias = 0
# Tue, 13 Jun 2017 16:46:25
s.reset()
# Tue, 13 Jun 2017 16:46:42
s.testInput = 'A_flux'
# Tue, 13 Jun 2017 16:49:11
s.A_bias = 0
# Tue, 13 Jun 2017 16:49:15
s.A_bias = 43
# Tue, 13 Jun 2017 16:49:22
s.A_flux = 0
# Tue, 13 Jun 2017 16:49:25
s.A_flux = 5
# Tue, 13 Jun 2017 16:49:40
s.A_flux = 6
# Tue, 13 Jun 2017 16:49:42
s.A_flux = 7
# Tue, 13 Jun 2017 16:49:57
s.lock('Array')
# Tue, 13 Jun 2017 16:50:02
s.reset()
# Tue, 13 Jun 2017 16:50:52
s.reset()
# Tue, 13 Jun 2017 16:53:00
s.unlock()
# Tue, 13 Jun 2017 16:58:48
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 7,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 8.0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Tue, 13 Jun 2017 16:59:54
1.55/10e3
#[Out]# 0.000155
# Tue, 13 Jun 2017 17:00:12
5*495
#[Out]# 2475
# Tue, 13 Jun 2017 17:00:29
5*310
#[Out]# 1550
# Tue, 13 Jun 2017 17:03:58
s.A_bias = 0
# Tue, 13 Jun 2017 17:04:01
s.A_bias = 43
# Tue, 13 Jun 2017 17:04:08
s.A_flux = 0
# Tue, 13 Jun 2017 17:04:11
s.A_flux = 1
# Tue, 13 Jun 2017 17:04:13
s.A_flux = 2
# Tue, 13 Jun 2017 17:04:16
s.A_flux = 3
# Tue, 13 Jun 2017 17:04:18
s.A_flux = 10
# Tue, 13 Jun 2017 17:04:22
s.A_flux = 9
# Tue, 13 Jun 2017 17:04:25
s.A_flux = 8
# Tue, 13 Jun 2017 17:04:28
s.A_flux = 7
# Tue, 13 Jun 2017 17:04:32
s.A_flux = 7.5
# Tue, 13 Jun 2017 17:04:37
s.A_flux = 78
# Tue, 13 Jun 2017 17:04:45
s.A_flux = 8
# Tue, 13 Jun 2017 17:04:51
s.A_flux = 8.5
# Tue, 13 Jun 2017 17:04:55
s.A_flux = 7.5
# Tue, 13 Jun 2017 17:04:59
s.A_flux = 7.0
# Tue, 13 Jun 2017 17:05:08
s.A_flux = 8
# Tue, 13 Jun 2017 17:07:55
s.sensitivity
#[Out]# 'Med'
# Tue, 13 Jun 2017 17:08:01
s.sensitivity = 'High'
# Tue, 13 Jun 2017 17:12:07
s.sensitivity = 'Med'
# Tue, 13 Jun 2017 17:12:14
s.sensitivity = 'low'
# Tue, 13 Jun 2017 17:12:19
s.sensitivity = 'med'
# Tue, 13 Jun 2017 17:12:22
s.sensitivity = 'high'
# Tue, 13 Jun 2017 17:22:48
s.lock('array')
# Tue, 13 Jun 2017 17:22:51
s.reset
#[Out]# <bound method PFL102.reset of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CF64908>>
# Tue, 13 Jun 2017 17:22:56
s.reset()
# Tue, 13 Jun 2017 17:22:58
s.reset()
# Tue, 13 Jun 2017 17:22:59
s.reset()
# Tue, 13 Jun 2017 17:23:13
s.testSignal = 'off'
# Tue, 13 Jun 2017 17:23:18
s.testSignal = 'Off'
# Tue, 13 Jun 2017 17:23:27
s.reset()
# Tue, 13 Jun 2017 17:23:33
s.testSignal = 'On'
# Tue, 13 Jun 2017 17:23:47
s.testSignal = 'Off'
# Tue, 13 Jun 2017 17:23:57
s.A_flux = 0
# Tue, 13 Jun 2017 17:24:06
s.A_flux = 5
# Tue, 13 Jun 2017 17:24:33
s.A_flux = 6
# Tue, 13 Jun 2017 17:24:37
s.A_flux = 5.5
# Tue, 13 Jun 2017 17:25:15
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 17:25:49
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''array locked, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 17:28:33
s.sensitivity
#[Out]# 'High'
# Tue, 13 Jun 2017 17:29:17
s.heat(t_heat=.1,t_cool=60*10)
# Tue, 13 Jun 2017 17:43:48
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''array locked, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1]
);
spectrum.run()

# Tue, 13 Jun 2017 17:51:39
s.lock
#[Out]# <bound method PFL102.lock of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CF64908>>
# Tue, 13 Jun 2017 17:51:52
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 5.5,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 8.0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 17:52:08
s.sensitivity
#[Out]# 'High'
# Tue, 13 Jun 2017 17:56:02
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 17:56:03
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = SQUIDSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
[time, averages] = [{7:f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:f}, {10:f}, {11:f}, {12:f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity']
);
spectrum.run()

# Tue, 13 Jun 2017 17:59:29
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 17:59:39
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:e}, c0={4:e}
[gain, filter f] = [{5:d}, {6:d}]
[time, averages] = [{7:f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 18:00:35
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 18:00:42
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, [x,y,z] = [{0:d},{1:d},{2:d}]
c={3:2.2e}, c0={4:2.2e}
[gain, filter f] = [{5:d}, {6:d}]
[time, averages] = [{7:f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           pa.gain,
           pa.filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 18:02:09
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 18:02:20
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:d}]
[time, averages] = [{7:f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 18:03:13
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 18:03:22
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 18:08:57
s.sensitivity = 'Med'
# Tue, 13 Jun 2017 18:09:02
s.reset ()
# Tue, 13 Jun 2017 18:09:17
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 18:13:00
s.sensitivity = 'Low'
# Tue, 13 Jun 2017 18:13:03
s.reset()
# Tue, 13 Jun 2017 18:13:11
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 19:16:58
s.sensitivity
#[Out]# 'Low'
# Tue, 13 Jun 2017 19:17:01
s.sensitivity = 'high'
# Tue, 13 Jun 2017 19:17:05
s.unlock
#[Out]# <bound method PFL102.unlock of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CF64908>>
# Tue, 13 Jun 2017 19:17:07
s.unlock()
# Tue, 13 Jun 2017 19:17:20
s.testInput
#[Out]# 'A_flux'
# Tue, 13 Jun 2017 19:17:28
s.testSignal = 'On'
# Tue, 13 Jun 2017 19:17:36
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 5.5,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 8.0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:17:48
s.S_Flux = 0
# Tue, 13 Jun 2017 19:17:52
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 5.5,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 8.0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:18:00
s.S_flux = 0
# Tue, 13 Jun 2017 19:18:04
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 5.5,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.1,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:18:28
s.A_bias = 45
# Tue, 13 Jun 2017 19:18:33
s.A_bias = 46
# Tue, 13 Jun 2017 19:18:49
s.A_bias = 45
# Tue, 13 Jun 2017 19:18:51
s.A_bias = 46
# Tue, 13 Jun 2017 19:18:55
s.A_bias = 47
# Tue, 13 Jun 2017 19:19:09
s.A_bias = 46
# Tue, 13 Jun 2017 19:19:12
s.A_bias = 48
# Tue, 13 Jun 2017 19:19:32
s.A_bias = 49
# Tue, 13 Jun 2017 19:19:52
s.A_bias = 47
# Tue, 13 Jun 2017 19:20:03
s.A_flux = 1
# Tue, 13 Jun 2017 19:20:07
s.A_flux = 2
# Tue, 13 Jun 2017 19:20:10
s.A_flux = 3
# Tue, 13 Jun 2017 19:20:27
s.A_bias = 46
# Tue, 13 Jun 2017 19:20:29
s.A_bias = 47
# Tue, 13 Jun 2017 19:20:35
s.A_flux = 10
# Tue, 13 Jun 2017 19:20:46
s.A_flux = 15
# Tue, 13 Jun 2017 19:21:13
s.offset = .1
# Tue, 13 Jun 2017 19:21:16
s.offset = .2
# Tue, 13 Jun 2017 19:21:28
s.lock('Array')
# Tue, 13 Jun 2017 19:21:33
s.resest()
# Tue, 13 Jun 2017 19:21:38
s.reset()
# Tue, 13 Jun 2017 19:21:40
s.reset()
# Tue, 13 Jun 2017 19:21:40
s.reset()
# Tue, 13 Jun 2017 19:21:41
s.reset()
# Tue, 13 Jun 2017 19:21:42
s.reset()
# Tue, 13 Jun 2017 19:21:43
s.reset()
# Tue, 13 Jun 2017 19:21:44
s.reset()
# Tue, 13 Jun 2017 19:21:55
s.inputSignal = 'off'
# Tue, 13 Jun 2017 19:22:00
s.inputSignal
#[Out]# 'off'
# Tue, 13 Jun 2017 19:22:08
s.inputSignal()
# Tue, 13 Jun 2017 19:22:46
s.inputSignal = SquidArray.inputSignal
# Tue, 13 Jun 2017 19:22:50
s.inputSignal = SquidArray.inputSignal()
# Tue, 13 Jun 2017 19:23:26
s.testSignal
#[Out]# 'On'
# Tue, 13 Jun 2017 19:23:30
s.testSignal = 'off'
# Tue, 13 Jun 2017 19:23:33
s.testSignal = 'Off'
# Tue, 13 Jun 2017 19:23:37
s.reset()
# Tue, 13 Jun 2017 19:23:39
s.reset()
# Tue, 13 Jun 2017 19:23:40
s.reset()
# Tue, 13 Jun 2017 19:23:40
s.reset()
# Tue, 13 Jun 2017 19:23:48
s.A_bias = 
# Tue, 13 Jun 2017 19:23:50
s.A_bias
#[Out]# 47
# Tue, 13 Jun 2017 19:24:00
s.A_flux
#[Out]# 15
# Tue, 13 Jun 2017 19:24:03
s.A_flux = 14
# Tue, 13 Jun 2017 19:24:05
s.A_flux = 13
# Tue, 13 Jun 2017 19:24:08
s.A_flux = 12
# Tue, 13 Jun 2017 19:24:11
s.A_flux = 11
# Tue, 13 Jun 2017 19:24:14
s.A_flux = 14
# Tue, 13 Jun 2017 19:24:18
s.A_flux = 15
# Tue, 13 Jun 2017 19:24:21
s.A_flux = 17
# Tue, 13 Jun 2017 19:24:24
s.A_flux = 18
# Tue, 13 Jun 2017 19:24:27
s.A_flux = 20
# Tue, 13 Jun 2017 19:24:32
s.A_flux = 19
# Tue, 13 Jun 2017 19:26:08
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 19:26:16
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 19:32:21
s.unlock()
# Tue, 13 Jun 2017 19:32:29
s.testSignal = 'On'
# Tue, 13 Jun 2017 19:32:37
s.A_bias
#[Out]# 47
# Tue, 13 Jun 2017 19:32:40
s.A_bias = 46
# Tue, 13 Jun 2017 19:32:51
s.lock('array')
# Tue, 13 Jun 2017 19:33:01
s.testSignal = 'Off'
# Tue, 13 Jun 2017 19:33:11
s.sensitivity
#[Out]# 'High'
# Tue, 13 Jun 2017 19:34:09
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 19:36:08
s.unlock()
# Tue, 13 Jun 2017 19:36:13
s.reset()
# Tue, 13 Jun 2017 19:36:21
s.testSignal= 'On'
# Tue, 13 Jun 2017 19:36:23
s.reset
#[Out]# <bound method PFL102.reset of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CF64908>>
# Tue, 13 Jun 2017 19:36:46
s.A_bias = 48
# Tue, 13 Jun 2017 19:37:06
s.A_bias = 49
# Tue, 13 Jun 2017 19:37:10
s.A_bias = 50
# Tue, 13 Jun 2017 19:37:15
s.A_bias = 51
# Tue, 13 Jun 2017 19:37:20
s.reset()
# Tue, 13 Jun 2017 19:37:25
s.A_bias = 52
# Tue, 13 Jun 2017 19:37:55
s.offset = .5
# Tue, 13 Jun 2017 19:38:02
s.offset = .55
# Tue, 13 Jun 2017 19:38:07
s.offset = .6
# Tue, 13 Jun 2017 19:38:14
s.offset = .58
# Tue, 13 Jun 2017 19:38:24
s.lock('Array')
# Tue, 13 Jun 2017 19:38:33
s.testSignal = 'Off'
# Tue, 13 Jun 2017 19:38:45
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 19:41:16
s.unlock()
# Tue, 13 Jun 2017 19:41:24
s.__getstatus__()
# Tue, 13 Jun 2017 19:41:29
s.__getstate__()
#[Out]# {'Array bias': 52,
#[Out]#  'Array flux': 19,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.58,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:41:41
s.testSignal='On'
# Tue, 13 Jun 2017 19:41:49
s.A_bias = 53
# Tue, 13 Jun 2017 19:41:54
s.A_bias = 54
# Tue, 13 Jun 2017 19:41:56
s.A_bias = 55
# Tue, 13 Jun 2017 19:41:58
s.A_bias = 5
# Tue, 13 Jun 2017 19:42:02
s.A_bias = 56
# Tue, 13 Jun 2017 19:42:06
s.A_bias = 57
# Tue, 13 Jun 2017 19:42:09
s.A_bias = 58
# Tue, 13 Jun 2017 19:42:12
s.A_bias = 59
# Tue, 13 Jun 2017 19:42:19
s.A_bias = 60
# Tue, 13 Jun 2017 19:42:34
s.A_bias = 70
# Tue, 13 Jun 2017 19:43:07
s.A_bias = 66
# Tue, 13 Jun 2017 19:43:13
s.offset
#[Out]# 0.58
# Tue, 13 Jun 2017 19:43:30
s.A_bias = 60
# Tue, 13 Jun 2017 19:43:45
s.offset = .7
# Tue, 13 Jun 2017 19:43:48
s.offset = .9
# Tue, 13 Jun 2017 19:43:52
s.offset = 1
# Tue, 13 Jun 2017 19:43:59
s.offset = .95
# Tue, 13 Jun 2017 19:44:08
s.lock('Array')
# Tue, 13 Jun 2017 19:44:14
s.testSignal='Off'
# Tue, 13 Jun 2017 19:44:22
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 19:44:33
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 19:47:51
s.__getstate__()
#[Out]# {'Array bias': 60,
#[Out]#  'Array flux': 19,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.95,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:48:01
s.testSignal='On'
# Tue, 13 Jun 2017 19:48:08
s.testInput
#[Out]# 'A_flux'
# Tue, 13 Jun 2017 19:48:15
s.testInput = 'S_flux'
# Tue, 13 Jun 2017 19:48:25
s.__getstate__()
#[Out]# {'Array bias': 60,
#[Out]#  'Array flux': 19,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.95,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 13 Jun 2017 19:48:49
s.S_bias= 450
# Tue, 13 Jun 2017 19:48:53
s.reset()
# Tue, 13 Jun 2017 19:49:03
s.S_bias= 440
# Tue, 13 Jun 2017 19:49:05
s.S_bias= 430
# Tue, 13 Jun 2017 19:49:43
s.S_bias= 440
# Tue, 13 Jun 2017 19:49:47
s.S_bias= 450
# Tue, 13 Jun 2017 20:00:02
s.S_flux
#[Out]# 0
# Tue, 13 Jun 2017 20:00:04
s.S_flux = 1
# Tue, 13 Jun 2017 20:00:08
s.S_flux = 0
# Tue, 13 Jun 2017 20:00:15
s.reset()
# Tue, 13 Jun 2017 20:00:18
s.reset()
# Tue, 13 Jun 2017 20:00:19
s.reset()
# Tue, 13 Jun 2017 20:00:20
s.reset()
# Tue, 13 Jun 2017 20:00:21
s.reset()
# Tue, 13 Jun 2017 20:00:27
s.A_bias
#[Out]# 60
# Tue, 13 Jun 2017 20:00:32
s.A_bias = 50
# Tue, 13 Jun 2017 20:00:36
s.A_bias = 60
# Tue, 13 Jun 2017 20:00:39
s.reset()
# Tue, 13 Jun 2017 20:00:53
s.A_flux
#[Out]# 19
# Tue, 13 Jun 2017 20:00:55
s.A_flux = 20
# Tue, 13 Jun 2017 20:00:58
s.A_flux = 24
# Tue, 13 Jun 2017 20:01:02
s.A_flux = 30
# Tue, 13 Jun 2017 20:01:11
s.A_flux = 28
# Tue, 13 Jun 2017 20:01:25
s.lock('squid')
# Tue, 13 Jun 2017 20:01:28
s.reset()
# Tue, 13 Jun 2017 20:01:32
s.testSignal
#[Out]# 'On'
# Tue, 13 Jun 2017 20:01:35
s.testSignal = 'off'
# Tue, 13 Jun 2017 20:01:38
s.testSignal = 'Off'
# Tue, 13 Jun 2017 20:01:40
s.reset()
# Tue, 13 Jun 2017 20:01:52
s.reset()
# Tue, 13 Jun 2017 20:01:53
s.reset()
# Tue, 13 Jun 2017 20:01:53
s.reset()
# Tue, 13 Jun 2017 20:02:02
s.S_flux
#[Out]# 0
# Tue, 13 Jun 2017 20:02:04
s.S_flux = 10
# Tue, 13 Jun 2017 20:02:06
s.S_flux = 20
# Tue, 13 Jun 2017 20:02:08
s.S_flux = 40
# Tue, 13 Jun 2017 20:02:11
s.reset()
# Tue, 13 Jun 2017 20:02:15
s.S_flux = 50
# Tue, 13 Jun 2017 20:02:18
s.S_flux = 80
# Tue, 13 Jun 2017 20:02:23
s.S_flux = 100
# Tue, 13 Jun 2017 20:02:28
s.reset()
# Tue, 13 Jun 2017 20:02:33
s.S_flux = 110
# Tue, 13 Jun 2017 20:02:37
s.S_flux
#[Out]# 100
# Tue, 13 Jun 2017 20:02:40
s.reset()
# Tue, 13 Jun 2017 20:02:41
s.reset()
# Tue, 13 Jun 2017 20:02:41
s.reset()
# Tue, 13 Jun 2017 20:02:42
s.reset()
# Tue, 13 Jun 2017 20:02:50
s.S_flux = 0
# Tue, 13 Jun 2017 20:02:54
s.reset ()
# Tue, 13 Jun 2017 20:03:07
s.lock('Array')
# Tue, 13 Jun 2017 20:03:13
s.testSignal='On'
# Tue, 13 Jun 2017 20:03:16
s.reset()
# Tue, 13 Jun 2017 20:03:34
s.S_bias
#[Out]# 450
# Tue, 13 Jun 2017 20:03:37
s.S_flux
#[Out]# 0
# Tue, 13 Jun 2017 20:03:42
s.S_flux=10
# Tue, 13 Jun 2017 20:03:45
s.S_flux=20
# Tue, 13 Jun 2017 20:03:48
s.S_flux=30
# Tue, 13 Jun 2017 20:03:56
s.lock()
# Tue, 13 Jun 2017 20:04:03
s.lock('Squid')
# Tue, 13 Jun 2017 20:04:08
s.reset ()
# Tue, 13 Jun 2017 20:04:09
s.reset ()
# Tue, 13 Jun 2017 20:04:10
s.reset ()
# Tue, 13 Jun 2017 20:04:11
s.reset ()
# Tue, 13 Jun 2017 20:04:17
s.S_flux
#[Out]# 30
# Tue, 13 Jun 2017 20:04:20
s.S_flux = 40
# Tue, 13 Jun 2017 20:04:22
s.S_flux = 30
# Tue, 13 Jun 2017 20:04:25
s.S_flux = 20
# Tue, 13 Jun 2017 20:04:27
s.S_flux = 10
# Tue, 13 Jun 2017 20:04:29
s.S_flux = 0
# Tue, 13 Jun 2017 20:04:32
s.reset()
# Tue, 13 Jun 2017 20:04:33
s.reset()
# Tue, 13 Jun 2017 20:04:42
s.S_flux=100
# Tue, 13 Jun 2017 20:04:46
s.reset()
# Tue, 13 Jun 2017 20:04:52
s.testSignal='Off'
# Tue, 13 Jun 2017 20:05:43
s.testSignal = 'On'
# Tue, 13 Jun 2017 20:05:53
s.testSignal='Off'
# Tue, 13 Jun 2017 20:07:05
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xf918ac8>
# Tue, 13 Jun 2017 20:07:17
pa.dc_coupling
#[Out]# <bound method SR5113.dc_coupling of <Nowack_Lab.Instruments.preamp.SR5113 object at 0x000000000F918AC8>>
# Tue, 13 Jun 2017 20:07:40
pa.__getstate__()
#[Out]# {'filter': (1, 100000), 'gain': 25}
# Tue, 13 Jun 2017 20:07:50
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 20:08:21
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, measure_time=1, 
						 annotate_notes=True)
pzvals = pz.V;
spectrum.notes = '''AC coupled 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 20:21:55
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
# Tue, 13 Jun 2017 20:31:31
reload
#[Out]# <function imp.reload>
# Tue, 13 Jun 2017 20:31:40
reload(Nowack_Lab.Procedures.daqspectrum)
# Tue, 13 Jun 2017 20:31:59
from Nowack_Lab.Procedures import daqspectrum
# Tue, 13 Jun 2017 20:32:03
reload(daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Tue, 13 Jun 2017 20:32:17
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 20:33:11
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
						measure_time=1, 
						annotate_notes=True,
						preamp_gain_override=True,
						preamp_filter_override=True,
						preamp_dccouple_override=True
			)
pzvals = pz.V;
spectrum.notes = '''AC couple, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()

# Tue, 13 Jun 2017 20:33:44
reload(daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Tue, 13 Jun 2017 20:33:55
from daqspectrum import DaqSpectrum
# Tue, 13 Jun 2017 20:34:50
get_ipython().magic('run -i ../../../Users/B82A/Documents/GitHub/Nowack_Lab/Procedures/daqspectrum.py')
