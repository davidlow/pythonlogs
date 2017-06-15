# longscan_vibrationtest.py
# author: david low
# 
# takes a scan to look for vibrations


# Session parameters for this script
ONF = {'x': 216, 'y': 0}; # on the feature
OFF = {'x': 116, 'y': 0}; # off the feature
FED = {'x': 190, 'y': 0}; # on the falling edge of the feature
RED = {'x': 242, 'y': 0}; # on the rising edge of the feature
HEIGHTS = [200,100,50,30,20,15,10,5,0,-5,-10]
MEASURE_TIME = 10
SCANRATE = 10;

REDUCE_GAIN_AT = 15
ORIGINAL_GAIN = 25
REDUCED_GAIN = 10

GAIN = ORIGINAL_GAIN


# for testing, quick and dirty
#HEIGHTS = [200,50,15,5]
#MEASURE_TIME = 1
#SCANRATE = 100;

TOTAL_LINES=3;
LINE = 1;

class VibrationTest(Measurement):
    def __init__(self, scanplane, 
                spectrum_onf, 
                spectrum_off, 
                spectrum_fed, 
                spectrum_red):
        super().__init__();
        sp = scanplane;
        ventries = ['acx', 'acy', 'dc' ,'cap'];

        self.fig, self.ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
        self.ax = list(self.ax.flatten())

        for entry in range(len(ventries)):
            self.ax[entry].plot(sp.X[LINE], sp.V[ventries[entry]][LINE]);
            self.ax[entry].set_ylabel([ventries[entry], " V"]);

        self.ax[-1].set_xlabel('V')
        self.ax[0].set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
                sp.timestamp,
                int(sp.Y[LINE][0]),
                int(sp.Z[LINE][0])
                )
        )
        self.fig.tight_layout()

        self.X = sp.X;
        self.Y = sp.Y;
        self.Z = sp.Z;
        self.V = sp.V;
        self.spectrum_off_V = spectrum_off.V;
        self.spectrum_onf_V = spectrum_onf.V;
        self.spectrum_fed_V = spectrum_onf.V;
        self.spectrum_red_V = spectrum_onf.V;
        self.spectrum_off_f = spectrum_off.f;
        self.spectrum_onf_f = spectrum_onf.f;
        self.spectrum_fed_f = spectrum_fed.f;
        self.spectrum_red_f = spectrum_red.f;
        self.spectrum_off_psdave = spectrum_off.psdAve;
        self.spectrum_onf_psdave = spectrum_onf.psdAve;
        self.spectrum_fed_psdave = spectrum_fed.psdAve;
        self.spectrum_red_psdave = spectrum_red.psdAve;


    def do(self):
        return;

    def setup_plots(self):
        return;

    def plot(self):
        return;


for height in HEIGHTS:
    #instruments['squidarray'].reset()

    if height <= REDUCE_GAIN_AT:
        GAIN=REDUCED_GAIN;

    instruments['preamp'].gain = GAIN;


    print("Now starting height {0:d}".format(height));
    sc = Scanplane(instruments,pf,
            span=[200,1], 
            center=[216,0], 
            numpts=[2000,3],
            scan_rate=SCANRATE, 
            scanheight=height
    );
    sc.notes = "[dhl88]  Quick Line scan"
    sc.run()
    plt.close('all')
    pz.sweep(pz.V, {'x':OFF['x'], 'y':OFF['y'], 'z':sc.Z[LINE][0]});
    spectrum_off = AnnotatedSpectrum(CAP_I, instruments=instruments,
        notes="Off the feature",
        measure_time=MEASURE_TIME,
        preamp_gain_override=False,
        preamp_gain=ORIGINAL_GAIN,
        preamp_filter_override=False,
        preamp_filter=(0,10e3),
        preamp_dccouple_override=True,
        preamp_autoOL=True
    );
    spectrum_off.run()
    plt.close('all')
    pz.sweep(pz.V, {'x':ONF['x'], 'y':ONF['y'], 'z':sc.Z[LINE][0]});
    spectrum_onf = AnnotatedSpectrum(CAP_I, instruments=instruments,
        notes="Directly on the feature",
        measure_time=MEASURE_TIME,
        preamp_gain_override=False,
        preamp_gain=ORIGINAL_GAIN,
        preamp_filter_override=False,
        preamp_filter=(0,10e3),
        preamp_dccouple_override=True,
        preamp_autoOL=True
    );
    spectrum_onf.run()
    plt.close('all')

    plt.close('all')
    pz.sweep(pz.V, {'x':FED['x'], 'y':FED['y'], 'z':sc.Z[LINE][0]});
    spectrum_fed = AnnotatedSpectrum(CAP_I, instruments=instruments,
        notes="On the falling edge of the feature",
        measure_time=MEASURE_TIME,
        preamp_gain_override=False,
        preamp_gain=ORIGINAL_GAIN,
        preamp_filter_override=False,
        preamp_filter=(0,10e3),
        preamp_dccouple_override=True,
        preamp_autoOL=True
    );
    spectrum_fed.run()
    plt.close('all')

    plt.close('all')
    pz.sweep(pz.V, {'x':RED['x'], 'y':RED['y'], 'z':sc.Z[LINE][0]});
    spectrum_red = AnnotatedSpectrum(CAP_I, instruments=instruments,
        notes="On the rising edge of the feature",
        measure_time=MEASURE_TIME,
        preamp_gain_override=False,
        preamp_gain=ORIGINAL_GAIN,
        preamp_filter_override=False,
        preamp_filter=(0,10e3),
        preamp_dccouple_override=True,
        preamp_autoOL=True
    );
    spectrum_red.run()
    plt.close('all')

    vib = VibrationTest(sc, 
        spectrum_onf, 
        spectrum_off, 
        spectrum_fed, 
        spectrum_red);
    vib.run()

