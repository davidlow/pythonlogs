specs = []
scans = []
currents = [-200e-6, 0, 200e-6, -500e-6, -600e-6, -700e-6, 500e-6, 600e-6, 700e-6]
mods = np.array(currents) * 1e6 * (35/600)
for current, mod in zip(currents, mods):
    print(current, datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"))
    instruments['lockin_cap'].amplitude=0.0
    instruments['lockin_squid'].amplitude=0.0
    Is = np.linspace(k.I, current, 20)
    for I in Is:
        k.Iout = I
        time.sleep(0.2)
    s.S_flux = mod
    s.reset()
    pa.filter = (1, 100000)
    spec = SQUIDSpectrum(instruments, averages=10, measure_time=2)
    spec.run()
    specs.append(spec)
    instruments['lockin_cap'].amplutide=3.0
    pa.filter = (1, 100)
    instruments['lockin_squid'].amplitude=3.0
    scan = Scanplane(instruments, plane, numpts=[1200, 100], scanheight=15, scan_rate=20, center=[50,-300], span=[600,150])
    scan.run()
    scans.append(scan)
    plt.close("all")
