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