# IPython log file

get_ipython().magic('load qtconsole/2017/07/setups/startlog_20170703.py')
# Mon, 03 Jul 2017 21:23:12
get_ipython().magic('load qtconsole/2017/07/setups/main_20170703.py')
# Mon, 03 Jul 2017 21:23:13
# %load qtconsole/2017/07/setups/main_20170703.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/07/setups/setup_20170703.py')

# Mon, 03 Jul 2017 21:23:38
sa
# Mon, 03 Jul 2017 21:23:40
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xcb1d7b8>
# Mon, 03 Jul 2017 21:23:47
s.__getstatus__()
# Mon, 03 Jul 2017 21:23:52
s.__getstate__()
#[Out]# {'Array bias': 0,
#[Out]#  'Array flux': 0,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0,
#[Out]#  'SQUID bias': 0,
#[Out]#  'SQUID flux': 0,
#[Out]#  'SQUID locked': False,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Mon, 03 Jul 2017 21:23:56
s.reset()
# Mon, 03 Jul 2017 21:24:07
s.heat()
# Mon, 03 Jul 2017 21:24:19
s.heat()
# Mon, 03 Jul 2017 21:25:03
s.A_bias=43
# Mon, 03 Jul 2017 21:25:14
s.testInput
#[Out]# 'S_flux'
# Mon, 03 Jul 2017 21:25:19
s.testInput = "A_flux'
# Mon, 03 Jul 2017 21:25:22
s.testInput = "A_flux"
# Mon, 03 Jul 2017 21:25:27
s.testSignal
#[Out]# 'Off'
# Mon, 03 Jul 2017 21:25:29
s.testSignal = 'On'
# Mon, 03 Jul 2017 21:25:33
s.reset()
# Mon, 03 Jul 2017 21:25:51
s.heat(.5,20)
# Mon, 03 Jul 2017 21:27:01
s.A_bias
#[Out]# 43
# Mon, 03 Jul 2017 21:27:03
s.A_bias = 42
# Mon, 03 Jul 2017 21:27:12
s.A_flux
#[Out]# 0
# Mon, 03 Jul 2017 21:27:13
s.A_flux = 1
# Mon, 03 Jul 2017 21:27:18
s.A_flux = 0
# Mon, 03 Jul 2017 21:27:20
s.offset
#[Out]# 0
# Mon, 03 Jul 2017 21:27:22
s.offset = .1
# Mon, 03 Jul 2017 21:27:28
s.offset = .15
# Mon, 03 Jul 2017 21:27:52
s.lock('Array')
# Mon, 03 Jul 2017 21:27:55
s.reset()
# Mon, 03 Jul 2017 21:27:59
s.A_flux
#[Out]# 0
# Mon, 03 Jul 2017 21:28:01
s.A_flux = 10
# Mon, 03 Jul 2017 21:28:03
s.A_flux = 5
# Mon, 03 Jul 2017 21:28:09
s.testInput
#[Out]# 'A_flux'
# Mon, 03 Jul 2017 21:28:13
s.testInput = 'S_flux'
# Mon, 03 Jul 2017 21:28:57
s.A_bias
#[Out]# 42
# Mon, 03 Jul 2017 21:29:02
s.S_bias
#[Out]# 0
# Mon, 03 Jul 2017 21:29:07
s.S_bias = 100
# Mon, 03 Jul 2017 21:29:10
s.S_bias = 1000
# Mon, 03 Jul 2017 21:29:17
s.S_bias = 1400
# Mon, 03 Jul 2017 21:29:19
s.reset()
# Mon, 03 Jul 2017 21:29:29
s.S_bias = 1420
# Mon, 03 Jul 2017 21:29:33
s.S_bias = 1120
# Mon, 03 Jul 2017 21:29:37
s.S_bias = 1000
# Mon, 03 Jul 2017 21:29:40
s.S_bias = 900
# Mon, 03 Jul 2017 21:29:43
s.S_bias = 800
# Mon, 03 Jul 2017 21:29:46
s.S_bias = 500
# Mon, 03 Jul 2017 21:29:49
s.reset()
# Mon, 03 Jul 2017 21:29:56
s.S_bias = 100
# Mon, 03 Jul 2017 21:29:58
s.reset()
# Mon, 03 Jul 2017 21:30:03
s.S_bias = 50
# Mon, 03 Jul 2017 21:30:07
s.S_bias = 60
# Mon, 03 Jul 2017 21:30:09
s.S_bias = 100
# Mon, 03 Jul 2017 21:30:13
s.S_bias = 200
# Mon, 03 Jul 2017 21:30:17
s.S_bias = 100
# Mon, 03 Jul 2017 21:30:24
s.A_flux
#[Out]# 5
# Mon, 03 Jul 2017 21:30:26
s.A_flux = 10
# Mon, 03 Jul 2017 21:30:34
s.A_flux = 12
# Mon, 03 Jul 2017 21:30:44
s.S_flux
#[Out]# 0
# Mon, 03 Jul 2017 21:30:47
s.S_flux = 10
# Mon, 03 Jul 2017 21:30:51
s.S_flux = 15
# Mon, 03 Jul 2017 21:30:53
s.S_flux = 20
# Mon, 03 Jul 2017 21:31:01
s.A_flux
#[Out]# 12
# Mon, 03 Jul 2017 21:31:03
s.A_flux = 11
# Mon, 03 Jul 2017 21:31:11
s.lock('Squid')
# Mon, 03 Jul 2017 21:31:16
s.reset()
# Mon, 03 Jul 2017 21:31:21
s.S_flux
#[Out]# 20
# Mon, 03 Jul 2017 21:31:24
s.S_flux = 21
# Mon, 03 Jul 2017 21:31:27
s.S_flux = 18
# Mon, 03 Jul 2017 21:31:31
s.S_flux = 15
# Mon, 03 Jul 2017 21:31:35
s.S_flux = 12
# Mon, 03 Jul 2017 21:31:41
s.testSignal
#[Out]# 'On'
# Mon, 03 Jul 2017 21:31:44
s.testSignal = 'Off'
# Mon, 03 Jul 2017 21:31:50
s.S_flux = 13
# Mon, 03 Jul 2017 21:31:52
s.S_flux = 10
# Mon, 03 Jul 2017 21:31:54
s.S_flux = 11
# Mon, 03 Jul 2017 21:32:00
s.S_flux = 9
# Mon, 03 Jul 2017 21:41:28
get_ipython().magic('load qtconsole/2017/07/setups/annotatedspectrum_20170626.py')
# Mon, 03 Jul 2017 21:41:39
# %load qtconsole/2017/07/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Mon, 03 Jul 2017 21:44:51
s.__getstate__()
#[Out]# {'Array bias': 42,
#[Out]#  'Array flux': 11,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.15,
#[Out]#  'SQUID bias': 100,
#[Out]#  'SQUID flux': 9,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Mon, 03 Jul 2017 21:44:59
s.testSignal='On'
# Mon, 03 Jul 2017 21:45:07
s.lock('Array')
# Mon, 03 Jul 2017 21:45:11
s.reset()
# Mon, 03 Jul 2017 21:45:17
s.S_bias
#[Out]# 100
# Mon, 03 Jul 2017 21:45:19
s.S_bias = 200
# Mon, 03 Jul 2017 21:45:22
s.S_bias = 300
# Mon, 03 Jul 2017 21:45:25
s.S_bias = 400
# Mon, 03 Jul 2017 21:45:27
s.S_bias = 500
# Mon, 03 Jul 2017 21:45:31
s.S_bias = 600
# Mon, 03 Jul 2017 21:45:34
s.reset()
# Mon, 03 Jul 2017 21:45:35
s.reset()
# Mon, 03 Jul 2017 21:45:40
s.S_bias = 550
# Mon, 03 Jul 2017 21:45:44
s.S_bias = 500
# Mon, 03 Jul 2017 21:45:46
s.S_bias = 550
# Mon, 03 Jul 2017 21:45:49
s.reset()
# Mon, 03 Jul 2017 21:45:55
s.A_flux
#[Out]# 11
# Mon, 03 Jul 2017 21:45:57
s.A_flux = 12
# Mon, 03 Jul 2017 21:45:59
s.A_flux = 5
# Mon, 03 Jul 2017 21:46:05
s.A_flux = 6
# Mon, 03 Jul 2017 21:48:01
s.lock('Squid')
# Mon, 03 Jul 2017 21:48:06
s.testSignal
#[Out]# 'On'
# Mon, 03 Jul 2017 21:48:09
s.testSignal = 'Off'
# Mon, 03 Jul 2017 21:48:15
s.S_flux
#[Out]# 9
# Mon, 03 Jul 2017 21:48:17
s.S_flux = 8
# Mon, 03 Jul 2017 21:48:19
s.S_flux = 10
# Mon, 03 Jul 2017 21:48:23
s.S_flux = 11
# Mon, 03 Jul 2017 21:48:26
s.S_flux = 12
# Mon, 03 Jul 2017 21:48:47
s.S_flux = 12.5
# Mon, 03 Jul 2017 21:49:17
get_ipython().magic('load qtconsole/2017/07/setups/annotatedspectrum_20170626.py')
# Mon, 03 Jul 2017 21:49:25
# %load qtconsole/2017/07/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Mon, 03 Jul 2017 21:51:28
s.lock('Array')
# Mon, 03 Jul 2017 21:51:31
s.reset()
# Mon, 03 Jul 2017 21:51:44
s.S_bias
#[Out]# 550
# Mon, 03 Jul 2017 21:51:46
s.S_bias = 0
# Mon, 03 Jul 2017 21:51:50
s.reset()
# Mon, 03 Jul 2017 21:51:57
s.A_flux
#[Out]# 6
# Mon, 03 Jul 2017 21:52:00
s.A_flux - 5
#[Out]# 1
# Mon, 03 Jul 2017 21:52:05
s.A_flux = 5
# Mon, 03 Jul 2017 21:52:08
s.A_flux = 4
# Mon, 03 Jul 2017 21:52:32
# %load qtconsole/2017/07/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.arrayspectra()
spectrum.run()

