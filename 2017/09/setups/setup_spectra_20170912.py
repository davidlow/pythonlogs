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

import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.preamp
import Nowack_Lab.Instruments.squidarray

from Nowack_Lab.Instruments.nidaq           import NIDAQ
from Nowack_Lab.Instruments.squidarray      import SquidArray
from Nowack_Lab.Instruments.preamp          import SR5113
from Nowack_Lab.Instruments.preamp          import FakeSR5113


import Nowack_Lab.Procedures.daqspectrum

from Nowack_Lab.Procedures.daqspectrum      import DaqSpectrum
from Nowack_Lab.Procedures.daqspectrum      import SQUIDSpectrum
from Nowack_Lab.Procedures.daqspectrum      import AnnotatedSpectrum


from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()


# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")

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
pa = FakeSR5113()
#liC = SR830(gpib_address=12)
#liS = SR830(gpib_address=15)

s = SquidArray.load(visaResource='COM1')

# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
    'preamp': pa,
    'squidarray': s
}
