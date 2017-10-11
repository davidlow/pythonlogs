TEMPS = np.linspace(1.3,.6,71)
#TEMPS = np.linspace(1.3,1.2,2)

ARGS = [instruments, plane2]
KWARGS = [ {'x':-77, 'y':-14, 'z0':-10,'scan_rate':2}, 
           {'x':-350,'y':-100,'z0':-10,'scan_rate':2} ]
KWARGS_r = {'zstart':-400}
INST = lakeshore
PARAM = 'pid_setpoint'


def wait_until_t_stable(t, lakeshore, s):
    starttime = time.time()
    print("Waiting until T={0}".format(t))
    while (starttime + 1800 > time.time()):
        if(abs(lakeshore.T[6] - t) < .01):
            print("T={0}".format(lakeshore.T[6]))
            break;
        time.sleep(10)
    print("Tuning SFlux")
    s.autotune_sflux(instruments['daq'], 'dc', P=10, exittime=120)

def log(measurement, lakeshore):
    measurement.notes = 'Temperature series, T={0}'.format(lakeshore.T[6])
    return 'T={0}'.format(lakeshore.T[6])

temperatures=[]
for T in TEMPS:
    temperatures.append(T)
    temperatures.append(T)

constructors = [Heightsweep for t in temperatures]
c_args = [ ARGS for t in temperatures]
c_kwargs=[ KWARGS[i%2]   for i in range(len(temperatures))]
r_args  =[ [] for i in range(len(temperatures))]
r_kwargs=[ KWARGS_r for i in range(len(temperatures))]
instrument_to_varry = [INST for t in temperatures]
instrument_parameter = [PARAM for t in temperatures]
waitfncts = [wait_until_t_stable for t in temperatures]
wait_fncts_args = [[t, lakeshore, s] for t in temperatures]
log_fncts = [log for t in temperatures]
log_fncts_args = [[lakeshore] for t in temperatures]


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
        log_fncts_args
        )

#nm.run()
