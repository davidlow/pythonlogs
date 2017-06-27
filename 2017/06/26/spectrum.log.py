# IPython log file

# Mon, 26 Jun 2017 20:59:09
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170622.py')
# Mon, 26 Jun 2017 20:59:28
s.__getstate__()
#[Out]# {'Array bias': 0.0,
#[Out]#  'Array flux': 0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'A_flux',
#[Out]#  'Test signal': 'Auto',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Mon, 26 Jun 2017 20:59:39
s.A_bias = 44
# Mon, 26 Jun 2017 21:00:00
s.offset
#[Out]# 0.0
# Mon, 26 Jun 2017 21:00:04
s.offset = .1
# Mon, 26 Jun 2017 21:00:07
s.offset = .2
# Mon, 26 Jun 2017 21:00:12
s.offset = .18
# Mon, 26 Jun 2017 21:00:23
s.S_bias
#[Out]# 0
# Mon, 26 Jun 2017 21:00:34
s.lock('Array')
# Mon, 26 Jun 2017 21:00:38
s.reset()
# Mon, 26 Jun 2017 21:00:41
s.reset()
# Mon, 26 Jun 2017 21:00:42
s.reset()
# Mon, 26 Jun 2017 21:00:45
s.A_flux
#[Out]# 0
# Mon, 26 Jun 2017 21:00:47
s.A_flux = 10
# Mon, 26 Jun 2017 21:00:51
s.reset()
# Mon, 26 Jun 2017 21:00:55
s.A_flux = 15
# Mon, 26 Jun 2017 21:00:57
s.A_flux = 5
# Mon, 26 Jun 2017 21:01:03
s.sensitivity
#[Out]# 'High'
# Mon, 26 Jun 2017 21:01:25
s.testInput
#[Out]# 'A_flux'
# Mon, 26 Jun 2017 21:01:29
s.testInput = 'S_flux'
# Mon, 26 Jun 2017 21:01:32
s.testSignal
#[Out]# 'Auto'
# Mon, 26 Jun 2017 21:01:35
s.testSignal = 'On'
# Mon, 26 Jun 2017 21:01:45
s.S_bias = 1424
# Mon, 26 Jun 2017 21:01:49
s.rest()
# Mon, 26 Jun 2017 21:01:52
s.reset()
# Mon, 26 Jun 2017 21:01:56
s.reset()
# Mon, 26 Jun 2017 21:02:00
s.A_flux
#[Out]# 5
# Mon, 26 Jun 2017 21:02:02
s.A_flux = 0
# Mon, 26 Jun 2017 21:02:04
s.A_flux = 10
# Mon, 26 Jun 2017 21:02:42
s.S_bias = 1420
# Mon, 26 Jun 2017 21:02:48
s.S_bias = 1418
# Mon, 26 Jun 2017 21:02:52
s.S_bias = 1430
# Mon, 26 Jun 2017 21:02:54
s.S_bias = 1420
# Mon, 26 Jun 2017 21:03:03
s.A_flux = 12
# Mon, 26 Jun 2017 21:03:05
s.A_flux = 9
# Mon, 26 Jun 2017 21:03:10
s.A_flux = 9.5
# Mon, 26 Jun 2017 21:03:23
s.lock('Squid')
# Mon, 26 Jun 2017 21:03:28
s.testInput
#[Out]# 'S_flux'
# Mon, 26 Jun 2017 21:03:31
s.testSignal
#[Out]# 'On'
# Mon, 26 Jun 2017 21:03:34
s.testSignal = 'Off'
# Mon, 26 Jun 2017 21:03:40
s.reset()
# Mon, 26 Jun 2017 21:03:46
s.A_flux
#[Out]# 9.5
# Mon, 26 Jun 2017 21:03:50
s.S_flux
#[Out]# 0
# Mon, 26 Jun 2017 21:03:52
s.S_flux = 1
# Mon, 26 Jun 2017 21:03:56
s.S_flux = 2
# Mon, 26 Jun 2017 21:04:37
pa.__getstate__()
#[Out]# {'dccoupled': True, 'filter': (1000, 10000), 'gain': 250, 'overloaded': False}
# Mon, 26 Jun 2017 21:05:02
pa.__getstate__()
#[Out]# {'dccoupled': True, 'filter': (1000, 10000), 'gain': 250, 'overloaded': False}
# Mon, 26 Jun 2017 21:07:59
get_ipython().magic('load qtconsole/2017/06/setups/annotatedspectrum_20170626.py')
# Mon, 26 Jun 2017 21:08:01
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
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

# Mon, 26 Jun 2017 21:09:24
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 30, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '8.5 mK'
spectrum.squidspectra()
spectrum.run()

# Mon, 26 Jun 2017 21:28:12
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 9.5,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.18,
#[Out]#  'SQUID bias': 1420,
#[Out]#  'SQUID flux': 2,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Mon, 26 Jun 2017 21:28:21
s.lock('Array')
# Mon, 26 Jun 2017 21:28:30
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 9.5,
#[Out]#  'Array locked': True,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.18,
#[Out]#  'SQUID bias': 1420,
#[Out]#  'SQUID flux': 2,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Mon, 26 Jun 2017 21:28:48
s.S_bias=0
# Mon, 26 Jun 2017 21:28:51
s.reset()
# Mon, 26 Jun 2017 21:28:53
s.reset()
# Mon, 26 Jun 2017 21:28:58
s.S_flux =0
# Mon, 26 Jun 2017 21:29:02
s.A_flux
#[Out]# 9.5
# Mon, 26 Jun 2017 21:29:05
s.A_flux = 10
# Mon, 26 Jun 2017 21:29:07
s.A_flux = 5
# Mon, 26 Jun 2017 21:29:11
s.reset()
# Mon, 26 Jun 2017 21:29:21
s.A_flux = 5.1
# Mon, 26 Jun 2017 21:29:26
s.A_flux = 5.3
# Mon, 26 Jun 2017 21:29:44
pa.__getstate__()
#[Out]# {'dccoupled': True, 'filter': (1000, 10000), 'gain': 1000, 'overloaded': False}
# Mon, 26 Jun 2017 21:29:58
get_ipython().magic('load qtconsole/2017/06/setups/annotatedspectrum_20170626.py')
# Mon, 26 Jun 2017 21:30:00
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
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

# Mon, 26 Jun 2017 21:31:29
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 30, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '8.5 mK'
spectrum.squidspectra()
spectrum.run()

# Mon, 26 Jun 2017 21:51:10
# %load qtconsole/2017/06/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '8.5 mK, keithley off, unplugged'
spectrum.squidspectra()
spectrum.run()

# Mon, 26 Jun 2017 21:53:08
s.zero()
# Mon, 26 Jun 2017 21:53:17
s.reset()