# Mon, 03 Jul 2017 21:54:18
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xcb1d7b8>
# Mon, 03 Jul 2017 21:54:31
s.S_bias = 100
# Mon, 03 Jul 2017 21:54:34
s.reset()
# Mon, 03 Jul 2017 21:54:36
s.reset()
# Mon, 03 Jul 2017 21:54:46
s.testSignal
#[Out]# 'Off'
# Mon, 03 Jul 2017 21:54:48
s.testSignal = 'On'
# Mon, 03 Jul 2017 21:54:53
s.A_flux
#[Out]# 4
# Mon, 03 Jul 2017 21:55:00
s.A_flux = 11
# Mon, 03 Jul 2017 21:55:47
s.S_bias = 700
# Mon, 03 Jul 2017 21:55:50
s.S_bias = 800
# Mon, 03 Jul 2017 21:55:53
s.S_bias = 900
# Mon, 03 Jul 2017 21:55:56
s.S_bias = 1000
# Mon, 03 Jul 2017 21:55:59
s.S_bias = 1100
# Mon, 03 Jul 2017 21:56:02
s.S_bias = 1200
# Mon, 03 Jul 2017 21:56:05
s.S_bias = 1300
# Mon, 03 Jul 2017 21:56:10
s.S_bias = 1400
# Mon, 03 Jul 2017 21:56:13
s.S_bias = 1500
# Mon, 03 Jul 2017 21:56:17
s.S_bias = 1600
# Mon, 03 Jul 2017 21:56:19
s.reset()
# Mon, 03 Jul 2017 21:56:24
s.S_bias = 1700
# Mon, 03 Jul 2017 21:56:27
s.S_bias = 1800
# Mon, 03 Jul 2017 21:56:30
s.S_bias = 1900
# Mon, 03 Jul 2017 21:56:33
s.S_bias = 190
# Mon, 03 Jul 2017 21:56:36
s.reset()
# Mon, 03 Jul 2017 21:56:44
s.S_bias = 200
# Mon, 03 Jul 2017 21:57:01
s.lock('Squid')
# Mon, 03 Jul 2017 21:57:08
s.testSignal='Off'
# Mon, 03 Jul 2017 21:57:16
s.S_flux
#[Out]# 12.5
# Mon, 03 Jul 2017 21:57:19
s.S_flux = 15
# Mon, 03 Jul 2017 21:57:22
s.S_flux = 8
# Mon, 03 Jul 2017 21:57:25
s.S_flux = 6
# Mon, 03 Jul 2017 21:57:43
get_ipython().magic('load qtconsole/2017/07/setups/annotatedspectrum_20170626.py')
# Mon, 03 Jul 2017 21:57:52
# %load qtconsole/2017/07/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 1, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Mon, 03 Jul 2017 21:59:38
# %load qtconsole/2017/07/setups/annotatedspectrum_20170626.py
spectrum = AnnotatedSpectrum(1,instruments, 
        measure_time = 30, 
        preamp_filter_override=True, 
        preamp_dccouple_override=True, 
        preamp_autoOL=False, 
        annotate_piezos=False, 
        annotate_cap = False)
spectrum.notes = '4K'
spectrum.squidspectra()
spectrum.run()

# Mon, 03 Jul 2017 23:06:04
s.zero()
# Mon, 03 Jul 2017 23:06:11
exit()
