# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Fri, 09 Jun 2017 02:59:33
get_ipython().magic('load qtconsole/2017/06/setups/main_20170608.py')
# Fri, 09 Jun 2017 02:59:35
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Fri, 09 Jun 2017 03:00:03
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170608.py')
# Fri, 09 Jun 2017 03:00:25
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  Quick scan for testing scanning, last time, code changed
and lockin on and sending current
'''
sc.run()

# Fri, 09 Jun 2017 03:41:54
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
# pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  Couldn't get code to work, scanning closer to see how 
close I can scan reliably
'''
sc.run()

# Fri, 09 Jun 2017 03:54:50
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
# pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=7)
sc.notes = '''
[dhl88]  Couldn't get code to work, scanning closer to see how 
close I can scan reliably
'''
sc.run()

# Fri, 09 Jun 2017 04:15:26
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
# pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=11)
sc.notes = '''
[dhl88]  Splitting the difference between no touching scan and touching
scan
'''
sc.run()

# Fri, 09 Jun 2017 04:27:54
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
# pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=13)
sc.notes = '''
[dhl88]  Splitting the difference between no touching scan and touching
scan
'''
sc.run()

# Fri, 09 Jun 2017 05:09:31
get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Fri, 09 Jun 2017 05:10:13
# %load qtconsole/2017/06/setups/startlog_20170608.py
### Just starts logs.  This will never be in the log file
### Author: david low (dhl88)

get_ipython().magic('logstart -ot qtconsole/2017/06/09/longscan.log.py rotate')
# Fri, 09 Jun 2017 05:10:19
get_ipython().magic('logoff')
