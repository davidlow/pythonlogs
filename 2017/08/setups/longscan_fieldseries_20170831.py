s_fluxes = [44, 60, 66, 68, 71, 86,
            27, 33, 41, 72, 85]
s_fluxes = [66, 82, 91, 94, 98, 42,
            62, 70, 78, 30, 41]
currents = [-1e-3,-.8e-3,-.5e-3,-.4e-3,-.3e-3,0,
            .3e-3,.4e-3,.5e-3,.8e-3,1e-3]
scans    = []

plt.close('all')

for i in range(len(currents)):
    k.Iout = currents[i]
    s.reset()
    s.S_flux = s_fluxes[i]
    s.reset()
    scans.append(Scanplane(instruments,plane,span=[800,800], center=[0,0], 
                        numpts=[2000,300],scan_rate=20, scanheight=30))
    scans[-1].run()
