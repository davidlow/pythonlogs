heights = np.linspace(100,0,13)
sc = []
i = 0
for h in heights:
    print("{0}/13: height={1}".format(i,h))
    sc.append(Scanplane(instruments,plane0,span=[800,800], center=[0,0], 
            numpts=[2000,100],scan_rate=50, scanheight=h))
    sc[i].notes = '''
    Scan in height series
    '''
    sc[i].run()
    i=i+1
