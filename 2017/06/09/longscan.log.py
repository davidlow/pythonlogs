# IPython log file

# Fri, 09 Jun 2017 05:19:57
get_ipython().magic('load qtconsole/2017/06/setups/main_20170608.py')
# Fri, 09 Jun 2017 05:20:00
# %load qtconsole/2017/06/setups/main_20170608.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170606.py')
pf = Planefit.load(instruments=instruments)
# %run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code

# Fri, 09 Jun 2017 05:20:24
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Fri, 09 Jun 2017 05:20:39
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Fri, 09 Jun 2017 05:20:56
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170609.py')
# Fri, 09 Jun 2017 05:20:58
# %load qtconsole/2017/06/setups/quickscan_20170609.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  Quick scan for testing scanning
'''
sc.run()

