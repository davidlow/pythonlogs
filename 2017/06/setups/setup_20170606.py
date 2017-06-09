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

s = SquidArray.load()

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
