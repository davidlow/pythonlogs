plt.close('all')
sc = Scanplane(instruments,plane0,span=[800,800], center=[0,0], 
            numpts=[2000,162],scan_rate=3, scanheight=40)
sc.notes = '''
[dhl88]  Long scan
'''
sc.run()

scheight = ['','','','']
i=0

for height in [70,60,50,40]:
    scheight[i] = Scanplane(instruments,plane0,span=[800,800],center=[0,0],
                    numpts=[2000,80],scan_rate=20,scanheight=height)
    scheight[i].notes = "For subtractions"
    scheight[i].run()
    i=i+1
