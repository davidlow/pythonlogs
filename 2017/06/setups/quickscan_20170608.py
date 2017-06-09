plt.close('all')
pf = Planefit.load();
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  Quick scan for testing scanning
'''
sc.run()