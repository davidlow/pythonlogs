# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Tue, 27 Jun 2017 15:21:58
get_ipython().magic('load qtconsole/2017/06/setups/setup_20170622.py')
# Tue, 27 Jun 2017 15:21:59
# %load qtconsole/2017/06/setups/setup_20170622.py
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

import Nowack_Lab.Instruments.attocube
import Nowack_Lab.Instruments.keithley
import Nowack_Lab.Instruments.lockin
import Nowack_Lab.Instruments.montana
import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.piezos
import Nowack_Lab.Instruments.preamp
import Nowack_Lab.Instruments.squidarray


from Nowack_Lab.Instruments.attocube        import Attocube
from Nowack_Lab.Instruments.lockin          import SR830
from Nowack_Lab.Instruments.nidaq           import NIDAQ
from Nowack_Lab.Instruments.piezos          import Piezos
from Nowack_Lab.Instruments.montana         import Montana
from Nowack_Lab.Instruments.squidarray      import SquidArray


import Nowack_Lab.Procedures.daqspectrum
import Nowack_Lab.Procedures.planefit
import Nowack_Lab.Procedures.scanplane

from Nowack_Lab.Procedures.daqspectrum      import DaqSpectrum
from Nowack_Lab.Procedures.daqspectrum      import SQUIDSpectrum
from Nowack_Lab.Procedures.daqspectrum      import AnnotatedSpectrum
from Nowack_Lab.Procedures.planefit         import Planefit
from Nowack_Lab.Procedures.scanplane        import Scanplane


# from Nowack_Lab.Instruments import NIDAQ, SR830, SR5113, Piezos, Montana, Attocube, SquidArray
# from Nowack_Lab.Procedures import Planefit

# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")
#daq.outputs = {
#    'x':0,
#    'y':1,
#    'z':2
#}
daq.inputs = {
#    'cap':0,
#    'theta':1,
#    'capx':2, # disconnected
#    'capy':3, # disconnected
#    'acx':4,
#    'acy':5,
    'dc':6
}

# Initialize other measurement equipment
pa = SR5113(port="COM3")
#liC = SR830(gpib_address=12)
#liS = SR830(gpib_address=13)
#pz = Piezos(daq)
#montana = Montana()
#atto = Attocube(montana)

s = SquidArray.load(visaResource='COM1')

# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
#    'montana':montana,
#    'piezos':pz,
#    'lockin_cap':liC,
#    'atto': atto,
    'preamp': pa,
#    'lockin_squid': liS,
    'squidarray': s
}

# Tue, 27 Jun 2017 15:22:15
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe309d30>
# Tue, 27 Jun 2017 15:22:16
s.reset()
# Tue, 27 Jun 2017 15:22:22
s.__getstate__()
#[Out]# {'Array bias': 0,
#[Out]#  'Array flux': 0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 27 Jun 2017 15:22:30
s.A_bias=44
# Tue, 27 Jun 2017 15:22:44
s.testInput='A_flux'
# Tue, 27 Jun 2017 15:22:47
s.testSignal
#[Out]# 'Off'
# Tue, 27 Jun 2017 15:22:49
s.testSignal = 'On'
# Tue, 27 Jun 2017 15:22:53
s.reset()
# Tue, 27 Jun 2017 15:23:02
s.A_bias=40
# Tue, 27 Jun 2017 15:23:04
s.reset
#[Out]# <bound method PFL102.reset of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000E309D30>>
# Tue, 27 Jun 2017 15:23:09
s.heat()
# Tue, 27 Jun 2017 15:23:39
s.A_bias=41
# Tue, 27 Jun 2017 15:23:41
s.A_bias=42
# Tue, 27 Jun 2017 15:23:44
s.A_bias=41
# Tue, 27 Jun 2017 15:23:53
s.offset
#[Out]# 0
# Tue, 27 Jun 2017 15:23:55
s.offset = .1
# Tue, 27 Jun 2017 15:23:58
s.offset = .2
# Tue, 27 Jun 2017 15:24:12
s.lock('Array')
# Tue, 27 Jun 2017 15:24:15
s.reset()
# Tue, 27 Jun 2017 15:24:18
s.reset()
# Tue, 27 Jun 2017 15:24:22
s.A_flux
#[Out]# 0
# Tue, 27 Jun 2017 15:24:24
s.A_flux = 1
# Tue, 27 Jun 2017 15:24:26
s.A_flux = 20
# Tue, 27 Jun 2017 15:24:29
s.reset()
# Tue, 27 Jun 2017 15:24:32
s.A_flux = 30
# Tue, 27 Jun 2017 15:24:37
s.A_flux = 40
# Tue, 27 Jun 2017 15:24:41
s.reset()
# Tue, 27 Jun 2017 15:24:45
s.A_flux = 35
# Tue, 27 Jun 2017 15:24:53
s.testSignal
#[Out]# 'On'
# Tue, 27 Jun 2017 15:24:55
s.testSignal = 'Off'
# Tue, 27 Jun 2017 15:25:29
get_ipython().magic('load qtconsole/2017/06/setups/annotatedspectrum_20170626.py')
# Tue, 27 Jun 2017 15:25:45
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.arrayspectra()
spectrum.run()

