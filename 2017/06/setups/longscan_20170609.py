plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], numpts=[2000,900],scan_rate=20, scanheight=15)
sc.notes = '''
[dhl88]  Long scan.  I want a good image to compare with 10 mK

Set for 10 hr at close to touching height
'''
sc.run()

# [dhl88] Actually took 12.9 hr