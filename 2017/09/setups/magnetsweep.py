magnetcurrents = [-1e-3, -.5e-3, -.4e-3, -.3e-3, -.1e-3, 0, 
                  .1e-3,  .3e-3, .4e-3, .5e-3, .6e-4, .7e-3]
approxS_flux = [7.6,53.6,60.6,70.8,78.4,88.3,
                91.25, 100, 100, 100,100,100]
NUMLINESY = 100
SCANRATE  = 50

offsetscans = []
scans = []


for current,sflux in zip(magnetcurrents, approxS_flux):
    instruments['keithley'].Iout = current
    instruments['squidarray'].S_flux = sflux
    [istuned, flux] = instruments['squidarray'].autotune_sflux(
                                            instruments['daq'],
                                             'dc', 
                                             P=10, 
                                             exittime=120)
    print("isTuned={0}, S_flux={1:2.2f}".format(
            istuned, flux))
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
