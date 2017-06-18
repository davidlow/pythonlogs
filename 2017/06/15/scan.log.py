# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Fri, 16 Jun 2017 02:37:50
get_ipython().magic('load qtconsole/2017/06/setups/main_20170613.py')
# Fri, 16 Jun 2017 02:37:52
# %load qtconsole/2017/06/setups/main_20170613.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170613.py')

# Fri, 16 Jun 2017 02:38:02
td = Touchdown(instruments, planescan=False)
# Fri, 16 Jun 2017 02:38:12
td.run()
# Fri, 16 Jun 2017 02:48:07
pf = Planefit(instruments)
# Fri, 16 Jun 2017 02:48:17
pf.run()
# Fri, 16 Jun 2017 03:15:20
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xc6671d0>
# Fri, 16 Jun 2017 03:15:23
s.reset()
# Fri, 16 Jun 2017 03:15:25
s.status
# Fri, 16 Jun 2017 03:15:30
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
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Fri, 16 Jun 2017 03:15:41
s.tune()
# Fri, 16 Jun 2017 03:16:04
s.__getstate__()
#[Out]# {'Array bias': 43.0,
#[Out]#  'Array flux': 60,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0.95,
#[Out]#  'SQUID bias': 450,
#[Out]#  'SQUID flux': 100,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Auto',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Fri, 16 Jun 2017 03:16:15
s.A_flux=0
# Fri, 16 Jun 2017 03:16:53
s.reset()
# Fri, 16 Jun 2017 03:17:12
s.S_flux = 0
# Fri, 16 Jun 2017 03:17:15
s.reset()
# Fri, 16 Jun 2017 03:18:32
s.A_bias
#[Out]# 43.0
# Fri, 16 Jun 2017 03:18:34
s.A_bias = 0
# Fri, 16 Jun 2017 03:18:38
s.reset()
# Fri, 16 Jun 2017 03:18:45
s.heat()
# Fri, 16 Jun 2017 03:18:59
s.reset()
# Fri, 16 Jun 2017 03:19:36
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xc6671d0>
# Fri, 16 Jun 2017 03:20:12
s.reset()
# Fri, 16 Jun 2017 03:20:13
s.reset()
# Fri, 16 Jun 2017 03:20:14
s.reset()
# Fri, 16 Jun 2017 03:20:38
s.zero
#[Out]# <bound method SquidArray.zero of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000C6671D0>>
# Fri, 16 Jun 2017 03:20:41
s.zero()
# Fri, 16 Jun 2017 03:20:50
s.__getstate__()
#[Out]# {'Array bias': 0,
#[Out]#  'Array flux': 0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Fri, 16 Jun 2017 03:21:05
s.testSignal = 'On'
# Fri, 16 Jun 2017 03:21:10
s.reset
#[Out]# <bound method PFL102.reset of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000C6671D0>>
# Fri, 16 Jun 2017 03:21:18
s.A_bias = 43
# Fri, 16 Jun 2017 03:21:30
s.offset = .1
# Fri, 16 Jun 2017 03:21:39
s.reset()
# Fri, 16 Jun 2017 03:21:49
s.offset = .5
# Fri, 16 Jun 2017 03:21:52
s.offset = .3
# Fri, 16 Jun 2017 03:21:55
s.offset = .2
# Fri, 16 Jun 2017 03:22:21
s.A_bias = 44
# Fri, 16 Jun 2017 03:22:24
s.A_bias = 42
# Fri, 16 Jun 2017 03:22:26
s.A_bias = 43
# Fri, 16 Jun 2017 03:22:29
s.A_bias = 45
# Fri, 16 Jun 2017 03:22:30
s.A_bias = 46
# Fri, 16 Jun 2017 03:22:33
s.A_bias = 43
# Fri, 16 Jun 2017 03:22:39
s.A_bias = 42
# Fri, 16 Jun 2017 03:22:42
s.A_bias = 42.5
# Fri, 16 Jun 2017 03:22:50
s.A_bias = 43
# Fri, 16 Jun 2017 03:22:53
s.A_bias = 42
# Fri, 16 Jun 2017 03:22:58
s.A_bias = 43
# Fri, 16 Jun 2017 03:23:09
s.lock('Array')
# Fri, 16 Jun 2017 03:23:14
s.reset()
# Fri, 16 Jun 2017 03:23:29
s.A_flux = 1
# Fri, 16 Jun 2017 03:23:31
s.A_flux = 5
# Fri, 16 Jun 2017 03:23:35
s.reset()
# Fri, 16 Jun 2017 03:24:00
s.testInput('S_flux')
# Fri, 16 Jun 2017 03:24:12
s.testSignal('S_Flux')
# Fri, 16 Jun 2017 03:24:28
s.testInput = 'S_flux'
# Fri, 16 Jun 2017 03:24:31
s.reset()
# Fri, 16 Jun 2017 03:24:50
s.S_bias = 450
# Fri, 16 Jun 2017 03:24:53
s.reset()
# Fri, 16 Jun 2017 03:25:06
s.S_bias = 400
# Fri, 16 Jun 2017 03:25:16
s.S_flux = 5
# Fri, 16 Jun 2017 03:25:19
s.S_flux = 0
# Fri, 16 Jun 2017 03:25:24
s.A_flux
#[Out]# 5
# Fri, 16 Jun 2017 03:25:27
s.A_flux = 6
# Fri, 16 Jun 2017 03:25:30
s.A_flux = 0
# Fri, 16 Jun 2017 03:25:34
s.A_flux = 1
# Fri, 16 Jun 2017 03:25:37
s.A_flux = 2
# Fri, 16 Jun 2017 03:25:49
s.lock('Squid')
# Fri, 16 Jun 2017 03:25:57
s.testSignal = 'Off'
# Fri, 16 Jun 2017 03:26:01
s.reset()
# Fri, 16 Jun 2017 03:26:07
s.S_flux
#[Out]# 0
# Fri, 16 Jun 2017 03:26:09
s.S_flux = 1
# Fri, 16 Jun 2017 03:26:12
s.S_flux = 40
# Fri, 16 Jun 2017 03:26:14
s.S_flux = 20
# Fri, 16 Jun 2017 03:26:19
s.S_flux = 10
# Fri, 16 Jun 2017 03:26:22
s.S_flux = 12
# Fri, 16 Jun 2017 03:26:26
s.reset()
# Fri, 16 Jun 2017 03:26:27
s.reset()
# Fri, 16 Jun 2017 03:26:28
s.reset()
# Fri, 16 Jun 2017 03:26:29
s.reset()
# Fri, 16 Jun 2017 03:35:18
CAP_I = liC.R
# Fri, 16 Jun 2017 03:35:20
CAP_I
#[Out]# 1.09338e-06
# Fri, 16 Jun 2017 03:35:54
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xc63a940>
# Fri, 16 Jun 2017 03:35:57
pa.gain
#[Out]# 1
# Fri, 16 Jun 2017 03:35:59
pa.gain = 5
# Fri, 16 Jun 2017 03:36:04
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:36:08
pa.gain = 20
# Fri, 16 Jun 2017 03:36:12
pa.gain
#[Out]# 20
# Fri, 16 Jun 2017 03:36:18
pa.gain = 25
# Fri, 16 Jun 2017 03:36:22
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:36:25
pa.gain = 50
# Fri, 16 Jun 2017 03:36:27
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:36:32
pa.gain = 100
# Fri, 16 Jun 2017 03:36:34
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:36:38
pa.gain = 250
# Fri, 16 Jun 2017 03:36:40
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:36:45
pa.gain = 500
# Fri, 16 Jun 2017 03:36:47
pa.is_OL()
#[Out]# False
# Fri, 16 Jun 2017 03:37:02
pa.gain()
# Fri, 16 Jun 2017 03:37:06
pa.gain
#[Out]# 1000
# Fri, 16 Jun 2017 03:38:44
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="test scan", measure_time=1, preamp_gain_override=True, preamp_filter_override=True,preamp_dccouple_override=True, preamp_autoOL=False)
# Fri, 16 Jun 2017 03:38:46
a.run()
# Fri, 16 Jun 2017 03:42:45
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="test scan", measure_time=1, preamp_gain_override=True, preamp_filter_override=True,preamp_dccouple_override=True, preamp_autoOL=False)
# Fri, 16 Jun 2017 03:42:54
self.units = '\phi_0'
# Fri, 16 Jun 2017 03:42:57
a.units = '\phi_0'
# Fri, 16 Jun 2017 03:43:31
from Nowack_Lab.Utilities import conversions
# Fri, 16 Jun 2017 03:45:28
a.conversion = conversions.Vsquid_to_phi0[self.squidarray.sensitivity]
# Fri, 16 Jun 2017 03:45:37
a.conversion = conversions.Vsquid_to_phi0[s.sensitivity]
# Fri, 16 Jun 2017 03:45:42
a.run()
# Fri, 16 Jun 2017 03:47:39
s.sensitivity='High'
# Fri, 16 Jun 2017 03:48:06
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="test scan", measure_time=1, preamp_gain_override=True, preamp_filter_override=True,preamp_dccouple_override=True, preamp_autoOL=False)
# Fri, 16 Jun 2017 03:48:11
a.units = '\phi_0'
# Fri, 16 Jun 2017 03:48:17
a.conversion = conversions.Vsquid_to_phi0[s.sensitivity]
# Fri, 16 Jun 2017 03:48:19
a.run()
# Fri, 16 Jun 2017 03:50:46
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="long scan", measure_time=30, preamp_gain_override=True, preamp_filter_override=True,preamp_dccouple_override=True, preamp_autoOL=False)
# Fri, 16 Jun 2017 03:50:50
a.units = '\phi_0'
# Fri, 16 Jun 2017 03:50:51
a.conversion = conversions.Vsquid_to_phi0[s.sensitivity]
# Fri, 16 Jun 2017 03:50:54
a.run()
# Fri, 16 Jun 2017 04:09:57
s.sensitive
# Fri, 16 Jun 2017 04:10:05
s.sensitivity
#[Out]# 'High'
# Fri, 16 Jun 2017 04:10:09
s.sensitivity = 'Med'
# Fri, 16 Jun 2017 04:10:25
pa.gain = 25
# Fri, 16 Jun 2017 04:20:13
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_20170609.py')

# Fri, 16 Jun 2017 04:22:10
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
