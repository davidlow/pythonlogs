# IPython log file

get_ipython().magic('load qtconsole/2017/06/setups/startlog_20170608.py')
# Wed, 14 Jun 2017 22:35:46
get_ipython().magic('load qtconsole/2017/06/setups/main_20170613.py')
# Wed, 14 Jun 2017 22:35:47
# %load qtconsole/2017/06/setups/main_20170613.py
### Setup script main, load me and modify
### Author: david low (dhl88)

get_ipython().magic('matplotlib qt5')
get_ipython().magic('run -i qtconsole/2017/06/setups/setup_20170613.py')

# Wed, 14 Jun 2017 22:36:00
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-08_mattplane_and_scan\2017-06-09\2017-06-09_011238_Planefit.json", instruments=instruments)
# Wed, 14 Jun 2017 22:36:12
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
# Wed, 14 Jun 2017 23:08:22
CAP_I = instruments['lockin_cap'].R
# Wed, 14 Jun 2017 23:08:28
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
# Wed, 14 Jun 2017 23:56:31
get_ipython().magic('run -i qtconsole/2017/06/setups/longscan_vibrationtest.py')
