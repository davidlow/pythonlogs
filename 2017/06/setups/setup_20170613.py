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

s = SquidArray.load(visaResource='COM1')

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
