# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Wed, 14 Jun 2017 21:56:45
get_ipython().magic('load qtconsole/2017/06/setups/main_20170613.py')
# Wed, 14 Jun 2017 21:56:48
# %load qtconsole/2017/06/setups/main_20170613.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170613.py')

# Wed, 14 Jun 2017 21:57:09
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="testing code", measure_time=.1, preamp_gain_override=False, preamp_gain=250, preamp_dccouple_override=False, preamp_dccouple=True)
# Wed, 14 Jun 2017 21:57:14
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 21:57:21
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="testing code", measure_time=.1, preamp_gain_override=False, preamp_gain=250, preamp_dccouple_override=False, preamp_dccouple=True)
# Wed, 14 Jun 2017 21:57:34
CAP_I = instruments['lockin_cap'].R
# Wed, 14 Jun 2017 21:57:36
CAP_I
#[Out]# 1.07196e-06
# Wed, 14 Jun 2017 21:57:41
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="testing code", measure_time=.1, preamp_gain_override=False, preamp_gain=250, preamp_dccouple_override=False, preamp_dccouple=True)
# Wed, 14 Jun 2017 21:57:57
a.run()
# Wed, 14 Jun 2017 22:03:42
from importlib import reload
# Wed, 14 Jun 2017 22:03:45
reload(Nowack_Lab.Procedures.daqspectrum)
#[Out]# <module 'Nowack_Lab.Procedures.daqspectrum' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqspectrum.py'>
# Wed, 14 Jun 2017 22:03:49
from Nowack_Lab.Procedures.daqspectrum import AnnotatedSpectrum
# Wed, 14 Jun 2017 22:03:53
a = AnnotatedSpectrum(CAP_I, instruments=instruments, notes="testing code", measure_time=.1, preamp_gain_override=False, preamp_gain=250, preamp_dccouple_override=False, preamp_dccouple=True)
# Wed, 14 Jun 2017 22:04:14
a.run()
# Wed, 14 Jun 2017 22:29:40
get_ipython().magic('load qtconsole/2017/06/setups/longscan_vibrationtest.py')
# Wed, 14 Jun 2017 22:29:47
# %load qtconsole/2017/06/setups/longscan_vibrationtest.py
# longscan_vibrationtest.py
# author: david low
# 
# takes a scan to look for vibrations


# Session parameters for this script
ONF = {'x': 216, 'y': 0}; # on the feature
OFF = {'x': 116, 'y': 0}; # off the feature
FED = {'x': 190, 'y': 0}; # on the falling edge of the feature
RED = {'x': 242, 'y': 0}; # on the rising edge of the feature
#HEIGHTS = [200,100,50,30,20,15,10,5,0,-5,-10]
#MEASURE_TIME = 10
#SCANRATE = 10;

REDUCE_GAIN_AT = 15
ORIGINAL_GAIN = 25
REDUCED_GAIN = 10

GAIN = ORIGINAL_GAIN


# for testing, quick and dirty
HEIGHTS = [200,50,15,5]
MEASURE_TIME = 1
SCANRATE = 100;

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

    instuments['preamp'].gain = GAIN;


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


