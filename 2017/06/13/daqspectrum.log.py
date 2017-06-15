# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Tue, 13 Jun 2017 22:37:06
get_ipython().magic('load qtconsole/2017/06/setups/main_20170613.py')
# Tue, 13 Jun 2017 22:37:08
# %load qtconsole/2017/06/setups/main_20170613.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170613.py')

# Tue, 13 Jun 2017 22:37:21
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xcffd668>
# Tue, 13 Jun 2017 22:37:26
s.__getstate__()
#[Out]# {'Array bias': 60,
#[Out]#  'Array flux': 60,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0.95,
#[Out]#  'SQUID bias': 450,
#[Out]#  'SQUID flux': 100,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Tue, 13 Jun 2017 22:41:21
s.testSignal='Off'
# Tue, 13 Jun 2017 22:41:35
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 22:42:04
CAP_I = liC.R
# Tue, 13 Jun 2017 22:42:06
CAP_I
#[Out]# 1.00304e-06
# Tue, 13 Jun 2017 22:42:08
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 22:44:11
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
						measure_time=1, 
						annotate_notes=True,
						preamp_gain_override=True,
						preamp_filter_override=True,
						preamp_dccouple_override=False,
                       preamp_dccouple=True
			)
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

# Tue, 13 Jun 2017 22:46:03
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 22:46:54
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 22:46:56
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Tue, 13 Jun 2017 22:54:42
s.sensitivity='High'
# Tue, 13 Jun 2017 22:55:30
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=True
            )
