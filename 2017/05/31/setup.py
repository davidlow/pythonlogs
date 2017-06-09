from matplotlib import pyplot as plt
plt.ion()
from Nowack_Lab.Instruments import NIDAQ, SR830, SR5113, Piezos, Montana, Attocube, SquidArray
from Nowack_Lab.Procedures import Planefit

daq = NIDAQ(dev_name="Dev2")
daq.outputs = {
    'x':0,
    'y':1,
    'z':2
}
daq.inputs = {
    'cap':0,
    'theta':1,
    'capx':2, #nothing connected?
    'capy':3, #nothing connected?
    'acx':4,
    'acy':5,
    'dc':6
}

pa = SR5113(port="COM3")
pa = SR5113(port="COM2")
pa = SR5113(port="COM3")

liC = SR830(gpib_address=12)
liS = SR830(gpib_address=13)

pz = Piezos(daq)
montana = Montana()
atto = Attocube(montana)

s = SquidArray(visaResource='COM1')

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