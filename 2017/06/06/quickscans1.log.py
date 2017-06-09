# IPython log file

# Tue, 06 Jun 2017 20:06:57
get_ipython().magic('run qtconsole/2017/06/setups/setup_20170606.py')
# Tue, 06 Jun 2017 20:07:22
pf = Planefit.load(r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-05-29_daqapproach\2017-06-06\2017-06-06_025437_Planefit.json", instruments=instruments)
# Tue, 06 Jun 2017 20:07:30
get_ipython().magic('matplotlib notebook')
# Tue, 06 Jun 2017 20:08:06
get_ipython().magic('run qtconsole/2017/06/setups/quickscan_20170606.py')
# Tue, 06 Jun 2017 20:08:12
plt
#[Out]# <module 'matplotlib.pyplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py'>
# Tue, 06 Jun 2017 20:08:21
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170606.py')
# Tue, 06 Jun 2017 20:08:24
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

# Tue, 06 Jun 2017 20:14:43
get_ipython().magic('matplotlib inline')
# Tue, 06 Jun 2017 20:14:55
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

# Tue, 06 Jun 2017 20:17:54
get_ipython().magic('matplotlib notebook')
# Tue, 06 Jun 2017 20:18:01
get_ipython().magic('matplotlib qt')
# Tue, 06 Jun 2017 20:18:27
get_ipython().magic('matplotlib qt4')
# Tue, 06 Jun 2017 20:18:30
get_ipython().magic('matplotlib qt5')
# Tue, 06 Jun 2017 20:18:32
get_ipython().magic('matplotlib tk')
# Tue, 06 Jun 2017 20:18:35
get_ipython().magic('matplotlib wx')
# Tue, 06 Jun 2017 20:18:40
get_ipython().magic('matplotlib gtk')
# Tue, 06 Jun 2017 20:18:45
get_ipython().magic('matplotlib inline')
# Tue, 06 Jun 2017 20:18:48
get_ipython().magic('matplotlib gtk')
# Tue, 06 Jun 2017 20:18:52
get_ipython().magic('matplotlib gtk3')
# Tue, 06 Jun 2017 20:19:00
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

