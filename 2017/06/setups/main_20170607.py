### Setup script main, run me and modify
### Author: david low (dhl88)

%logstart -ot qtconsole/2017/06/07/longscan_daqspectrum.log.py rotate
%matplotlib qt5
%run -i qtconsole/2017/06/setups/setup_20170606.py
pf = Planefit.load(instruments=instruments)
%run -i qtconsole/2017/06/setups/longscan_daqspectrum.py

# 2017-06-07T15:31 reproduced this error with just this code