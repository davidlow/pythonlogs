v = spectrum.V;
[h,edges] = np.histogram(v,int(2**16));
[fig,ax] = plt.subplots();
ax.plot(edges[0:-1],h)