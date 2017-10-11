desiredTs = [.2,.4,.5,.6,.65,.7,.75,.8,.85,.9,.95,1]
Ts = []
offsetscans = []
scans = []
NUMLINESY = 100
SCANRATE = 50


for desiredT in desiredTs:
    lakeshore.pid_setpoint=desiredT
    starttime = time.time()
    while (abs(lakeshore.T[6] - desiredT) > .01 and 
           time.time() - starttime        < 30*60
          ):
        print('T={0:2.3f}, pid_setpoint={1:2.3f}'.format(
            lakeshore.T[6], desiredT));
        time.sleep(30)
    T = []
    T.append(lakeshore.T[6])
    offsetscans.append(
                    Scanplane(instruments=instruments, 
                                 plane=plane2, 
                                 span=[800,800], 
                                 center=[0,0], 
                                 numpts=[2000, NUMLINESY], 
                                 scanheight=400, 
                                 scan_rate=SCANRATE)       
                         )
    print('Start offset scan')
    offsetscans[-1].run()
    T.append(lakeshore.T[6])

    scans.append(
                    Scanplane(instruments=instruments, 
                                 plane=plane2, 
                                 span=[800,800], 
                                 center=[0,0], 
                                 numpts=[2000, NUMLINESY], 
                                 scanheight=25, 
                                 scan_rate=SCANRATE)       
                 )
    print('Start scan')
    scans[-1].run()
    T.append(lakeshore.T[6])

lakeshore.pid_setpoint=.01
