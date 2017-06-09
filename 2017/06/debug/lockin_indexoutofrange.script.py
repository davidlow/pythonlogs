# reproduce lockin list index out of range

%logstart -ot qtconsole/2017/06/debug/lockin_indexoutofrange.log.py rotate
%matplotlib qt5
%run -i qtconsole/2017/06/setups/setup_20170606.py
pf = Planefit.load(instruments=instruments)
%run -i qtconsole/2017/06/debug/longscan_daqspectrum.debug.py

# 2017-06-07T15:31 reproduced this error with just this code