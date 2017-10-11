from matplotlib import pyplot as plt
plt.ion()
#plt.style.use("notebook")


import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.preamp
import Nowack_Lab.Instruments.lakeshore


from Nowack_Lab.Instruments.nidaq            import NIDAQ
from Nowack_Lab.Instruments.preamp           import SR5113
from Nowack_Lab.Instruments.lakeshore        import Lakeshore372



import Nowack_Lab.Procedures.daqtransport

from Nowack_Lab.Procedures.daqtransport     import DAQ_Transport


# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")
daq.outputs = {
#    'x':0,
#    'y':1,
#    'z':2
     'bias':3
}
daq.inputs = {
#    'cap':0,
#    'theta':1,
#    'capx':2, # disconnected
#    'capy':3, # disconnected
#    'acx':4,
#    'acy':5,
    #'dc':6
     'voltage':7
}

# Initialize other measurement equipment
pa = SR5113(port="COM3")
#liC = SR830(gpib_address=12)
#liS = SR830(gpib_address=13)
#pz = Piezos(daq)
#montana = Montana()
#atto = Attocube(montana)

#s = SquidArray.load(visaResource='COM1')
l = Lakeshore372()

# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
#    'montana':montana,
#    'piezos':pz,
#    'lockin_cap':liC,
#    'atto': atto,
    'preamp': pa,
#    'lockin_squid': liS,
#    'squidarray': s
     'lakeshore': l
}