# Tue, 27 Jun 2017 15:29:38
get_ipython().magic('load qtconsole/2017/06/setups/annotatedspectrum_20170626.py')
# Tue, 27 Jun 2017 15:29:52
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 30, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4k'
spectrum.arrayspectra()
spectrum.run()

# Tue, 27 Jun 2017 15:48:54
s.S_bias
#[Out]# 0
# Tue, 27 Jun 2017 15:50:04
s.S_bias = 1420
# Tue, 27 Jun 2017 15:50:07
s.reset()
# Tue, 27 Jun 2017 15:50:10
s.reset()
# Tue, 27 Jun 2017 15:50:11
s.reset()
# Tue, 27 Jun 2017 15:50:12
s.reset()
# Tue, 27 Jun 2017 15:50:13
s.reset()
# Tue, 27 Jun 2017 15:50:19
s.S_flux
#[Out]# 0
# Tue, 27 Jun 2017 15:50:33
s.testSignal
#[Out]# 'Off'
# Tue, 27 Jun 2017 15:50:35
s.testSignal = 'On'
# Tue, 27 Jun 2017 15:50:37
s.testInput
#[Out]# 'A_flux'
# Tue, 27 Jun 2017 15:50:43
s.testInput = 'S_flux'
# Tue, 27 Jun 2017 15:50:46
s.reset()
# Tue, 27 Jun 2017 15:50:51
s.A_flux
#[Out]# 35
# Tue, 27 Jun 2017 15:50:52
s.A_flux = 0
# Tue, 27 Jun 2017 15:50:54
s.reset()
# Tue, 27 Jun 2017 15:51:13
s.reset()
# Tue, 27 Jun 2017 15:51:18
s.A_flux
#[Out]# 0
# Tue, 27 Jun 2017 15:51:19
s.A_flux = 1
# Tue, 27 Jun 2017 15:51:22
s.A_flux = 10
# Tue, 27 Jun 2017 15:51:24
s.A_flux = 8
# Tue, 27 Jun 2017 15:51:34
s.reset()
# Tue, 27 Jun 2017 15:51:41
s.S_bias = 1400
# Tue, 27 Jun 2017 15:51:42
s.reset()
# Tue, 27 Jun 2017 15:51:47
s.S_bias = 1350
# Tue, 27 Jun 2017 15:51:50
s.S_bias = 1450
# Tue, 27 Jun 2017 15:51:53
s.S_bias = 1480
# Tue, 27 Jun 2017 15:51:56
s.S_bias = 1450
# Tue, 27 Jun 2017 15:52:01
s.A_flux
#[Out]# 8
# Tue, 27 Jun 2017 15:52:03
s.A_flux = 10
# Tue, 27 Jun 2017 15:52:05
s.A_flux = 5
# Tue, 27 Jun 2017 15:52:07
s.A_flux = 7
# Tue, 27 Jun 2017 15:52:15
s.lock('Squid')
# Tue, 27 Jun 2017 15:52:19
s.reset()
# Tue, 27 Jun 2017 15:52:26
s.S_flux
#[Out]# 0
# Tue, 27 Jun 2017 15:52:28
s.S_flux = 1
# Tue, 27 Jun 2017 15:52:32
s.S_flux = 10
# Tue, 27 Jun 2017 15:52:34
s.reset()
# Tue, 27 Jun 2017 15:52:36
s.reset()
# Tue, 27 Jun 2017 15:52:37
s.reset()
# Tue, 27 Jun 2017 15:52:40
s.S_flux = 50
# Tue, 27 Jun 2017 15:52:42
s.reset()
# Tue, 27 Jun 2017 15:52:58
s.S_flux = 70
# Tue, 27 Jun 2017 15:53:01
s.S_flux = 0
# Tue, 27 Jun 2017 15:53:09
s.reset()
# Tue, 27 Jun 2017 15:53:10
s.reset()
# Tue, 27 Jun 2017 15:53:13
s.S_flux = 50
# Tue, 27 Jun 2017 15:53:15
s.reset()
# Tue, 27 Jun 2017 15:53:19
s.S_flux = 100
# Tue, 27 Jun 2017 15:53:28
s.testSignal='Off'
# Tue, 27 Jun 2017 15:53:30
s.reset()
# Tue, 27 Jun 2017 15:53:57
s.testSignal='On'
# Tue, 27 Jun 2017 15:54:05
s.lock('Array')
# Tue, 27 Jun 2017 15:54:22
s.A_flux
#[Out]# 7
# Tue, 27 Jun 2017 15:54:24
s.A_flux = 8
# Tue, 27 Jun 2017 15:54:33
s.S_flux
#[Out]# 100
# Tue, 27 Jun 2017 15:54:36
s.S_flux = 50
# Tue, 27 Jun 2017 15:54:44
s.lock('Squid')
# Tue, 27 Jun 2017 15:54:46
s.reset()
# Tue, 27 Jun 2017 15:54:47
s.reset()
# Tue, 27 Jun 2017 15:54:48
s.reset()
# Tue, 27 Jun 2017 15:54:49
s.reset()
# Tue, 27 Jun 2017 15:55:00
s.S_flux = 0
# Tue, 27 Jun 2017 17:02:56
s.reset()
# Tue, 27 Jun 2017 17:03:04
s.testSignal='Off'
# Tue, 27 Jun 2017 17:03:17
s.S_flux
#[Out]# 0
# Tue, 27 Jun 2017 17:03:19
s.S_flux = 1
# Tue, 27 Jun 2017 17:03:22
s.S_flux = 10
# Tue, 27 Jun 2017 17:03:25
s.S_flux = 20
# Tue, 27 Jun 2017 17:03:28
s.S_flux = 30
# Tue, 27 Jun 2017 17:03:38
s.S_flux = 31
# Tue, 27 Jun 2017 17:03:40
s.S_flux = 32
# Tue, 27 Jun 2017 17:03:42
s.S_flux = 33
# Tue, 27 Jun 2017 17:03:43
s.S_flux = 34
# Tue, 27 Jun 2017 17:03:45
s.S_flux = 35
# Tue, 27 Jun 2017 17:04:05
pa.__getstate__()
#[Out]# {'dccoupled': True, 'filter': (1000, 10000), 'gain': 100, 'overloaded': False}
# Tue, 27 Jun 2017 17:04:13
get_ipython().magic('load qtconsole/2017/06/setups/annotatedspectrum_20170626.py')
# Tue, 27 Jun 2017 17:04:23
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Tue, 27 Jun 2017 17:05:49
s.__getstate__()
#[Out]# {'Array bias': 41,
#[Out]#  'Array flux': 8,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.2,
#[Out]#  'SQUID bias': 1450,
#[Out]#  'SQUID flux': 35,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Tue, 27 Jun 2017 17:06:01
s.testSignal='On'
# Tue, 27 Jun 2017 17:06:16
s.testSignal='off'
# Tue, 27 Jun 2017 17:06:19
s.testSignal='Off'
# Tue, 27 Jun 2017 17:06:54
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 30, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Tue, 27 Jun 2017 17:32:07
s.lock('Array')
# Tue, 27 Jun 2017 17:32:17
s.testSignal = 'On'
# Tue, 27 Jun 2017 17:32:44
s.lock('Squid')
# Tue, 27 Jun 2017 17:32:52
s.S_flux
#[Out]# 35
# Tue, 27 Jun 2017 17:32:58
s.testSignal='Off'
# Tue, 27 Jun 2017 17:33:10
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Tue, 27 Jun 2017 17:39:22
s.zero()
# Tue, 27 Jun 2017 17:39:26
z.__getstate__()
# Tue, 27 Jun 2017 17:39:31
z.__getstatus__()
# Tue, 27 Jun 2017 17:39:40
s.__getstate__()
#[Out]# {'Array bias': 0,
#[Out]#  'Array flux': 0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
