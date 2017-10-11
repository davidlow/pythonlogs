spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        averages = 30,
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
#spectrum.notes = 'T = {0}K'.format(lakeshore.T[6])
spectrum.arrayspectra()
spectrum.run()
