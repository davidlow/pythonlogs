import numpy as np
import h5py

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments",
	r"\2017-06-10_10mk_scans\2017-06-14\extras\2017-06-14_000516_Line.h5"
	);


with h5py.File(file,'r') as f:
	# for k in f.keys():
	#     print(k);
	dc = f['Vfull']['dc'];
	pz = f['Vfull']['piezo'];
