spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '8.5 mK'
spectrum.squidspectra()
spectrum.run()
