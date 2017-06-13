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
