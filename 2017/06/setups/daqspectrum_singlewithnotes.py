spectrum = DaqSpectrum(instruments=instruments, 
                        measure_time=1, 
                        annotate_notes=True,
                        preamp_gain_override=True,
                        preamp_filter_override=True,
                        preamp_dccouple_override=False,
                        preamp_dccouple=True
            )
pzvals = pz.V;
spectrum.notes = '''short scan, 
[x,y,z] = [{0:d},{1:d},{2:d}]
[c, c0] = [{3:2.2e}, {4:2.2e}]
[gain, filter f] = [{5:d}, {6:2.2e}]
[time, averages] = [{7:2.2f}, {8:d}]
[A_bias, A_flux, S_bias, S_flux] = [{9:2.2f}, {10:2.2f}, {11:2.2f}, {12:2.2f}]
[Alocked, Slocked, sensitivity] = [{13}, {14}, {15}]
[units, conversion] = [{16},{17:2.4f}]
'''.format(int(pzvals['x']), 
           int(pzvals['y']), 
           int(pzvals['z']),
           instruments['lockin_cap'].R,
           CAP_I,
           instruments['preamp'].gain,
           instruments['preamp'].filter[1],
           spectrum.measure_time,
           spectrum.averages,
           instruments['squidarray'].A_bias,
           instruments['squidarray'].A_flux,
           instruments['squidarray'].S_bias,
           instruments['squidarray'].S_flux,
           instruments['squidarray'].__getstate__()['Array locked'],
           instruments['squidarray'].__getstate__()['SQUID locked'],
           instruments['squidarray'].__getstate__()['sensitivity'],
           spectrum.units,
           spectrum.conversion
);
spectrum.run()