plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2340,780],scan_rate=10, scanheight=30)
sc.notes = '''
[dhl88]  Long scan
'''
sc.run()
