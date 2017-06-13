# daqspectrum height series across a feature

#zs = np.array([50,100,180,200]);
#xs = np.linspace(150,250,20);
zs = np.array([50,100,180,200]);
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