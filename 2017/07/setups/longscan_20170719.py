heights = [22, 20, 18]
center = [77, -135]
pa.filter = (10, 100)
specs = []
scans = []
long_scans=[]
long_scan1 = Scanplane(instruments, plane4, numpts = [200,200], span=[100,100], scan_rate=80, scanheight=22, center=center)
long_scan1.run()
long_scan2 = Scanplane(instruments, plane4, numpts=[200, 200], span=[100, 100], scan_rate=80, scanheight=20, center=center)
long_scan2.run()
long_scans.append(long_scan1)
long_scans.append(long_scan2)
pa.filter = (10, 1000)
for height in heights:
    print(height, datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"))
    print("scan spectrum", height)
    instruments['lockin_cap'].amplitude=0.0
    spec = ss.Scanspectra(instruments, plane4, numpts=[25,25], span=[50,50], center=center, scanheight=height, monitor_time=30, sample_rate=900)
    spec.run()
    specs.append(spec)
    print("take image", height)
    instruments['lockin_cap'].amplutide=3.0
    scan = Scanplane(instruments, plane4, numpts=[200, 100], scanheight=height, scan_rate=100, center=center, span=[100,100])
    scan.run()
    scans.append(scan)
    plt.close("all")

pa.filter = (10, 100)
long_scan3 = Scanplane(instruments, plane4, numpts = [200,200], span=[100,100], scan_rate=100, scanheight=22, center=center)
long_scan3.run()
long_scan4 = Scanplane(instruments, plane4, numpts=[200, 200], span=[100, 100], scan_rate=100, scanheight=20, center=center)
long_scan4.run()
long_scans.append(long_scan3)
long_scans.append(long_scan4)