pzvals = pz.V;
spectrum.notes = '''AC couple, 10 s, 
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

# Tue, 13 Jun 2017 23:08:32
s.sensitivity='Med'
# Tue, 13 Jun 2017 23:08:42
s.reset()
# Tue, 13 Jun 2017 23:14:11
len(spectrum.V)
#[Out]# 256000
# Tue, 13 Jun 2017 23:21:11
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Tue, 13 Jun 2017 23:21:20
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Tue, 13 Jun 2017 23:24:34
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Tue, 13 Jun 2017 23:24:45
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Tue, 13 Jun 2017 23:26:59
spectrum.V
#[Out]# array([ 0.07958658,  0.07980561,  0.07996021, ...,  0.07847855,
#[Out]#         0.07851721,  0.07856874])
# Tue, 13 Jun 2017 23:27:14
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Tue, 13 Jun 2017 23:27:25
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
# Tue, 13 Jun 2017 23:27:31
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Tue, 13 Jun 2017 23:29:13
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Tue, 13 Jun 2017 23:29:15
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
# Tue, 13 Jun 2017 23:29:19
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Tue, 13 Jun 2017 23:31:10
spectrum.V
#[Out]# array([[ 0.07846567,  0.07856874,  0.07854297, ...,  0.0777184 ,
#[Out]#          0.07758956,  0.07756379],
#[Out]#        [ 0.07922583,  0.07905833,  0.07892949, ...,  0.07813069,
#[Out]#          0.07806627,  0.07828529],
#[Out]#        [ 0.0784399 ,  0.07842702,  0.07863316, ...,  0.07865893,
#[Out]#          0.07865893,  0.07872335],
#[Out]#        ..., 
#[Out]#        [ 0.07798896,  0.07786012,  0.07787301, ...,  0.07834971,
#[Out]#          0.07824664,  0.07831106],
#[Out]#        [ 0.07806627,  0.07797608,  0.07792454, ...,  0.07910987,
#[Out]#          0.0793289 ,  0.07938043],
#[Out]#        [ 0.07840125,  0.07840125,  0.07849144, ...,  0.0781178 ,
#[Out]#          0.07801473,  0.07797608]])
# Tue, 13 Jun 2017 23:31:13
spectrum.V[0]
#[Out]# array([ 0.07846567,  0.07856874,  0.07854297, ...,  0.0777184 ,
#[Out]#         0.07758956,  0.07756379])
# Tue, 13 Jun 2017 23:31:18
spectrum.V[1]
#[Out]# array([ 0.07922583,  0.07905833,  0.07892949, ...,  0.07813069,
#[Out]#         0.07806627,  0.07828529])
# Tue, 13 Jun 2017 23:31:22
spectrum.V[29]
#[Out]# array([ 0.07840125,  0.07840125,  0.07849144, ...,  0.0781178 ,
#[Out]#         0.07801473,  0.07797608])
# Wed, 14 Jun 2017 00:01:40
get_ipython().magic('load qtconsole/2017/06/setups/quickline_20170613.py')
# Wed, 14 Jun 2017 00:01:42
# %load qtconsole/2017/06/setups/quickline_20170613.py
plt.close('all')
sc = Scanplane(instruments,pf,
	span=[800,1], 
	center=[0,0], 
	numpts=[2000,3],
	scan_rate=100, 
	scanheight=15
);
sc.notes = '''[dhl88]  Quick Line scan
'''
sc.run()

# Wed, 14 Jun 2017 00:03:36
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-08_mattplane_and_scan\2017-06-09\2017-06-09_222930_Planefit.json", instruments=instruments)
# Wed, 14 Jun 2017 00:04:02
get_ipython().magic('load qtconsole/2017/06/setups/quickline_20170613.py')
# Wed, 14 Jun 2017 00:04:39
# %load qtconsole/2017/06/setups/quickline_20170613.py
plt.close('all')
sc = Scanplane(instruments,pf,
	span=[200,1], 
	center=[213,0], 
	numpts=[2000,3],
	scan_rate=100, 
	scanheight=50
);
sc.notes = '''[dhl88]  Quick Line scan at 50 mK
'''
sc.run()

# Wed, 14 Jun 2017 01:00:40
get_ipython().magic('load qtconsole/2017/06/setups/quickline1_20170613.py')
# Wed, 14 Jun 2017 01:00:42
# %load qtconsole/2017/06/setups/quickline1_20170613.py
plt.close('all')
sl = Scanline(instruments,pf,
	start=(100,0),
	end=(300,0) 
	scan_rate=100, 
	scanheight=15
);
sl.notes = '''[dhl88]  Quick Line scan
'''
sl.run()
# Wed, 14 Jun 2017 01:00:54
# %load qtconsole/2017/06/setups/quickline1_20170613.py
plt.close('all')
sl = Scanline(instruments,pf,
	start=(100,0),
	end=(300,0) 
	scan_rate=100, 
	scanheight=15
);
sl.notes = '''[dhl88]  Quick Line scan
'''
sl.run()
# Wed, 14 Jun 2017 01:01:26
get_ipython().magic('load qtconsole/2017/06/setups/quickline1_20170613.py')
# Wed, 14 Jun 2017 01:01:29
# %load qtconsole/2017/06/setups/quickline1_20170613.py
plt.close('all')
sl = Scanline(instruments,pf,
	start=(100,0),
	end=(300,0),
	scan_rate=100,
	scanheight=15
);
sl.notes = '''[dhl88]  Quick Line scan
'''
sl.run()

# Wed, 14 Jun 2017 01:17:45
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:17:46
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);


sp = Scanplane.load(file);
fig = plt.figure()
ax = {};
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

x = s.X;
y = s.Y;
z = s.Z;

fig = plt.figure()
ax['dc']  = plt.subplots(141);
ax['cap'] = plt.subplots(142);
ax['acx'] = plt.subplots(143);
ax['acy'] = plt.subplots(144);

for entry in ventries:
	ax[entry].plot(s.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:18:22
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:18:23
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);


sp = Scanplane.load(file);
fig = plt.figure()
ax = {};
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

x = sp.X;
y = sp.Y;
z = sp.Z;

fig = plt.figure()
ax['dc']  = plt.subplots(141);
ax['cap'] = plt.subplots(142);
ax['acx'] = plt.subplots(143);
ax['acy'] = plt.subplots(144);

for entry in ventries:
	ax[entry].plot(s.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:19:55
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:19:55
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);


sp = Scanplane.load(file);
fig = plt.figure()
ax = {};
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig = plt.figure()
fig, ax['dc']  = fig.subplots(141);
fig, ax['cap'] = fig.subplots(142);
fig, ax['acx'] = fig.subplots(143);
fig, ax['acy'] = fig.subplots(144);

for entry in ventries:
	ax[entry].plot(sp.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:20:13
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:20:14
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);


sp = Scanplane.load(file);
fig = plt.figure()
ax = {};
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig = plt.figure()
fig, ax['dc']  = fig.add_subplots(141);
fig, ax['cap'] = fig.add_subplots(142);
fig, ax['acx'] = fig.add_subplots(143);
fig, ax['acy'] = fig.add_subplots(144);

for entry in ventries:
	ax[entry].plot(sp.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:22:26
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:22:26
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);


sp = Scanplane.load(file);
fig = plt.figure()
ax = {};
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig = plt.figure()
ax['dc']  = fig.add_subplot(411);
ax['cap'] = fig.add_subplot(412);
ax['acx'] = fig.add_subplot(413);
ax['acy'] = fig.add_subplot(414);

for entry in ventries:
	ax[entry].plot(sp.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:22:59
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:22:59
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig = plt.figure();
ax['dc']  = fig.add_subplot(411);
ax['cap'] = fig.add_subplot(412);
ax['acx'] = fig.add_subplot(413);
ax['acy'] = fig.add_subplot(414);

for entry in ventries:
	ax[entry].plot(sp.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');



# Wed, 14 Jun 2017 01:25:46
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:25:47
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig = plt.figure();
ax['dc']  = fig.add_subplot(411, sharex=True);
ax['cap'] = fig.add_subplot(412, sharex=True);
ax['acx'] = fig.add_subplot(413, sharex=True);
ax['acy'] = fig.add_subplot(414, sharex=True);

for entry in ventries:
	ax[entry].plot(sp.X[line], sp.V[entry][line]);
	ax[entry].set_ylabel(entry);
	ax[entry].set_xlabel('V');

ax['cap'].set_y

# Wed, 14 Jun 2017 01:27:19
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:27:20
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

self.fig_cuts, self.axes_cuts = plt.subplots(4, 1, figsize=(6, 8),
                                                     sharex=True)


for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);


# Wed, 14 Jun 2017 01:28:11
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:28:11
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);


# Wed, 14 Jun 2017 01:30:22
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:30:24
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
fig.tight_layout()

# Wed, 14 Jun 2017 01:33:59
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:34:03
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
fig.tight_layout()
fig.set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.y[line][0]),
				int(sp.z[line][0])
			)
)

# Wed, 14 Jun 2017 01:34:17
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:34:17
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
fig.tight_layout()
ax.set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.y[line][0]),
				int(sp.z[line][0])
			)
)
# Wed, 14 Jun 2017 01:34:28
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:34:31
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
fig.tight_layout()
ax[0].set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.y[line][0]),
				int(sp.z[line][0])
			)
)

# Wed, 14 Jun 2017 01:34:47
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:34:49
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
fig.tight_layout()
ax[0].set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.Y[line][0]),
				int(sp.Z[line][0])
			)
)

#[Out]# <matplotlib.text.Text at 0x4d917780>
# Wed, 14 Jun 2017 01:35:10
get_ipython().magic('load qtconsole/2017/06/analyze/plotlinecut2.py')
# Wed, 14 Jun 2017 01:35:12
# %load qtconsole/2017/06/analyze/plotlinecut2.py
import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel(ventries[entry]);

ax[-1].set_xlabel('V')
ax[0].set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.Y[line][0]),
				int(sp.Z[line][0])
			)
)
fig.tight_layout()

# Wed, 14 Jun 2017 02:33:50
s.sensitivity
#[Out]# 'Med'
# Wed, 14 Jun 2017 02:37:25
get_ipython().magic('load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py')
# Wed, 14 Jun 2017 02:38:11
# %load qtconsole/2017/06/setups/daqspectrum_singlewithnotes.py
spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=10, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
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

# Wed, 14 Jun 2017 02:48:55
["{0:d}", "{1:d}"].format(1,2)
# Wed, 14 Jun 2017 02:49:07
str(["{0:d}", "{1:d}"]).format(1,2)
#[Out]# "['1', '2']"
# Wed, 14 Jun 2017 02:49:25
a = ["{0:d}", "{1:d}"]; a.format(1,2)
# Wed, 14 Jun 2017 02:49:38
a = ("{0:d}", "{1:d}"); a.format(1,2)
# Wed, 14 Jun 2017 02:49:49
a = ("{0:d}", "{1:d}"); a = str(a); a.format(1,2)
#[Out]# "('1', '2')"
# Wed, 14 Jun 2017 02:54:00
a = ("{0:d}" "{1:d}"); a = str(a); a.format(1,2)
#[Out]# '12'
# Wed, 14 Jun 2017 02:54:43
(a 'hello')
# Wed, 14 Jun 2017 02:54:55
b = (a 'hello')
# Wed, 14 Jun 2017 03:02:01
reload(Nowack_Lab.Procedures.daqspectrum)
# Wed, 14 Jun 2017 03:02:27
reload(Nowack_Lab.Procedures.daqspectrum)
# Wed, 14 Jun 2017 03:02:39
reload(Nowack_Lab.Procedures.daqspectrum)
# Wed, 14 Jun 2017 03:03:10
reload(Nowack_Lab.Procedures.daqspectrum)
# Wed, 14 Jun 2017 03:03:22
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:03:43
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:05:10
spectrum = AnnotatedSpectrum(instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:05:22
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:05:41
instruments
#[Out]# {'atto': <Nowack_Lab.Instruments.attocube.Attocube at 0xcffd198>,
#[Out]#  'daq': <Nowack_Lab.Instruments.nidaq.NIDAQ at 0x7d99eb8>,
#[Out]#  'lockin_cap': <Nowack_Lab.Instruments.lockin.SR830 at 0x7db1240>,
#[Out]#  'lockin_squid': <Nowack_Lab.Instruments.lockin.SR830 at 0xcff5198>,
#[Out]#  'montana': <Nowack_Lab.Instruments.montana.Montana at 0xcfddbe0>,
#[Out]#  'piezos': <Nowack_Lab.Instruments.piezos.Piezos at 0xcff5358>,
#[Out]#  'preamp': <Nowack_Lab.Instruments.preamp.SR5113 at 0xcfddda0>,
#[Out]#  'squidarray': <Nowack_Lab.Instruments.squidarray.SquidArray at 0xcffd668>}
# Wed, 14 Jun 2017 03:08:39
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:08:44
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:08:48
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:09:42
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:09:43
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:09:47
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:10:00
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:10:01
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:10:05
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:10:54
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:10:56
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:10:58
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
# Wed, 14 Jun 2017 03:11:30
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 03:11:35
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 03:11:41
from Nowack_Lab.Procedures.daqspectrum import DaqSpectrum
# Wed, 14 Jun 2017 03:11:46
spectrum = AnnotatedSpectrum(CAP_I, instruments=instruments,
measure_time=1,
preamp_gain_override=True,
preamp_filter_override=True,
preamp_dccouple_override=True
)
