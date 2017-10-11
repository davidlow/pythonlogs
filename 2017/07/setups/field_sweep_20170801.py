fields_up = np.linspace(0.00002, 0.00006, 11)
fields_down = np.linspace(0.00006, 0.00002, 11)
fields_set = []
fields = []
currents = []
scans = []
for i in range(2):
    for field in fields_up:
        m.ramp_to_field(field, rate=0.001)
        s.reset()
        scan = Scanplane(instruments, plane3, numpts=[1600, 50], span=[800, 400], center=[0, 200], scanheight=30)
        scan.run()
        fields_set.append(m.Bset)
        fields.append(m.B)
        currents.append(m.I)
        scans.append(scan)
    for field in fields_down:
        m.ramp_to_field(field, rate=0.001)
        s.reset()
        scan = Scanplane(instruments, plane3, numpts=[1600, 50], span=[800, 400], center=[0, 200], scanheight=30)
        scan.run()
        fields_set.append(m.Bset)
        fields.append(m.B)
        currents.append(m.I)
        scans.append(scan)