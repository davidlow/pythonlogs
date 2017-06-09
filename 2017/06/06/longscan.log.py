# IPython log file

# Wed, 07 Jun 2017 05:36:19
get_ipython().magic('matplotlib qt5')
# Wed, 07 Jun 2017 05:36:28
get_ipython().magic('load qtconsole/2017/06/setups/setup_20170606.py')
# Wed, 07 Jun 2017 05:36:29
# %load qtconsole/2017/06/setups/setup_20170606.py
### Setup script, modified from gmf57
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

# Wed, 07 Jun 2017 05:36:43
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-06_spectra_at_points\2017-06-06\2017-06-06_214043_Planefit.json", instruments=instruments)
# Wed, 07 Jun 2017 05:36:50
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Wed, 07 Jun 2017 05:37:03
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.linspace(50,170,3);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.5, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        plt.close('all');

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax.imshow(vs, cmap='viridis', origin='upper')
        cbar = plt.colorbar(image)
        ax.set_xlabel('x');
        ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);


