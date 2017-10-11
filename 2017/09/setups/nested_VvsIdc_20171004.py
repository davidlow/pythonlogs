TEMPSup = np.linspace(.2,1.2,101)
TEMPSdown = np.linspace(1.2,.2,101)
#TEMPSup = [.180]
#TEMPSdown = [.185]
ISRCs = np.linspace(-1e-3,1e-3, 21)
DWELLTIME = 5 

import time

ARGS = [daq.ai6, instruments, ISRCs, DWELLTIME]
#KWARGS = [ {'x':-77, 'y':-14, 'z0':-10,'scan_rate':2}, 
#           {'x':-350,'y':-100,'z0':-10,'scan_rate':2},
#           {'x': 145,'y':-185,'z0': 25,'scan_rate':2},
#           {'x':-120,'y':-315,'z0': 25,'scan_rate':2},
#           ]
#KWARGS_r = {'zstart':-400}
INST = lakeshore
PARAM = 'pid_setpoint'


def wait_until_t_stable(t, lakeshore, s):
    starttime = time.time()
    print("Waiting until T={0}".format(t))
    while (starttime + 1800 > time.time()):
        if(abs(lakeshore.T[6] - t) < .01):
            print("T={0}, timeelapsed={1}".format(
                lakeshore.T[6],
                time.time() - starttime
                ))
            break;
        time.sleep(10)
#    print("Tuning SFlux")
#    s.autotune_sflux(instruments['daq'], 'dc', P=10, exittime=120)

def log(measurement, lakeshore):
    measurement.notes = 'Temperature series, T={0}'.format(lakeshore.T[6])
    measurement.T = lakeshore.T[6]
    return 'T={0}'.format(lakeshore.T[6])



temperatures=[]
for T in TEMPSup:
    temperatures.append(T)

for T in TEMPSdown:
    temperatures.append(T)

def before(obj, a):
    obj.Ts = np.zeros(len(temperatures))
    obj.Rs = np.zeros(len(temperatures))

def postrun(obj, lakeshore):
    obj.Ts[len(obj.measurements)-1] = lakeshore.T[6]
    obj.Rs[len(obj.measurements)-1] = obj.measurements[-1].R

constructors = [VvsIdc for t in temperatures]
c_args = [ ARGS for t in temperatures]
c_kwargs=[ {}   for i in range(len(temperatures))]
r_args  =[ [] for i in range(len(temperatures))]
r_kwargs=[ {} for i in range(len(temperatures))]
instrument_to_varry = [INST for t in temperatures]
instrument_parameter = [PARAM for t in temperatures]
waitfncts = [wait_until_t_stable for t in temperatures]
wait_fncts_args = [[t, lakeshore, s] for t in temperatures]
log_fncts = [log for t in temperatures]
log_fncts_args = [[lakeshore] for t in temperatures]
before_fnct_args = [0]
post_run = [postrun for t in temperatures]
post_run_args = [ [lakeshore] for t in temperatures]


nm = NestedMeasurement(
        constructors,
        c_args,
        c_kwargs,
        r_args,
        r_kwargs,
        instrument_to_varry,
        instrument_parameter,
        temperatures,
        waitfncts,
        wait_fncts_args,
        log_fncts,
        log_fncts_args,
        before,
        before_fnct_args,
        post_run,
        post_run_args
        )

#nm.run()

