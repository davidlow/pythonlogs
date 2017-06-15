plt.close('all')
sc = Scanplane(instruments,pf,
	span=[800,1], 
	center=[0,0], 
	numpts=[2000,3],
	scan_rate=100, 
	scanheight=15
);
sc.notes = '''[dhl88]  Quick Line scan
'''
sc.run()