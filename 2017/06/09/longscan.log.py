# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Sat, 10 Jun 2017 00:33:02
get_ipython().magic('load qtconsole/2017/06/setups/main_20170608.py')
# Sat, 10 Jun 2017 00:33:03
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Sat, 10 Jun 2017 00:33:41
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
# pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Sat, 10 Jun 2017 00:33:52
pf = Planefit.load()
# Sat, 10 Jun 2017 00:34:38
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-08_mattplane_and_scan\2017-06-09\2017-06-09_222930_Planefit.json", instruments=instruments)
# Sat, 10 Jun 2017 00:34:51
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Sat, 10 Jun 2017 00:35:10
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  first cold scan! Quick scan to make sure we're at the right place
'''
sc.run()

# Sat, 10 Jun 2017 00:59:01
s.reset()
# Sat, 10 Jun 2017 00:59:04
s.tune()
# Sat, 10 Jun 2017 00:59:27
s = SquidArray(visaResource='COM1')
# Sat, 10 Jun 2017 00:59:31
s.tune()
# Sat, 10 Jun 2017 00:59:54
s.tune()
# Sat, 10 Jun 2017 01:01:40
s.sensitivity = 'Med'
# Sat, 10 Jun 2017 01:01:46
s.reset()
# Sat, 10 Jun 2017 01:02:32
instruments['squidarray'] = s
# Sat, 10 Jun 2017 01:02:56
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  fixed squid array?
'''
sc.run()

# Sat, 10 Jun 2017 01:13:15
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  fixed squid array. strange looking plot, redoing to make sure
'''
sc.run()

# Sat, 10 Jun 2017 01:31:56
get_ipython().magic('load qtconsole/2017/06/setups/longscan_20170609.py')
# Sat, 10 Jun 2017 01:32:56
# %load qtconsole/2017/06/setups/longscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,900],scan_rate=20, scanheight=15)
sc.notes = '''
[dhl88]  Long scan.  50 mK

To compare with previous long scan
'''
sc.run()

# [dhl88] Actually took 12.9 hr

# Sat, 10 Jun 2017 21:53:53
# %load qtconsole/2017/06/setups/longscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,900],scan_rate=20, scanheight=30)
sc.notes = '''
[dhl88]  Long scan.  50 mK

I can see features in the last long scan in the capacitance.  scanning
much higher.  Hopefully that fixes the color issues on he DC flux
parts but I doubt it... 
'''
sc.run()

# [dhl88] Actually took 12.9 hr

# Mon, 12 Jun 2017 00:05:39
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 00:09:15
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 00:09:18
# %load qtconsole/2017/06/setups/longscan_daqspectrum_original.py
# daqspectrum height series across a feature

zs = np.array([50,100,180,200]);
xs = np.linspace(150,250,20);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

from Nowack_Lab.Utilities.utilities import AttrDict
from mpl_toolkits.axes_grid1 import make_axes_locatable

class Longscan_daqspectrumheight(Measurement):
    def __init__(self, instruments):
        super().__init__(instruments=instruments);
    def do(self, xs=[], zs=[], vs=[], cs=[]):
        self.xs = xs;
        self.zs = zs;
        self.vs = vs;
        self.cs = cs;
        self.plot();
        return;
    def plot(self):
        super().plot();
        image = self.ax['ave'].imshow(vs, cmap='viridis', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        d = make_axes_locatable(self.ax['ave'])
        cax = d.append_axes("right", size=0.1, pad=0.1)
        cbar = plt.colorbar(image, cax=cax)
        cbar.set_label('average value', rotation=270, labelpad=12)
        cbar.formatter.set_powerlimits((-2,2))

        image = self.ax['cap'].imshow(cs, cmap='inferno', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        d = make_axes_locatable(self.ax['cap'])
        cax = d.append_axes("right", size=0.1, pad=0.1)
        cbar = plt.colorbar(image, cax=cax)
        cbar.set_label('capacitance', rotation=270, labelpad=12)
        cbar.formatter.set_powerlimits((-8,6))

        self.ax['ave'].set_xlabel('x');
        self.ax['ave'].set_ylabel('z');
        self.ax['cap'].set_xlabel('x');
        self.ax['cap'].set_ylabel('z');
    def setup_plots(self):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = AttrDict()
        self.ax['ave'] = self.fig.add_subplot(121)
        self.ax['cap'] = self.fig.add_subplot(122)
        title = ax['ave'].set_title(self.timestamp, size="medium", y=1.02)
        title = ax['cap'].set_title(self.timestamp, size="medium", y=1.02)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Mon, 12 Jun 2017 00:10:29
spectrum = DaqSpectrum(instruments, measure_time=10), annotate_notes=True)
# Mon, 12 Jun 2017 00:10:37
spectrum = DaqSpectrum(instruments, measure_time=10, annotate_notes=True)
# Mon, 12 Jun 2017 00:10:56
pz.z.V
#[Out]# 49.9943164464139
# Mon, 12 Jun 2017 00:11:13
spectrum.notes('daq spectrum')
