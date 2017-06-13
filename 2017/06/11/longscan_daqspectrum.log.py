# IPython log file

# Mon, 12 Jun 2017 02:26:39
get_ipython().magic('load qtconsole/2017/06/setups/main_20170608.py')
# Mon, 12 Jun 2017 02:26:44
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
#pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Mon, 12 Jun 2017 02:26:56
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe5be748>
# Mon, 12 Jun 2017 02:26:59
s.reset()
# Mon, 12 Jun 2017 02:27:10
s = SquidArray(visaResource='COM1')
# Mon, 12 Jun 2017 02:27:11
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe5d1da0>
# Mon, 12 Jun 2017 02:27:14
s.reset()
# Mon, 12 Jun 2017 02:27:19
s.sensitivity = 'Med'
# Mon, 12 Jun 2017 02:27:26
s.A_bias = 43
# Mon, 12 Jun 2017 02:27:36
s.S_bias = 430
# Mon, 12 Jun 2017 02:27:39
s.reset()
# Mon, 12 Jun 2017 02:27:49
s.offset = .08
# Mon, 12 Jun 2017 02:27:53
s.tune()
# Mon, 12 Jun 2017 02:28:57
get_ipython().magic('run qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 02:29:04
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 02:41:27
s.reset()
# Mon, 12 Jun 2017 02:41:34
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 02:53:51
s.reset()
# Mon, 12 Jun 2017 02:53:54
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 03:02:16
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum_original.py')
# Mon, 12 Jun 2017 03:02:36
# %load qtconsole/2017/06/setups/longscan_daqspectrum_original.py
# daqspectrum height series across a feature

#zs = np.array([50,100,180,200]);
#xs = np.linspace(150,250,20);
zs = np.array([50,100,170]);
xs = np.linspace(150,325,6);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
        instruments['squidarray'].reset()
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
        title = self.ax['ave'].set_title(self.timestamp, size="medium", y=1.02)
        title = self.ax['cap'].set_title(self.timestamp, size="medium", y=1.02)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);
# Mon, 12 Jun 2017 03:03:22
s.reset()
# Mon, 12 Jun 2017 03:03:33
instruments['preamp']
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xe5a0eb8>
# Mon, 12 Jun 2017 03:03:50
pa = SR5113(port='COM3')
# Mon, 12 Jun 2017 03:04:01
# %load qtconsole/2017/06/setups/longscan_daqspectrum_original.py
# daqspectrum height series across a feature

#zs = np.array([50,100,180,200]);
#xs = np.linspace(150,250,20);
zs = np.array([50,100,170]);
xs = np.linspace(150,325,6);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
        instruments['squidarray'].reset()
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
        title = self.ax['ave'].set_title(self.timestamp, size="medium", y=1.02)
        title = self.ax['cap'].set_title(self.timestamp, size="medium", y=1.02)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Mon, 12 Jun 2017 03:31:01
# %load qtconsole/2017/06/setups/longscan_daqspectrum_original.py
# daqspectrum height series across a feature

#zs = np.array([50,100,180,200]);
xs = np.linspace(150,325,40);
zs = np.array([50,100,170]);
#xs = np.linspace(150,325,6);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.10, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
        instruments['squidarray'].reset()
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
        title = self.ax['ave'].set_title(self.timestamp, size="medium", y=1.02)
        title = self.ax['cap'].set_title(self.timestamp, size="medium", y=1.02)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Mon, 12 Jun 2017 03:31:51
# %load qtconsole/2017/06/setups/longscan_daqspectrum_original.py
# daqspectrum height series across a feature

#zs = np.array([50,100,180,200]);
xs = np.linspace(150,325,40);
zs = np.array([50,100,170]);
#xs = np.linspace(150,325,6);

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
        instruments['squidarray'].reset()
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
        title = self.ax['ave'].set_title(self.timestamp, size="medium", y=1.02)
        title = self.ax['cap'].set_title(self.timestamp, size="medium", y=1.02)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);
# Mon, 12 Jun 2017 16:39:48
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Mon, 12 Jun 2017 16:39:54
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  Quick scan for testing scanning
'''
sc.run()

# Mon, 12 Jun 2017 16:40:52
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-08_mattplane_and_scan\2017-06-09\2017-06-09_011238_Planefit.json", instruments=instruments)
# Mon, 12 Jun 2017 16:41:17
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Mon, 12 Jun 2017 16:41:19
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  Quick scan for testing scanning
'''
sc.run()

