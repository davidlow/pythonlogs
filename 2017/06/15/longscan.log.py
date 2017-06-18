# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Fri, 16 Jun 2017 04:27:29
get_ipython().magic('load qtconsole/2017/06/setups/main_20170613.py')
# Fri, 16 Jun 2017 04:27:31
# %load qtconsole/2017/06/setups/main_20170613.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170613.py')

# Fri, 16 Jun 2017 04:27:44
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_20170609.py')

# Fri, 16 Jun 2017 04:27:48
pf = Planefit.load()
# Fri, 16 Jun 2017 04:27:52
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_20170609.py')

# Fri, 16 Jun 2017 17:54:33
s.sensitivity
#[Out]# 'Med'
# Fri, 16 Jun 2017 17:54:45
s.lock('array')
# Fri, 16 Jun 2017 17:54:49
s.reset()
# Fri, 16 Jun 2017 17:54:56
s.__getstatus__()
# Fri, 16 Jun 2017 17:55:00
s.__getstate__()
#[Out]# {'Array bias': 43,
#[Out]#  'Array flux': 2,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '10kOhm',
#[Out]#  'Integrator capacitor': '15nF',
#[Out]#  'Preamp voltage offset': 0.2,
#[Out]#  'SQUID bias': 400,
#[Out]#  'SQUID flux': 12,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'Med'}
# Fri, 16 Jun 2017 17:55:09
s.S_bias
#[Out]# 400
# Fri, 16 Jun 2017 17:55:11
s.S_bias=0
# Fri, 16 Jun 2017 17:55:14
s.reset()
# Fri, 16 Jun 2017 17:55:20
s.sensitivity='High'
# Fri, 16 Jun 2017 17:55:28
s.reset()
# Fri, 16 Jun 2017 17:59:48
15.47*100*1e-3
#[Out]# 1.547
# Fri, 16 Jun 2017 17:59:52
15.47*10*1e-3
#[Out]# 0.15470000000000003
# Fri, 16 Jun 2017 17:59:55
15.47*1*1e-3
#[Out]# 0.015470000000000001
# Fri, 16 Jun 2017 18:02:05
from Nowack_Lab.Utilities import conversions
# Fri, 16 Jun 2017 18:02:08
reload
#[Out]# <function imp.reload>
# Fri, 16 Jun 2017 18:02:21
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Fri, 16 Jun 2017 18:02:30
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
