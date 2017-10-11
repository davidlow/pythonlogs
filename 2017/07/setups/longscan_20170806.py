scans = []
tds = []
for i in range(15):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"))
    print("take image")
    instruments['lockin_cap'].amplutide=3.0
    scan = Scanplane(instruments, plane, numpts=[1600, 200], scanheight=20, scan_rate=100, span=[800,200], center=[0,-300])
    scan.run()
    scans.append(scan)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"))
    print("touchdown series")
    for i in range(10):
        td = Touchdown(instruments, planescan=True)
        td.run()
        tds.append(td)
    plt.close("all")
