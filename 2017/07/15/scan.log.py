# IPython log file

# Sat, 15 Jul 2017 13:39:25
td = Touchdown(instruments=instruments)
# Sat, 15 Jul 2017 13:39:36
get_ipython().magic('run -i qtconsole/2017/07/setups/setup_20170714.py')
# Sat, 15 Jul 2017 13:39:47
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xc36c518>
# Sat, 15 Jul 2017 13:39:51
s.__getstate__()
#[Out]# {'Array bias': 44,
#[Out]#  'Array flux': 14,
#[Out]#  'Array locked': False,
#[Out]#  'Feedback resistor': '100kOhm',
#[Out]#  'Integrator capacitor': '1.5nF',
#[Out]#  'Preamp voltage offset': 0.3,
#[Out]#  'SQUID bias': 980,
#[Out]#  'SQUID flux': 100,
#[Out]#  'SQUID locked': True,
#[Out]#  'Test input': 'S_flux',
#[Out]#  'Test signal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'resetIntegrator': False,
#[Out]#  'sensitivity': 'High'}
# Sat, 15 Jul 2017 13:39:56
s.reset()
# Sat, 15 Jul 2017 13:40:03
td = Touchdown(instruments=instruments)
# Sat, 15 Jul 2017 13:40:05
td.run()
# Sat, 15 Jul 2017 13:57:28
td.run()
# Sat, 15 Jul 2017 16:02:25
pf = Planefit(instruments=instruments)
# Sat, 15 Jul 2017 16:02:28
pf.run()
# Sat, 15 Jul 2017 16:33:00
get_ipython().magic('load qtconsole/2017/07/setups/quickscan_20170715.py')
# Sat, 15 Jul 2017 16:34:31
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 16:49:27
atto
#[Out]# <Nowack_Lab.Instruments.attocube.Attocube at 0xc367ef0>
# Sat, 15 Jul 2017 16:49:42
atto.x.step(-100)
# Sat, 15 Jul 2017 16:49:49
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 17:02:00
atto.x.step(200)
# Sat, 15 Jul 2017 17:02:06
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 17:14:45
atto.x.step(200)
# Sat, 15 Jul 2017 17:14:52
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 17:24:33
atto.x.step(200)
# Sat, 15 Jul 2017 17:24:38
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 17:34:04
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  4K quick scan
'''
sc.run()

# Sat, 15 Jul 2017 17:44:55
pf = Planefit(instruments=instruments)
# Sat, 15 Jul 2017 17:45:20
pf = Planefit.load()
# Sat, 15 Jul 2017 17:45:21
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0x12a8df28>
# Sat, 15 Jul 2017 17:45:27
pf.timestamp
#[Out]# '2017-07-15 04:02:25 PM'
# Sat, 15 Jul 2017 17:45:47
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  corrected lockin, now outputting x and y, not R and theta
'''
sc.run()

# Sat, 15 Jul 2017 17:46:34
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  corrected lockin, now outputting x and y, not R and theta
'''
sc.run()

# Sat, 15 Jul 2017 17:46:46
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0x12a8df28>
