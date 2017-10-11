AMPS = np.linspace(0,3,61)
#TEMPS = np.linspace(1.3,1.2,2)

ARGS = [instruments, plane2]
#KWARGS = [ {'x':-77, 'y':-14, 'z0':-10,'scan_rate':2}, 
#           {'x':-350,'y':-100,'z0':-10,'scan_rate':2} ]
KWARGS = [ 
           {'x':-100, 'y':-50, 'z0':25,'scan_rate':10}, 
           #{'x':+145, 'y':-185,'z0':25,'scan_rate':2}, 
           {'x':-375, 'y':-100,'z0':25,'scan_rate':10},
           #{'x':-120, 'y':-315,'z0':25,'scan_rate':2} 
         ]
KWARGS_r = {'zstart':-400}
#INST = lakeshore
INST = liS
#PARAM = 'pid_setpoint'
PARAM = 'amplitude'


def wait_until_t_stable(a, liS):
    liS.amplitude = a
    print('Lockin amplitude = {0}'.format(liS.amplitude))

def log(measurement, liS):
    measurement.notes = 'lockin amplitude series, amplitude={0}'.format(
            liS.amplitude)
    return 'amplitude={0}'.format(liS.amplitude)

amplitudes=[]
for A in AMPS:
    amplitudes.append(A)
    amplitudes.append(A)

constructors = [Heightsweep for t in amplitudes]
c_args = [ ARGS for t in amplitudes]
c_kwargs=[ KWARGS[i%2]   for i in range(len(amplitudes))]
r_args  =[ [] for i in range(len(amplitudes))]
r_kwargs=[ KWARGS_r for i in range(len(amplitudes))]
instrument_to_varry = [INST for t in amplitudes]
instrument_parameter = [PARAM for t in amplitudes]
waitfncts = [wait_until_t_stable for t in amplitudes]
wait_fncts_args = [[a, liS] for a in amplitudes]
log_fncts = [log for t in amplitudes]
log_fncts_args = [[liS] for t in amplitudes]


nm = NestedMeasurement(
        constructors,
        c_args,
        c_kwargs,
        r_args,
        r_kwargs,
        instrument_to_varry,
        instrument_parameter,
        amplitudes,
        waitfncts,
        wait_fncts_args,
        log_fncts,
        log_fncts_args
        )

#nm.run()
