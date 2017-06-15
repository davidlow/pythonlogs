import numpy as np
import matplotlib.pyplot as plt
import Nowack_Lab.Procedures.scanplane
from Nowack_Lab.Procedures.scanplane import Scanplane

file = (
	r"C:\cygwin64\home\B82A\data\spruce\experiments\2017-06-10_10mk_scans\2017-06-14\2017-06-14_000439_Scanplane.json"
	);

line = 1

sp = Scanplane.load(file);
ventries = ['acx', 'acy', 'dc' ,'cap'];

#for entry in ventries:
#		ax[entry] = sp.V[entry];

fig, ax = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
ax = list(ax.flatten())

for entry in range(len(ventries)):
	ax[entry].plot(sp.X[line], sp.V[ventries[entry]][line]);
	ax[entry].set_ylabel([ventries[entry], " V"]);

ax[-1].set_xlabel('V')
ax[0].set_title("{0}: [x,y,z] = [x,{1:d},{2:d}]".format(
				sp.timestamp,
				int(sp.Y[line][0]),
				int(sp.Z[line][0])
			)
)
fig.tight_layout()