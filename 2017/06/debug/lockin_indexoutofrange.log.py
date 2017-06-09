# IPython log file

get_ipython().magic('load qtconsole/2017/06/debug/lockin_indexoutofrange.script.py')
# Thu, 08 Jun 2017 01:15:52
instruments.keys()
#[Out]# dict_keys(['squidarray', 'montana', 'lockin_cap', 'preamp', 'atto', 'lockin_squid', 'daq', 'piezos'])
# Thu, 08 Jun 2017 01:16:13
instruments['lockin_cap']
#[Out]# <Nowack_Lab.Instruments.lockin.SR830 at 0xc6375c0>
# Thu, 08 Jun 2017 01:16:19
instruments['lockin_cap'].V
# Thu, 08 Jun 2017 01:16:22
instruments['lockin_cap'].R
#[Out]# 9.68583e-07
# Thu, 08 Jun 2017 01:25:44
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 01:25:50
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,170]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

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
        image = self.ax_ave.imshow(vs, cmap='viridis', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax_ave.set_xlabel('x');
        self.ax_ave.set_ylabel('z');
        self.ax_cap.set_xlabel('x');
        self.ax_cap.set_ylabel('z');
    def setup_plots(self):
        self.fig_ave, self.ax_ave = plt.subplots();
        self.fig_cap, self.ax_cap = plt.subplots();


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

# Thu, 08 Jun 2017 01:31:28
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 01:31:30
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,170]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

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
        cbar = plt.colorbar(image)
        image = self.ax['cap'].imshow(cs, cmap='viridis', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax['ave'].set_xlabel('x');
        self.ax['ave'].set_ylabel('z');
        self.ax['cap'].set_xlabel('x');
        self.ax['cap'].set_ylabel('z');
    def setup_plots(self):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = AttrDict()
        self.ax['ave'] = self.fig.add_subplot(121)
        self.ax['cap'] = self.fig.add_subplot(122)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Thu, 08 Jun 2017 01:49:52
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 01:49:57
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,170]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

from Nowack_Lab.Utilities.utilities import AttrDict

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
        cbar = plt.colorbar(image)
        image = self.ax['cap'].imshow(cs, cmap='viridis', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax['ave'].set_xlabel('x');
        self.ax['ave'].set_ylabel('z');
        self.ax['cap'].set_xlabel('x');
        self.ax['cap'].set_ylabel('z');
    def setup_plots(self):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = AttrDict()
        self.ax['ave'] = self.fig.add_subplot(121)
        self.ax['cap'] = self.fig.add_subplot(122)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Thu, 08 Jun 2017 02:01:31
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 02:01:34
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,170]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

from Nowack_Lab.Utilities.utilities import AttrDict

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
        cbar = plt.colorbar(image)
        image = self.ax['cap'].imshow(cs, cmap='inferno', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax['ave'].set_xlabel('x');
        self.ax['ave'].set_ylabel('z');
        self.ax['cap'].set_xlabel('x');
        self.ax['cap'].set_ylabel('z');
    def setup_plots(self):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = AttrDict()
        self.ax['ave'] = self.fig.add_subplot(121)
        self.ax['cap'] = self.fig.add_subplot(122)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Thu, 08 Jun 2017 02:09:23
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 02:09:28
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,180,200]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
        cs[z][x] = instruments['lockin_cap'].R;
        plt.close('all');
    pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[0]});

from Nowack_Lab.Utilities.utilities import AttrDict

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
        cbar = plt.colorbar(image)
        image = self.ax['cap'].imshow(cs, cmap='inferno', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax['ave'].set_xlabel('x');
        self.ax['ave'].set_ylabel('z');
        self.ax['cap'].set_xlabel('x');
        self.ax['cap'].set_ylabel('z');
    def setup_plots(self):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = AttrDict()
        self.ax['ave'] = self.fig.add_subplot(121)
        self.ax['cap'] = self.fig.add_subplot(122)


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Thu, 08 Jun 2017 02:17:12
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 02:17:14
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,180,200]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
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
        cbar.set_label(clabel, rotation=270, labelpad=12)
        cbar.formatter.set_powerlimits((-2,2))

        image = self.ax['cap'].imshow(cs, cmap='inferno', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        d = make_axes_locatable(self.ax['cap'])
        cax = d.append_axes("right", size=0.1, pad=0.1)
        cbar = plt.colorbar(image, cax=cax)
        cbar.set_label(clabel, rotation=270, labelpad=12)
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


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

# Thu, 08 Jun 2017 02:21:21
get_ipython().magic('load qtconsole/2017/06/setups/longscan_daqspectrum.py')
# Thu, 08 Jun 2017 02:21:31
# %load qtconsole/2017/06/setups/longscan_daqspectrum.py
# daqspectrum height series across a feature

zs = np.array([50,100,180,200]);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);
cs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
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


ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs,cs=cs);

