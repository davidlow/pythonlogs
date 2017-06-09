# IPython log file

# Fri, 09 Jun 2017 01:12:38
pf = Planefit(instruments)
# Fri, 09 Jun 2017 01:12:41
pf.run()
# Fri, 09 Jun 2017 01:41:52
get_ipython().magic('load qtconsole/2017/06/setups/quickscan_20170608.py')
# Fri, 09 Jun 2017 01:42:06
# %load qtconsole/2017/06/setups/quickscan_20170608.py
plt.close('all')
pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  Quick scan for testing scanning with new matt plane
'''
sc.run()

