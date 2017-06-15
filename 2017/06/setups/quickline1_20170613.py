plt.close('all')
sl = Scanline(instruments,pf,
	start=(100,0),
	end=(300,0),
	scan_rate=100,
	scanheight=15
);
sl.notes = '''[dhl88]  Quick Line scan
'''
sl.run()