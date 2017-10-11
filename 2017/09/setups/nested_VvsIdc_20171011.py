# template that initializes a nestedmeasurement

# Global variables that the user is supposed to change at run time
#TEMPSup = np.linspace(.2,1.2,101)
#TEMPSdown = np.linspace(1.2,.2,101)
#TEMPSdown = [] #np.linspace(1.2,.8,21)
#TEMPSup = list(np.linspace(.3,1,25)) + [1.03,1.04,1.05,1.06]
#TEMPSup = [.3,.305]
#DWELLTIME = 5 

# Misc imports that I got tired of remembering to import before loading
import time
import types
import random

# Args and KWargs for constructing the measurements
ARGS = []
#KWARGS = {
#        'instruments': instruments,
#        'plane'      : plane,
#        'span'       : [800,800],
#        'center'     : [0,0],
#        'numpts'     : [2000,60],
#        'scanheight' : 10, 
#        'scan_rate'  : 25 
#        }
#KWARGS = {
#        'instruments': instruments,
#        'plane'      : plane,
#        'span'       : [800,800],
#        'center'     : [0,0],
#        'numpts'     : [2000,3],
#        'scanheight' : 15, 
#        'scan_rate'  : 100
#        }
KWARGS = {'daqchannel': daq.ai6,
          'instruments': instruments,
          'iouts': np.linspace(-1e-3,1e-3,11),
          'dwelltime': .1
         }
#KWARGS = [ {'x':-77, 'y':-14, 'z0':-10,'scan_rate':2}, 
#           {'x':-350,'y':-100,'z0':-10,'scan_rate':2},
#           {'x': 145,'y':-185,'z0': 25,'scan_rate':2},
#           {'x':-120,'y':-315,'z0': 25,'scan_rate':2},
#           ]
KWARGS_r = {'slowsweeppts':15, 
            'slowsweeprate':1000e-6}



# Instrument to control and param to varry
fakeinst = {'fakeparam':0}
INST = fakeinst
PARAM = 'fakeparam'


# How long to wait before making/running measurement?
def wait_until_t(obj, targetT, lakeshore, spread=.001, numsamples=20,
                 maxwaitbtwpts = 2):
    starttime = time.time()
    print("Waiting until T={0}".format(targetT))
    while (starttime + 1200 > time.time()):
        ts = []
        for i in range(numsamples):
            ts.append(lakeshore.T[6])
            time.sleep(maxwaitbtwpts*random.random())
        ts = np.array(ts)
        print('[Tmean, Tstd, Tmin, Tmax] = ' +
              '[{0:3.5f},{3:5.3f},{1:3.5f},{2:3.5f}]'.format(
            np.mean(ts), ts.min(), ts.max(), np.std(ts)))

        # If (target is within min/max and min/max close together) or
        #    (target is close to the mean value)
        if ( (targetT > ts.min() and targetT < ts.max()
                and abs(ts.min() - ts.max()) < 2*spread ) or 
             (abs(targetT  - np.mean(ts)) < spread)        ):
            print("T={0:3.3f}, time_elapsed={1:3.3f}".format(
                lakeshore.T[6],
                time.time() - starttime
                ))
            obj.tinfo = {'Ts':ts,
                         'waittime':time.time()-starttime
                         }
            break
        time.sleep(10)

def wait_time(obj):
    time.sleep(5)

# What should you do to log?
def log(obj):
    #measurement.T = lakeshore.T[6]
    #measurement.B = magnet.B
    return ''

# Create list of values to vary the instrument param over
temperatures=range(1000)
#for T in TEMPSup:
#    temperatures.append(T)
#for T in TEMPSdown:
#    temperatures.append(T)

# function to run before doing any of the measurements.  Run before
# the for loop that loops over the values of the instrument param
def before(obj, *args):
    obj.Bs = []
    obj.Ts = []
    obj.Rs = []

# Function that runs before running the measurement
def prerun(obj, lakeshore, magnet):
    b = magnet.B
    t = lakeshore.T[6]
    obj.measurements[-1].T = t
    obj.measurements[-1].B = b
    obj.Bs.append(b)
    obj.Ts.append(t)
    #piezoz.V = -400
    #offset = {}
    #offset['dc']  = daq_dc.V
    #offset['acx'] = daq_acx.V
    #offset['acy'] = daq_acy.V
    #offset['z']   = piezoz.V
    #obj.measurements[-1].offset = offset
    pass

# Function that runs after running the measurement
def postrun(obj, *args):
    obj.Rs.append(obj.measurements[-1].R)
    print('[T,R,B] = [{0:2.4f},{1:2.4f},{2:2.2e}]'.format(
        obj.Ts[-1], obj.Rs[-1], obj.Bs[-1]))
    pass

# all the parameters for nestedmeasurement
constructors         = [ VvsIdc for t in temperatures]
c_args               = [ ARGS for t in temperatures]
c_kwargs             = [ KWARGS for i in range(len(temperatures))]
r_args               = [ [] for i in range(len(temperatures))]
r_kwargs             = [ KWARGS_r for i in range(len(temperatures))]
instrument_to_varry  = [ INST for t in temperatures]
instrument_parameter = [ PARAM for t in temperatures]
waitfncts            = [ wait_time for t in temperatures]
wait_fncts_args      = [ [] for t in temperatures]
log_fncts            = [log for t in temperatures]
log_fncts_args       = [ [] for t in temperatures]
before_fnct_args     = [ [] ]
pre_run              = [prerun for t in temperatures]
pre_run_args         = [ [lakeshore, m] 
                         for t in temperatures]
post_run_args        = [ [] for t in temperatures]
post_run             = [postrun for t in temperatures]
post_run_args        = [ [] for t in temperatures]


nm = NestedMeasurement(
        constructors,
        c_args,
        c_kwargs,
        r_args,
        r_kwargs,
        instrument_to_varry,
        instrument_parameter,
        temperatures,
        before,
        before_fnct_args,
        waitfncts,
        wait_fncts_args,
        log_fncts,
        log_fncts_args,
        pre_run,
        pre_run_args,
        post_run,
        post_run_args
        )

#nm.run()

