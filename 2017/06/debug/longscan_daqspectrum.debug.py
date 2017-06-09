# daqspectrum height series across a feature


zs = np.linspace(50,170,3);
xs = np.linspace(150,250,3);

vs = np.outer(zs,xs);


for x in range(len(xs)):
    for z in range(len(zs)):
        pz.sweep(pz.V, {'x':xs[x], 'y':0, 'z':zs[z]});
        spectrum = spectrum = DaqSpectrum(instruments, measure_time=.1, 
                                          annotate_notes=True);
        spectrum.notes = "[dhl88] In contact, moving\nx={0:d}, z={1:d}".format(
                    int(pz.x.V), int(pz.z.V));
        spectrum.run()
        vs[z][x] = np.mean(spectrum.V)
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
        image = self.ax.imshow(vs, cmap='viridis', origin='upper',
                                extent = [self.xs.min(), self.xs.max(),
                                          self.zs.max(), self.zs.min()]
        );
        cbar = plt.colorbar(image)
        self.ax.set_xlabel('x');
        self.ax.set_ylabel('z');

ls_dsh = Longscan_daqspectrumheight(instruments=instruments);
ls_dsh.run(xs=xs,zs=zs,vs=vs);

