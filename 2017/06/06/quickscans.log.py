# IPython log file

get_ipython().magic('matplotlib tk')
# Tue, 06 Jun 2017 20:25:21
get_ipython().magic('run qtconsole/2017/06/setups/setup_20170606.py')
# Tue, 06 Jun 2017 20:25:32
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-05-29_daqapproach\2017-06-06\2017-06-06_025437_Planefit.json", instruments=instruments)
# Tue, 06 Jun 2017 20:26:38
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170606.py')
# Tue, 06 Jun 2017 20:26:41
# %load qtconsole/2017/06/setups/quickscan_20170606.py
plt.close('all')
#pz.z.sweep(pz.z.V, -pz.z.Vmax)
#atto.x.step(50)
#pz.zero()
#pf.update_c()
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=60)
sc.notes = '''
[dhl88]  Quick scan for testing scanning in qtconsole
'''
sc.run()

# Tue, 06 Jun 2017 20:48:11
plt.close('all')
# Tue, 06 Jun 2017 20:50:11
from guppy import hpy; h=hpy()
