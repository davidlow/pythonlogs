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

    def __init__(self, instruments
                zs = np.array([50,100,180,200]),
                ys = np.array([0]),
                xs = np.linspace(150,250,20),
                measure_time = 10):
    '''
    Arguments:
    instruments
        'piezos':   Piezos object
    xs              x piezo voltages, numpy array
    ys              y piezo voltages, numpy array  
    zs              z piezo voltages, numpy array
    measure_time    measurement time for DaqSpectrum
    '''
        super().__init__(instruments=instruments);
        self.xs = xs;
        self.ys = ys;
        self.zs = zs;
        self.spectrastructs = [];
        self.measure_time = measure_time;
    def do(self):
        pz = instruments['piezos'];
        for x in range(len(xs)):
            for y in range(len(yz)):
                for z in range(len(zs)):
                    pz.sweep(pz.V, {'x':xs[x], 'y':ys[y], 'z':zs[z]});
                    spectrum = spectrum = DaqSpectrum(instruments, 
                                          measure_time=self.measure_time, 
                                          annotate_notes=True
                                      );
                    spectrum.notes = "[x,y,z] = [{0:d},{1:d},{2:d}]".format(
                        int(pz.x.V), int(pz.y.V), int(pz.z.V));
                    spectrum.run()
                    vs[z][x] = np.mean(spectrum.V)
                    cs[z][x] = instruments['lockin_cap'].R;
                    plt.close('all');
                    spectrastructs.append(
                        {'loc':         np.array([pz.x.V, pz.y.V, pz.z.V]),
                         'spectrum_f':  spectrum.f,
                         'spectrum_V':  spectrum.V,
                         'spectrum_psdave': spectrum.psdAve,
                         'spectrum_name': 'filename', #FIXME
                         'spectrum_mean': np.mean(spectrum.V),
                        }
                    )# will this even save correctly????
                pz.sweep(pz.V, {'x':xs[x], 'y':ys[y], 'z':-pz.z.Vmax});
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