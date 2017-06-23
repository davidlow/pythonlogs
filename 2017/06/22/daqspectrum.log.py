# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Thu, 22 Jun 2017 20:54:37
s = SquidArray(visaResource='COM1')
# Thu, 22 Jun 2017 20:54:55
get_ipython().magic('load qtconsole/2017/06/setups/main_20170622.py')
# Thu, 22 Jun 2017 20:55:10
get_ipython().magic('load qtconsole/2017/06/setups/setup_20170622.py')
# Thu, 22 Jun 2017 20:55:11
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

# Thu, 22 Jun 2017 20:55:49
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
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Thu, 22 Jun 2017 20:55:56
s.reset()
# Thu, 22 Jun 2017 20:56:06
s.A_bias = 42
# Thu, 22 Jun 2017 20:56:21
s.testSignal
#[Out]# 'Off'
# Thu, 22 Jun 2017 20:56:23
s.testSignal = 'On'
# Thu, 22 Jun 2017 20:56:27
s.testInput
#[Out]# 'S_flux'
# Thu, 22 Jun 2017 20:56:33
s.testInput = 'A_flux'
# Thu, 22 Jun 2017 20:56:40
s.A_bias= 43
# Thu, 22 Jun 2017 20:56:45
s.A_bias= 44
# Thu, 22 Jun 2017 20:56:47
s.A_bias= 45
# Thu, 22 Jun 2017 20:56:49
s.A_bias= 44
# Thu, 22 Jun 2017 20:56:56
s.offset
#[Out]# 0
# Thu, 22 Jun 2017 20:57:20
s.lock('Array')
# Thu, 22 Jun 2017 20:57:24
s.reset()
# Thu, 22 Jun 2017 20:57:28
s.sensitivity
#[Out]# 'Med'
# Thu, 22 Jun 2017 20:57:31
s.sensitivity = 'High'
# Thu, 22 Jun 2017 20:57:34
s.reset()
# Thu, 22 Jun 2017 20:57:37
s.reset()
# Thu, 22 Jun 2017 20:57:38
s.reset()
# Thu, 22 Jun 2017 20:57:45
s.A_bias
#[Out]# 44
# Thu, 22 Jun 2017 20:57:48
s.A_flux
#[Out]# 0
# Thu, 22 Jun 2017 20:57:51
s.A_flux = 5
# Thu, 22 Jun 2017 20:57:55
s.reset()
# Thu, 22 Jun 2017 20:57:56
s.reset()
# Thu, 22 Jun 2017 20:58:02
s.A_flux = 6
# Thu, 22 Jun 2017 20:58:05
s.A_flux = 7
# Thu, 22 Jun 2017 20:58:07
s.A_flux = 8
# Thu, 22 Jun 2017 20:58:18
s.testInput
#[Out]# 'A_flux'
# Thu, 22 Jun 2017 20:58:22
s.testInput = 'S_flux'
# Thu, 22 Jun 2017 20:58:34
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 8,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 20:58:49
s.S_bias
#[Out]# 0
# Thu, 22 Jun 2017 20:58:52
s.S_bias = 10
# Thu, 22 Jun 2017 20:58:55
s.S_bias = 100
# Thu, 22 Jun 2017 20:58:59
s.reset()
# Thu, 22 Jun 2017 20:59:09
s.S_bias = 150
# Thu, 22 Jun 2017 20:59:13
s.S_bias = 20
# Thu, 22 Jun 2017 20:59:26
s.S_bias = 200
# Thu, 22 Jun 2017 20:59:30
s.S_bias = 250
# Thu, 22 Jun 2017 20:59:33
s.S_bias = 300
# Thu, 22 Jun 2017 20:59:43
s.S_bias = 310
# Thu, 22 Jun 2017 20:59:47
s.S_bias = 320
# Thu, 22 Jun 2017 20:59:49
s.S_bias = 330
# Thu, 22 Jun 2017 20:59:53
s.S_bias = 340
# Thu, 22 Jun 2017 21:00:00
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:02
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:03
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:03
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:04
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:04
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:04
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:05
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:05
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:05
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:05
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:06
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:06
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:06
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:08
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:08
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:08
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:08
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:09
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:09
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:09
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:10
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:10
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:11
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:00:15
s.reset()
# Thu, 22 Jun 2017 21:00:19
s.S_bias
#[Out]# 620
# Thu, 22 Jun 2017 21:00:23
s.S_bias = 700
# Thu, 22 Jun 2017 21:00:26
s.reset()
# Thu, 22 Jun 2017 21:00:30
s.S_bias = 710
# Thu, 22 Jun 2017 21:00:33
s.S_bias = 740
# Thu, 22 Jun 2017 21:00:36
s.S_bias = 760
# Thu, 22 Jun 2017 21:00:39
s.S_bias = 780
# Thu, 22 Jun 2017 21:00:42
s.S_bias = 800
# Thu, 22 Jun 2017 21:00:55
s.S_bias = 900
# Thu, 22 Jun 2017 21:00:59
s.S_bias = 1000
# Thu, 22 Jun 2017 21:01:05
s.S_bias_lim
#[Out]# 2000
# Thu, 22 Jun 2017 21:01:10
s.S_bias = 1100
# Thu, 22 Jun 2017 21:01:13
s.S_bias = 1200
# Thu, 22 Jun 2017 21:01:17
s.S_bias = 1300
# Thu, 22 Jun 2017 21:01:19
s.reset()
# Thu, 22 Jun 2017 21:01:23
s.S_bias = 1400
# Thu, 22 Jun 2017 21:01:27
s.S_bias = 1500
# Thu, 22 Jun 2017 21:01:35
s.S_bias = 200
# Thu, 22 Jun 2017 21:01:38
s.reset()
# Thu, 22 Jun 2017 21:01:50
s.S_bias = 190
# Thu, 22 Jun 2017 21:01:53
s.S_bias = 180
# Thu, 22 Jun 2017 21:01:56
s.S_bias = 170
# Thu, 22 Jun 2017 21:02:00
s.S_bias = 160
# Thu, 22 Jun 2017 21:02:03
s.S_bias = 150
# Thu, 22 Jun 2017 21:02:06
s.S_bias = 120
# Thu, 22 Jun 2017 21:02:09
s.S_bias = 110
# Thu, 22 Jun 2017 21:02:11
s.S_bias = 100
# Thu, 22 Jun 2017 21:02:21
s.S_bias = 50
# Thu, 22 Jun 2017 21:02:24
s.S_bias = 20
# Thu, 22 Jun 2017 21:02:27
s.S_bias = 30
# Thu, 22 Jun 2017 21:02:29
s.S_bias = 40
# Thu, 22 Jun 2017 21:02:34
s.S_bias = 80
# Thu, 22 Jun 2017 21:02:37
s.S_bias = 100
# Thu, 22 Jun 2017 21:02:41
s.S_bias = 130
# Thu, 22 Jun 2017 21:02:43
s.S_bias = 140
# Thu, 22 Jun 2017 21:02:45
s.S_bias = 150
# Thu, 22 Jun 2017 21:02:48
s.S_bias = 170
# Thu, 22 Jun 2017 21:02:53
s.S_bias = 200
# Thu, 22 Jun 2017 21:02:56
s.S_bias = 210
# Thu, 22 Jun 2017 21:02:58
s.S_bias = 220
# Thu, 22 Jun 2017 21:03:05
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:07
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:08
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:11
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:14
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:15
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:16
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:03:22
s.S_bias = s.S_bias - 10
# Thu, 22 Jun 2017 21:03:37
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:38
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:38
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:39
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:40
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:41
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:41
s.S_bias = s.S_bias - 1
# Thu, 22 Jun 2017 21:03:48
s.reset()
# Thu, 22 Jun 2017 21:03:54
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:03:57
s.reset()
# Thu, 22 Jun 2017 21:04:08
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:09
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:09
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:10
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:10
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:11
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:11
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:12
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:13
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:13
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:16
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:18
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:18
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:19
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:19
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:19
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:20
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:20
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:21
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:23
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:25
s.S_bias = s.S_bias - 5
# Thu, 22 Jun 2017 21:04:29
s.S_bias = s.S_bias + 5
# Thu, 22 Jun 2017 21:04:31
s.reset()
# Thu, 22 Jun 2017 21:04:35
s.S_bias
#[Out]# 288
# Thu, 22 Jun 2017 21:04:51
s.S_bias - 10
#[Out]# 278
# Thu, 22 Jun 2017 21:04:59
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:02
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:02
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:03
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:04
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:04
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:05
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:06
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:06
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:07
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:07
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:09
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:09
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:10
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:10
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:10
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:11
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:11
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:12
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:12
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:12
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:13
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:13
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:14
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:14
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:15
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:15
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:16
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:18
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:19
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:21
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:24
s.reset()
# Thu, 22 Jun 2017 21:05:28
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:30
s.reset()
# Thu, 22 Jun 2017 21:05:32
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:34
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:37
s.reset()
# Thu, 22 Jun 2017 21:05:39
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:40
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:41
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:41
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:42
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:42
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:43
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:44
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:45
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:45
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:46
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:47
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:48
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:49
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:51
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:52
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:53
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:05:55
s.reset()
# Thu, 22 Jun 2017 21:05:57
s.reset()
# Thu, 22 Jun 2017 21:05:58
s.reset()
# Thu, 22 Jun 2017 21:06:00
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:00
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:01
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:04
s.reset()
# Thu, 22 Jun 2017 21:06:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:15
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:16
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:17
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:17
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:18
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:18
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:19
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:19
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:20
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:21
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:21
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:22
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:23
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:24
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:24
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:25
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:26
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:40
s.reset()
# Thu, 22 Jun 2017 21:06:42
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:43
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:44
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:44
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:45
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:46
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:47
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:47
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:48
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:48
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:49
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:49
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:50
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:51
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:51
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:53
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:06:54
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:06
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:07
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:07
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:08
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:09
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:09
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:10
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:10
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:11
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:12
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:12
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:13
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:13
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:14
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:15
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:15
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:16
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:16
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:07:40
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:40
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:41
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:42
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:42
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:43
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:44
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:45
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:45
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:46
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:46
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:47
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:48
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:48
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:49
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:50
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:50
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:51
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:52
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:53
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:07:54
s.S_bias = s.S_bias -  10
# Thu, 22 Jun 2017 21:08:07
s.reset()
# Thu, 22 Jun 2017 21:08:12
s.S_bias
#[Out]# 1188
# Thu, 22 Jun 2017 21:10:19
s.S_bias = 10
# Thu, 22 Jun 2017 21:10:21
s.reset()
# Thu, 22 Jun 2017 21:10:28
s.S_bias = s.S_bias +  10
# Thu, 22 Jun 2017 21:10:35
s.reset()
# Thu, 22 Jun 2017 21:10:38
s.reset()
# Thu, 22 Jun 2017 21:10:38
s.reset()
# Thu, 22 Jun 2017 21:10:42
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:45
s.reset()
# Thu, 22 Jun 2017 21:10:50
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:51
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:52
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:55
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:55
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:56
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:57
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:57
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:58
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:58
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:59
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:59
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:10:59
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:00
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:01
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:01
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:02
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:02
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:03
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:03
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:04
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:04
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:05
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:05
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:06
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:06
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:07
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:07
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:08
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:08
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:09
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:09
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:10
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:10
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:11
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:11
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:12
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:13
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:13
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:14
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:14
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:15
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:15
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:16
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:16
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:25
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:26
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:26
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:27
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:27
s.S_bias = s.S_bias +  5
# Thu, 22 Jun 2017 21:11:31
s.S_bias = s.S_bias 1  5
# Thu, 22 Jun 2017 21:11:34
s.S_bias = s.S_bias -  5
# Thu, 22 Jun 2017 21:11:35
s.S_bias = s.S_bias -  5
# Thu, 22 Jun 2017 21:11:38
s.reset()
# Thu, 22 Jun 2017 21:12:06
s.A_bias
#[Out]# 44
# Thu, 22 Jun 2017 21:12:08
s.A_flux
#[Out]# 8
# Thu, 22 Jun 2017 21:12:11
s.A_flux = 10
# Thu, 22 Jun 2017 21:12:14
s.A_flux = 6
# Thu, 22 Jun 2017 21:12:25
s.S_bias
#[Out]# 265
# Thu, 22 Jun 2017 21:12:52
s.A_flux
#[Out]# 6
# Thu, 22 Jun 2017 21:13:04
s.A_bias
#[Out]# 44
# Thu, 22 Jun 2017 21:13:38
s.S_bias
#[Out]# 265
# Thu, 22 Jun 2017 21:13:47
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:13:48
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:13:51
s.reset()
# Thu, 22 Jun 2017 21:13:54
s.reset()
# Thu, 22 Jun 2017 21:13:55
s.S_bias = s.S_bias + 10
# Thu, 22 Jun 2017 21:13:57
s.reset()
# Thu, 22 Jun 2017 21:14:00
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:01
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:01
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:02
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:02
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:03
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:03
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:04
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:04
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:05
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:05
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:06
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:06
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:06
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:07
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:07
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:08
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:08
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:09
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:09
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:10
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:10
s.S_bias = s.S_bias + 1
# Thu, 22 Jun 2017 21:14:13
s.S_bias = s.S_bias -10
# Thu, 22 Jun 2017 21:14:15
s.S_bias = s.S_bias -10
# Thu, 22 Jun 2017 21:14:16
s.S_bias = s.S_bias -10
# Thu, 22 Jun 2017 21:14:17
s.S_bias = s.S_bias -10
# Thu, 22 Jun 2017 21:14:20
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:21
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:21
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:24
s.reset()
# Thu, 22 Jun 2017 21:14:34
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:35
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:36
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:36
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:37
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:38
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:38
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:39
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:39
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:40
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:41
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:41
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:42
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:42
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:43
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:43
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:44
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:44
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:45
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:46
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:46
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:47
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:47
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:14:51
s.reset()
# Thu, 22 Jun 2017 21:14:58
s.S_bias = s.S_bias +2
# Thu, 22 Jun 2017 21:15:00
s.reset()
# Thu, 22 Jun 2017 21:15:08
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 6,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 539,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 21:15:14
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:15:16
s.reset()
# Thu, 22 Jun 2017 21:15:18
s.reset()
# Thu, 22 Jun 2017 21:15:25
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:28
s.reset()
# Thu, 22 Jun 2017 21:15:35
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:36
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:36
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:37
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:37
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:37
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:38
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:38
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:38
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:39
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:39
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:40
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:42
s.reset()
# Thu, 22 Jun 2017 21:15:44
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:45
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:45
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:46
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:46
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:46
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:15:48
s.reset()
# Thu, 22 Jun 2017 21:16:27
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 6,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 644,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 21:17:51
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:52
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:54
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:55
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:55
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:56
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:56
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:57
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:57
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:58
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:58
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:59
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:17:59
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:00
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:00
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:01
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:02
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:03
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:07
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:08
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:08
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:08
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:09
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:10
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:11
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:11
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:12
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:13
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:13
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:14
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:14
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:15
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:15
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:16
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:16
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:17
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:17
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:18
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:18
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:19
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:19
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:20
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:20
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:20
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:21
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:21
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:22
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:22
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:22
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:23
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:23
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:23
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:24
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:24
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:24
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:24
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:24
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:25
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:25
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:25
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:25
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:26
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:26
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:26
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:26
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:27
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:27
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:27
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:28
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:28
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:28
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:28
s.S_bias = s.S_bias +5
# Thu, 22 Jun 2017 21:18:36
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:36
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:37
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:38
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:38
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:39
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:39
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:42
s.reset()
# Thu, 22 Jun 2017 21:18:44
s.reset()
# Thu, 22 Jun 2017 21:18:46
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:47
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:48
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:51
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:52
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:53
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:54
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:54
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:55
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:55
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:56
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:57
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:18:58
s.S_bias = s.S_bias +10
# Thu, 22 Jun 2017 21:19:02
s.S_bias = s.S_bias 110
# Thu, 22 Jun 2017 21:19:05
s.S_bias = s.S_bias -10
# Thu, 22 Jun 2017 21:19:11
s.reset()
# Thu, 22 Jun 2017 21:19:17
s.A_flux
#[Out]# 6
# Thu, 22 Jun 2017 21:19:19
s.A_flux = 10
# Thu, 22 Jun 2017 21:19:33
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 10,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 1194,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 21:20:53
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:54
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:20:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:01
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:01
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:02
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:02
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:02
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:03
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:21:13
s.reset()
# Thu, 22 Jun 2017 21:21:17
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 10,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 1424,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 21:22:32
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:33
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:36
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:36
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:37
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:38
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:38
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:39
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:39
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:40
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:41
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:42
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:42
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:43
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:43
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:44
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:44
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:45
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:45
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:45
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:46
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:46
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:47
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:47
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:48
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:48
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:51
s.reset()
# Thu, 22 Jun 2017 21:22:53
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:54
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:54
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:55
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:56
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:57
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:58
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:22:59
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:00
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:05
s.S_bias
#[Out]# 1974
# Thu, 22 Jun 2017 21:23:08
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:08
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:09
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:09
s.S_bias = s.S_bias  + 10
# Thu, 22 Jun 2017 21:23:18
s.S_bias = 0
# Thu, 22 Jun 2017 21:23:20
s.reset()
# Thu, 22 Jun 2017 21:23:22
s.reset()
# Thu, 22 Jun 2017 21:23:22
s.reset()
# Thu, 22 Jun 2017 21:23:52
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 10,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 21:24:06
s.testSignal = 'Off'
# Thu, 22 Jun 2017 21:24:09
s.reset()
# Thu, 22 Jun 2017 21:24:13
s.A_flux
#[Out]# 10
# Thu, 22 Jun 2017 21:24:16
s.A_flux = 6
# Thu, 22 Jun 2017 21:24:21
s.reset()
# Thu, 22 Jun 2017 21:24:32
s.A_flux = 5.5
# Thu, 22 Jun 2017 21:24:36
s.A_flux = 5.3
# Thu, 22 Jun 2017 21:25:02
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xccabf60>
# Thu, 22 Jun 2017 21:25:04
pa.gain
#[Out]# 500
# Thu, 22 Jun 2017 21:25:15
instruments['squidarray'] = s
# Thu, 22 Jun 2017 21:27:46
spectrum = AnnotatedSpectrum(1,instruments, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False) 
# Thu, 22 Jun 2017 21:27:50
spectrum.run()
# Thu, 22 Jun 2017 21:31:41
reload(Nowack_lab.Procedures.daqspectrum)
# Thu, 22 Jun 2017 21:31:52
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Thu, 22 Jun 2017 21:32:05
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Thu, 22 Jun 2017 21:32:27
spectrum = AnnotatedSpectrum(1,instruments, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False)
# Thu, 22 Jun 2017 21:32:33
spectrum.arrayspectra()
# Thu, 22 Jun 2017 21:32:39
spectrum.run()
# Thu, 22 Jun 2017 21:34:53
spectrum = AnnotatedSpectrum(1,instruments, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotoate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 21:35:05
spectrum = AnnotatedSpectrum(1,instruments, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 21:35:07
spectrum.arrayspectra()
# Thu, 22 Jun 2017 21:35:09
spectrum.run()
# Thu, 22 Jun 2017 21:37:32
reload(Nowack_lab.Procedures.daqspectrum)
# Thu, 22 Jun 2017 21:37:39
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Thu, 22 Jun 2017 21:37:42
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Thu, 22 Jun 2017 21:37:55
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 21:38:00
spectrum.arrayspectra()
# Thu, 22 Jun 2017 21:38:13
spectrum.notes = "magnet power supply on"
# Thu, 22 Jun 2017 21:38:16
spectrum.run()
# Thu, 22 Jun 2017 21:41:04
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 15, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 21:41:07
spectrum.arrayspectra()
# Thu, 22 Jun 2017 21:41:09
spectrum.notes = "magnet power supply on"
# Thu, 22 Jun 2017 21:41:11
spectrum.run()
# Thu, 22 Jun 2017 21:59:20
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 21:59:24
spectrum.notes = "magnet power supply off"
# Thu, 22 Jun 2017 21:59:28
spectrum.arrayspectra()
# Thu, 22 Jun 2017 21:59:33
spectrum.run()
# Thu, 22 Jun 2017 22:01:23
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 15, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:01:25
spectrum.arrayspectra()
# Thu, 22 Jun 2017 22:01:28
spectrum.notes = "magnet power supply off"
# Thu, 22 Jun 2017 22:01:30
spectrum.run()
# Thu, 22 Jun 2017 22:11:04
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 5.3,
#[Out]#  'Array locked': True,
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
# Thu, 22 Jun 2017 22:11:13
s.testSignal = 'On'
# Thu, 22 Jun 2017 22:11:43
s.S_bias = 265
# Thu, 22 Jun 2017 22:11:46
s.reset()
# Thu, 22 Jun 2017 22:12:07
s.A_bias
#[Out]# 44
# Thu, 22 Jun 2017 22:12:11
s.A_flux
#[Out]# 5.3
# Thu, 22 Jun 2017 22:12:15
s.A_flux = 5.2
# Thu, 22 Jun 2017 22:12:17
s.A_flux = 5.4
# Thu, 22 Jun 2017 22:12:23
s.A_flux = 5.7
# Thu, 22 Jun 2017 22:12:32
s.A_flux = 5.9
# Thu, 22 Jun 2017 22:12:42
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:12:53
s.lock('Squid')
# Thu, 22 Jun 2017 22:13:07
s.reset()
# Thu, 22 Jun 2017 22:13:08
s.reset()
# Thu, 22 Jun 2017 22:13:09
s.reset()
# Thu, 22 Jun 2017 22:13:10
s.reset()
# Thu, 22 Jun 2017 22:13:10
s.reset()
# Thu, 22 Jun 2017 22:13:11
s.reset()
# Thu, 22 Jun 2017 22:13:20
s.S_flux
#[Out]# 0
# Thu, 22 Jun 2017 22:13:23
s.S_flux = 10
# Thu, 22 Jun 2017 22:13:26
s.S_flux = 30
# Thu, 22 Jun 2017 22:13:28
s.S_flux = 100
# Thu, 22 Jun 2017 22:13:33
s.S_flux = 50
# Thu, 22 Jun 2017 22:13:35
s.reset()
# Thu, 22 Jun 2017 22:13:41
s.testSignal
#[Out]# 'On'
# Thu, 22 Jun 2017 22:13:44
s.testSignal = 'Off'
# Thu, 22 Jun 2017 22:13:47
s.reset()
# Thu, 22 Jun 2017 22:13:55
s.S_flux = 70
# Thu, 22 Jun 2017 22:13:58
s.S_flux = 80
# Thu, 22 Jun 2017 22:14:03
s.S_flux = 81
# Thu, 22 Jun 2017 22:14:07
s.S_flux = 82
# Thu, 22 Jun 2017 22:14:41
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:14:56
spectrum.notes = 'magnet power supply off'
# Thu, 22 Jun 2017 22:15:01
spectrum.run()
# Thu, 22 Jun 2017 22:18:58
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:19:05
spectrum.notes = 'magnet power supply on'
# Thu, 22 Jun 2017 22:19:09
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:19:13
spectrum.run()
# Thu, 22 Jun 2017 22:22:53
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 5.9,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 265,
#[Out]#  'SQUID flux': 82,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 22:23:15
s.lock('Array')
# Thu, 22 Jun 2017 22:23:26
s.testSignal = 'On'
# Thu, 22 Jun 2017 22:23:28
s.reset()
# Thu, 22 Jun 2017 22:23:31
s.reset()
# Thu, 22 Jun 2017 22:23:53
s.reset()
# Thu, 22 Jun 2017 22:24:07
s.lock('Squid')
# Thu, 22 Jun 2017 22:24:13
s.testSignal='Off'
# Thu, 22 Jun 2017 22:24:23
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:24:28
spectrum.notes = 'magnet power supply on'
# Thu, 22 Jun 2017 22:24:33
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:24:36
spectrum.run()
# Thu, 22 Jun 2017 22:29:56
s.lock('Array')
# Thu, 22 Jun 2017 22:30:01
s.testSignal='On'
# Thu, 22 Jun 2017 22:30:03
s.reset()
# Thu, 22 Jun 2017 22:30:10
s.S_bias
#[Out]# 265
# Thu, 22 Jun 2017 22:30:20
s.S_bias = 644
# Thu, 22 Jun 2017 22:30:22
s.reset
#[Out]# <bound method PFL102.reset of <Nowack_Lab.Instruments.squidarray.SquidArray object at 0x000000000CCADDA0>>
# Thu, 22 Jun 2017 22:30:24
s.reset()
# Thu, 22 Jun 2017 22:30:26
s.reset()
# Thu, 22 Jun 2017 22:30:40
s.reset()
# Thu, 22 Jun 2017 22:30:42
s.reset()
# Thu, 22 Jun 2017 22:30:43
s.reset()
# Thu, 22 Jun 2017 22:30:54
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 5.9,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 644,
#[Out]#  'SQUID flux': 82,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'On',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Thu, 22 Jun 2017 22:31:03
s.A_flux=6
# Thu, 22 Jun 2017 22:31:05
s.reset()
# Thu, 22 Jun 2017 22:31:12
s.S_bias = 500
# Thu, 22 Jun 2017 22:31:15
s.reset()
# Thu, 22 Jun 2017 22:31:17
s.reset()
# Thu, 22 Jun 2017 22:31:22
s.S_bias = 600
# Thu, 22 Jun 2017 22:31:25
s.reset()
# Thu, 22 Jun 2017 22:31:28
s.reset()
# Thu, 22 Jun 2017 22:31:41
s.S_bias = 610
# Thu, 22 Jun 2017 22:31:43
s.S_bias = 620
# Thu, 22 Jun 2017 22:31:45
s.reset()
# Thu, 22 Jun 2017 22:31:49
s.S_bias = 640
# Thu, 22 Jun 2017 22:31:51
s.reset()
# Thu, 22 Jun 2017 22:31:54
s.S_bias = 650
# Thu, 22 Jun 2017 22:31:59
s.S_bias = 660
# Thu, 22 Jun 2017 22:32:01
s.reset()
# Thu, 22 Jun 2017 22:32:04
s.S_bias = 670
# Thu, 22 Jun 2017 22:32:06
s.reset()
# Thu, 22 Jun 2017 22:32:10
s.S_bias = 680
# Thu, 22 Jun 2017 22:32:12
s.reset()
# Thu, 22 Jun 2017 22:32:16
s.S_bias = 690
# Thu, 22 Jun 2017 22:32:28
s.S_bias = 640
# Thu, 22 Jun 2017 22:32:31
s.reset()
# Thu, 22 Jun 2017 22:32:33
s.reset()
# Thu, 22 Jun 2017 22:32:35
s.S_bias = 644
# Thu, 22 Jun 2017 22:32:39
s.S_bias = 694
# Thu, 22 Jun 2017 22:32:41
s.reset()
# Thu, 22 Jun 2017 22:33:01
s.A_flux
#[Out]# 6
# Thu, 22 Jun 2017 22:33:03
s.A_flux = 8
# Thu, 22 Jun 2017 22:33:06
s.A_flux = 4
# Thu, 22 Jun 2017 22:33:11
s.A_flux = 3
# Thu, 22 Jun 2017 22:33:16
s.A_flux = 2
# Thu, 22 Jun 2017 22:33:26
s.lock('Squid')
# Thu, 22 Jun 2017 22:33:34
s.testSignal='Off'
# Thu, 22 Jun 2017 22:33:35
s.rest
# Thu, 22 Jun 2017 22:33:39
s.reset()
# Thu, 22 Jun 2017 22:33:41
s.reset()
# Thu, 22 Jun 2017 22:33:45
s.S_flux
#[Out]# 82
# Thu, 22 Jun 2017 22:33:47
s.S_flux = 0
# Thu, 22 Jun 2017 22:33:49
s.reset()
# Thu, 22 Jun 2017 22:33:51
s.reset()
# Thu, 22 Jun 2017 22:33:54
s.S_flux = 10
# Thu, 22 Jun 2017 22:33:57
s.S_flux = 40
# Thu, 22 Jun 2017 22:34:07
s.reset()
# Thu, 22 Jun 2017 22:34:11
s.S_flux = 80
# Thu, 22 Jun 2017 22:34:16
s.reset()
# Thu, 22 Jun 2017 22:34:19
s.S_flux = 100
# Thu, 22 Jun 2017 22:34:25
s.reset()
# Thu, 22 Jun 2017 22:34:30
s.S_flux=50
# Thu, 22 Jun 2017 22:34:42
s.lock('Array')
# Thu, 22 Jun 2017 22:34:46
s.testSignal='On'
# Thu, 22 Jun 2017 22:34:55
s.S_bias=1194
# Thu, 22 Jun 2017 22:35:43
s.reset()
# Thu, 22 Jun 2017 22:35:53
s.A_flux
#[Out]# 2
# Thu, 22 Jun 2017 22:35:55
s.A_flux = 6
# Thu, 22 Jun 2017 22:35:59
s.A_flux = 10
# Thu, 22 Jun 2017 22:36:08
s.S_flux
#[Out]# 50
# Thu, 22 Jun 2017 22:36:10
s.S_flux = 0
# Thu, 22 Jun 2017 22:36:16
s.reset()
# Thu, 22 Jun 2017 22:36:20
s.lock('Squid')
# Thu, 22 Jun 2017 22:36:24
s.reset()
# Thu, 22 Jun 2017 22:36:25
s.reset()
# Thu, 22 Jun 2017 22:36:27
s.reset()
# Thu, 22 Jun 2017 22:36:28
s.reset()
# Thu, 22 Jun 2017 22:36:29
s.reset()
# Thu, 22 Jun 2017 22:36:36
s.S_flux = 50
# Thu, 22 Jun 2017 22:36:39
s.reset()
# Thu, 22 Jun 2017 22:36:45
s.S_flux = 40
# Thu, 22 Jun 2017 22:36:48
s.S_flux = 60
# Thu, 22 Jun 2017 22:36:51
s.S_flux = 65
# Thu, 22 Jun 2017 22:36:54
s.S_flux = 70
# Thu, 22 Jun 2017 22:37:01
s.testSignal='Off'
# Thu, 22 Jun 2017 22:37:07
s.S_flux
#[Out]# 70
# Thu, 22 Jun 2017 22:37:10
s.S_flux = 75
# Thu, 22 Jun 2017 22:37:31
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:37:35
spectrum.notes = 'magnet power supply on'
# Thu, 22 Jun 2017 22:37:39
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:37:45
spectrum.run()
# Thu, 22 Jun 2017 22:39:39
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 15, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:39:42
spectrum.notes = 'magnet power supply on'
# Thu, 22 Jun 2017 22:39:45
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:39:47
spectrum.run()
# Thu, 22 Jun 2017 22:54:23
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Thu, 22 Jun 2017 22:54:30
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Thu, 22 Jun 2017 22:54:40
spectrum = AnnotatedSpectrum(1,instruments, measure_time = 1, preamp_filter_override=True, preamp_dccouple_override=True, preamp_autoOL=False, annotate_piezos=False, annotate_cap = False)
# Thu, 22 Jun 2017 22:54:46
spectrum.notes = 'magnet power supply on'
# Thu, 22 Jun 2017 22:54:50
spectrum.squidspectra()
# Thu, 22 Jun 2017 22:54:53
spectrum.run()
# Thu, 22 Jun 2017 22:56:43
s.lock('Array')
# Thu, 22 Jun 2017 22:56:48
s.testSignal='On'
# Thu, 22 Jun 2017 22:57:11
s.S_bias=1424
# Thu, 22 Jun 2017 22:57:14
s.reset()
# Thu, 22 Jun 2017 22:57:22
s.A_flux
#[Out]# 10
# Thu, 22 Jun 2017 22:57:26
s.A_flux = 8
# Thu, 22 Jun 2017 22:57:30
s.A_flux = 9
# Thu, 22 Jun 2017 22:57:35
s.A_flux = 8.5
# Thu, 22 Jun 2017 22:57:45
s.lock('Squid')
# Thu, 22 Jun 2017 22:57:48
s.reset()
# Thu, 22 Jun 2017 22:57:49
s.reset()
# Thu, 22 Jun 2017 22:57:54
s.S_flux=50
# Thu, 22 Jun 2017 22:57:57
s.reset()
# Thu, 22 Jun 2017 22:58:14
s.S_flux = 40
# Thu, 22 Jun 2017 22:58:16
s.S_flux = 20
# Thu, 22 Jun 2017 22:58:24
s.reset()
# Thu, 22 Jun 2017 22:58:25
s.reset()
# Thu, 22 Jun 2017 22:58:25
s.reset()
# Thu, 22 Jun 2017 22:58:26
s.reset()
# Thu, 22 Jun 2017 22:58:29
s.S_flux = 0
# Thu, 22 Jun 2017 22:58:39
s.reset()
# Thu, 22 Jun 2017 22:58:43
s.S_flux=70
# Thu, 22 Jun 2017 22:58:46
s.reset()
# Thu, 22 Jun 2017 22:58:47
s.reset()
# Thu, 22 Jun 2017 22:58:48
s.reset()
# Thu, 22 Jun 2017 22:58:48
s.reset()
# Thu, 22 Jun 2017 22:58:49
s.reset()
# Thu, 22 Jun 2017 22:58:54
s.S_flux=40
# Thu, 22 Jun 2017 22:58:57
s.reset()
# Thu, 22 Jun 2017 22:58:58
s.reset()
# Thu, 22 Jun 2017 22:59:01
s.S_flux=0
# Thu, 22 Jun 2017 22:59:06
s.testSignal='Off'
# Thu, 22 Jun 2017 22:59:13
s.S_flux=100
# Thu, 22 Jun 2017 22:59:16
s.reset()
# Thu, 22 Jun 2017 22:59:17
s.reset()
# Thu, 22 Jun 2017 22:59:18
s.reset()
# Thu, 22 Jun 2017 22:59:19
s.reset()
# Thu, 22 Jun 2017 22:59:24
s.S_flux=90
# Thu, 22 Jun 2017 22:59:26
s.reset()
# Thu, 22 Jun 2017 22:59:28
s.reset()
# Thu, 22 Jun 2017 22:59:29
s.reset()
# Thu, 22 Jun 2017 22:59:33
s.S_flux=60
# Thu, 22 Jun 2017 22:59:36
s.S_flux=40
# Thu, 22 Jun 2017 22:59:38
s.S_flux=0
# Thu, 22 Jun 2017 22:59:40
s.reset()
# Thu, 22 Jun 2017 23:01:18
s.zero()
# Thu, 22 Jun 2017 23:01:25
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
# Thu, 22 Jun 2017 23:01:43
exit()
