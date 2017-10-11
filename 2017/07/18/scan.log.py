# IPython log file

get_ipython().magic('load qtconsole/2017/07/setups/startlog_20170703.py')
# Tue, 18 Jul 2017 18:11:45
get_ipython().magic('run -i qtconsole/2017/07/setups/setup_20170714.py')
# Tue, 18 Jul 2017 18:12:52
pf = Planefit.load()
# Tue, 18 Jul 2017 18:12:54
pf
#[Out]# <Nowack_Lab.Procedures.planefit.Planefit at 0xe9b5208>
# Tue, 18 Jul 2017 18:13:19
get_ipython().magic('run -i qtconsole/2017/07/setups/quickscan_20170715.py')
# Tue, 18 Jul 2017 18:16:14
get_ipython().magic('run -i qtconsole/2017/07/setups/quickscan_20170715.py')
# Tue, 18 Jul 2017 18:17:02
pf = Planefit(instruments=instruments)
# Tue, 18 Jul 2017 18:17:05
pf.run()
# Tue, 18 Jul 2017 18:49:20
get_ipython().magic('run -i qtconsole/2017/07/setups/quickscan_20170715.py')
# Tue, 18 Jul 2017 18:50:11
get_ipython().magic('run -i qtconsole/2017/07/setups/quickscan_20170715.py')
# Tue, 18 Jul 2017 19:07:23
get_ipython().magic('run -i qtconsole/2017/07/setups/quickscan_20170715.py')
# Tue, 18 Jul 2017 19:20:01
get_ipython().magic('run -i qtconsole/2017/07/setups/longscan_20170715.py')
# Wed, 19 Jul 2017 13:38:10
pz.zero()
# Wed, 19 Jul 2017 13:38:22
instruments
#[Out]# {'atto': <Nowack_Lab.Instruments.attocube.Attocube at 0xe30bcf8>,
#[Out]#  'daq': <Nowack_Lab.Instruments.nidaq.NIDAQ at 0x4437208>,
#[Out]#  'lockin_cap': <Nowack_Lab.Instruments.lockin.SR830 at 0xc36e668>,
#[Out]#  'lockin_squid': <Nowack_Lab.Instruments.lockin.SR830 at 0xc36e898>,
#[Out]#  'montana': <Nowack_Lab.Instruments.montana.Montana at 0xc369a90>,
#[Out]#  'piezos': <Nowack_Lab.Instruments.piezos.Piezos at 0xc36ea58>,
#[Out]#  'preamp': <Nowack_Lab.Instruments.preamp.SR5113 at 0xc36e550>,
#[Out]#  'squidarray': <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe311208>}
# Wed, 19 Jul 2017 13:38:36
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:38:38
td.run()
# Wed, 19 Jul 2017 13:39:56
plane.a
# Wed, 19 Jul 2017 13:40:03
get_ipython().magic('pinfo pf')
# Wed, 19 Jul 2017 13:40:08
pf.a
#[Out]# 0.010175967792336593
# Wed, 19 Jul 2017 13:40:09
pf.b
#[Out]# 0.077672389216165705
# Wed, 19 Jul 2017 13:40:12
pf.c
#[Out]# 282.14607176217072
# Wed, 19 Jul 2017 13:41:26
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:41:28
td.run()
# Wed, 19 Jul 2017 13:52:08
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:52:10
td.run()
# Wed, 19 Jul 2017 13:54:17
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:54:21
td.run()
# Wed, 19 Jul 2017 13:56:16
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:56:18
td.run()
# Wed, 19 Jul 2017 13:58:28
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 13:58:29
td.run()
# Wed, 19 Jul 2017 14:02:35
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:02:36
td.run()
# Wed, 19 Jul 2017 14:05:01
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:05:02
td.run()
# Wed, 19 Jul 2017 14:07:57
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:07:58
td.run()
# Wed, 19 Jul 2017 14:09:59
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:10:00
td.run()
# Wed, 19 Jul 2017 14:11:53
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:11:54
td.run()
# Wed, 19 Jul 2017 14:13:36
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:13:37
td.run()
# Wed, 19 Jul 2017 14:15:27
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:15:28
td.run()
# Wed, 19 Jul 2017 14:17:23
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:17:25
td.run()
# Wed, 19 Jul 2017 14:19:31
plt.close("all")
# Wed, 19 Jul 2017 14:20:28
td = Touchdown(instruments, planescan=True)
# Wed, 19 Jul 2017 14:20:31
td.run()
# Wed, 19 Jul 2017 14:21:32
pf.c
#[Out]# 282.14607176217072
# Wed, 19 Jul 2017 14:21:36
pf.c = 148
# Wed, 19 Jul 2017 14:21:40
get_ipython().magic('pinfo sc')
# Wed, 19 Jul 2017 14:26:18
get_ipython().magic('pinfo Scanplane')
# Wed, 19 Jul 2017 14:26:48
scan = Scanplane(instruments, pf, span=[250,250], center = [-250, 100],  numpts=[500, 100], scanheight=20, scan_rate=100)
# Wed, 19 Jul 2017 14:31:08
scan.run()
# Wed, 19 Jul 2017 15:16:40
scan = Scanplane(instruments, pf, span=[250,250], center = [-250, 100],  numpts=[500, 100], scanheight=15, scan_rate=100)
# Wed, 19 Jul 2017 15:16:44
scan.run()
# Wed, 19 Jul 2017 15:39:00
scan = Scanplane(instruments, pf, span=[250,250], center = [-250, 100],  numpts=[500, 100], scanheight=10, scan_rate=100)
# Wed, 19 Jul 2017 15:39:02
scan.run()
# Wed, 19 Jul 2017 16:57:30
scan = Scanplane(instruments, pf, span=[100,100], center = [-220, 50],  numpts=[500, 500], scanheight=10, scan_rate=100)
# Wed, 19 Jul 2017 17:03:45
get_ipython().magic('pinfo dt')
# Wed, 19 Jul 2017 17:04:10
from Nowack_Lab.Procedures.daqtransport import DAQ_Transport
# Wed, 19 Jul 2017 17:04:26
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = -0.004,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.000,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.000,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = -0.002,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = -0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.125,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.104,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = 0.005,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.131,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.177,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.161,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.193,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.141,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = -0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = -0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = -0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = -0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = 0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.206,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = 0.002,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.002,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = 0.192,
#[Out]#  'capx': InputChannel; name: ai2; label: capx; V = -0.161,
#[Out]#  'capy': InputChannel; name: ai3; label: capy; V = -0.197,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.166,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 3.243}
# Wed, 19 Jul 2017 17:04:43
daq.inputs = {"voltage":2}
# Wed, 19 Jul 2017 17:04:44
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = 0.002,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.000,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.006,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = 0.001,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = 0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.128,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.105,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.146,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.171,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.190,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.166,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.198,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.147,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = 0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = -0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = -0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = -0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.212,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.001,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.001,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = 0.192,
#[Out]#  'capy': InputChannel; name: ai3; label: capy; V = -0.111,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.146,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 3.242,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = -0.300}
# Wed, 19 Jul 2017 17:05:07
daq.outputs = {"bias":3}
# Wed, 19 Jul 2017 17:05:10
daq.outputs 
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.001,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.001}
# Wed, 19 Jul 2017 17:09:16
dt = DAQ_Transport(instruments, -5e-6, 5e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:09:30
dt.run()
# Wed, 19 Jul 2017 17:10:16
l = lakeshore372()
# Wed, 19 Jul 2017 17:10:26
l = Lakeshore372()
# Wed, 19 Jul 2017 17:10:41
from Nowack_Lab.Instruments.lakeshore import Lakeshore372
# Wed, 19 Jul 2017 17:10:44
l = Lakeshore372()
# Wed, 19 Jul 2017 17:10:55
instruments['lakeshore'] = l
# Wed, 19 Jul 2017 17:11:07
dt = DAQ_Transport(instruments, -5e-6, 5e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:11:11
dt.run()
# Wed, 19 Jul 2017 17:11:58
dt = DAQ_Transport(instruments, -5e-6, 5e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:12:16
dt.run()
# Wed, 19 Jul 2017 17:13:04
dt = DAQ_Transport(instruments, -5e-6, 5e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:13:06
dt.run()
# Wed, 19 Jul 2017 17:13:38
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = 0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = -0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.000}
# Wed, 19 Jul 2017 17:13:58
dt = DAQ_Transport(instruments, -5e-6, 5e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:14:07
dt.run()
# Wed, 19 Jul 2017 17:14:23
fig, ax = plt.subplots()
# Wed, 19 Jul 2017 17:14:45
dt.plot()
# Wed, 19 Jul 2017 17:16:02
from Nowack_Lab.Procedures import daqtransport
# Wed, 19 Jul 2017 17:16:05
from imp import reload
# Wed, 19 Jul 2017 17:16:10
reload(daqtransport)
#[Out]# <module 'Nowack_Lab.Procedures.daqtransport' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqtransport.py'>
# Wed, 19 Jul 2017 17:16:37
dt = daqtransport.DAQ_Transport(instruments, 1e-6, 1e-6, 1e6, 90, 100)
# Wed, 19 Jul 2017 17:16:40
dt.run()
# Wed, 19 Jul 2017 17:16:53
dt.plot()
# Wed, 19 Jul 2017 17:21:12
dt = daqtransport.DAQ_Transport(instruments, 1e-6, 1e-6, 1e6, 9, 100)
# Wed, 19 Jul 2017 17:21:14
dt.run()
# Wed, 19 Jul 2017 17:21:47
dt.plot()
# Wed, 19 Jul 2017 17:22:45
dt = daqtransport.DAQ_Transport(instruments, -10e-6, 10e-6, 1e6, 9, 100)
# Wed, 19 Jul 2017 17:22:47
dt.run()
# Wed, 19 Jul 2017 17:23:15
dt.plot()
# Wed, 19 Jul 2017 17:24:31
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 1e6, 9, 100)
# Wed, 19 Jul 2017 17:24:52
dt.run()
# Wed, 19 Jul 2017 17:25:23
dt.plot()
# Wed, 19 Jul 2017 17:28:43
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = 0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.001,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.001}
# Wed, 19 Jul 2017 17:29:58
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 99e3, 9, 100)
# Wed, 19 Jul 2017 17:30:01
dt.run()
# Wed, 19 Jul 2017 17:30:30
dt.plot()
# Wed, 19 Jul 2017 17:32:22
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 99e3, 1, 100)
# Wed, 19 Jul 2017 17:32:25
dt.run()
# Wed, 19 Jul 2017 17:36:55
dt.plot()
# Wed, 19 Jul 2017 17:37:24
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 99e3, 1, 100)
# Wed, 19 Jul 2017 17:37:34
dt.run()
# Wed, 19 Jul 2017 17:42:01
dt.plot()
# Wed, 19 Jul 2017 18:58:34
get_ipython().magic('pinfo scan')
# Wed, 19 Jul 2017 18:58:52
scan = Scanplane(instruments, pf, span=[100,100], center = [-220, 50],  numpts=[500, 500], scanheight=10, scan_rate=100)
# Wed, 19 Jul 2017 18:58:54
pf.c
#[Out]# 148
# Wed, 19 Jul 2017 19:02:28
from datetime import datetime
# Wed, 19 Jul 2017 19:02:31
datetime.now()
#[Out]# datetime.datetime(2017, 7, 19, 19, 2, 31, 481000)
# Wed, 19 Jul 2017 19:04:38
get_ipython().magic('run -i qtconsole/2017/07/setups/longscan_20170719.py')
# Thu, 20 Jul 2017 10:38:01
get_ipython().magic('pinfo ds')
# Thu, 20 Jul 2017 10:38:32
dt = daqtransport.DAQ_Transport(instruments, -10e-6, 10e-6, 99e3, 1, 100)
# Thu, 20 Jul 2017 10:38:37
get_ipython().magic('pinfo daqtransport.DAQ_Transport')
# Thu, 20 Jul 2017 10:38:52
dt.run()
# Thu, 20 Jul 2017 10:40:03
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.990,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = -0.001,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = 0.000}
# Thu, 20 Jul 2017 10:40:51
_ = daq.sweep({'bias':daq.outputs['bias'].V}, 0, sample_rate = 10)
# Thu, 20 Jul 2017 10:40:57
daq.zero()
# Thu, 20 Jul 2017 10:41:12
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = 0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.001}
# Thu, 20 Jul 2017 10:41:19
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.002,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.001,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = 0.000,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.000,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = -0.001,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = 0.003,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = 0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = 0.001,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.481,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.191,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.108,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.122,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.185,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.182,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.206,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = 0.138,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.002,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = -0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = -0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = 0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = 0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.198,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = 0.001,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.003,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = 0.009,
#[Out]#  'capy': InputChannel; name: ai3; label: capy; V = -0.152,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.192,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = -0.049,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = -0.136}
# Thu, 20 Jul 2017 10:41:52
dt = daqtransport.DAQ_Transport(instruments, -10e-6, 10e-6, 99e3, 1, 100)
# Thu, 20 Jul 2017 10:41:55
plt.close("all")
# Thu, 20 Jul 2017 10:42:03
dt.run()
# Thu, 20 Jul 2017 10:45:31
dt.plot()
# Thu, 20 Jul 2017 10:48:20
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 99e3, 1, 100)
# Thu, 20 Jul 2017 10:48:26
dt.run()
# Thu, 20 Jul 2017 10:52:37
dt.plot()
# Thu, 20 Jul 2017 10:54:40
daq.ourputs
# Thu, 20 Jul 2017 10:54:43
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = 0.000}
# Thu, 20 Jul 2017 10:56:32
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 99e3, 1, 100)
# Thu, 20 Jul 2017 10:56:43
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 10:56:47
dt.run()
# Thu, 20 Jul 2017 11:01:38
dt.plot()
# Thu, 20 Jul 2017 11:02:37
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 11:02:41
dt.run()
# Thu, 20 Jul 2017 11:06:41
dt.plot()
# Thu, 20 Jul 2017 11:07:14
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xc36e550>
# Thu, 20 Jul 2017 11:07:37
pa2 = SR5113(port="COM2")
# Thu, 20 Jul 2017 11:08:34
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = 0.001,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.001,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.000,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = 0.002,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = -0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.174,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.158,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.033,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.162,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.196,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.188,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.212,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.169,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = -0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = -0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = 0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = -0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = 0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.240,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = 0.000,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.000,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = -0.037,
#[Out]#  'capy': InputChannel; name: ai3; label: capy; V = -2.087,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.712,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = -0.026,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = 0.481}
# Thu, 20 Jul 2017 11:09:04
daq.inpts = {"voltage2":3}
# Thu, 20 Jul 2017 11:09:19
daq.inputs = {"voltage3" : 3}
# Thu, 20 Jul 2017 11:09:21
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.001,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = 0.001,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.002,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.003,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = 0.001,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = 0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = -0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.179,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.164,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.187,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.204,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.208,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.192,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.214,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.169,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = -0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = -0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = -0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.001,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = -0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.244,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = 0.001,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = -0.002,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = -0.039,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.176,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 0.022,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = 0.338,
#[Out]#  'voltage3': InputChannel; name: ai3; label: voltage3; V = -2.045}
# Thu, 20 Jul 2017 11:09:31
daq.inputs = {"voltage2" : 3}
# Thu, 20 Jul 2017 11:09:33
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.001,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = -0.003,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = -0.001,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.001,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = 0.001,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.001,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = 0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.169,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.156,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.188,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.207,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.206,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.194,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.221,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.181,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = -0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = -0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = -0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = -0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.247,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.001,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.001,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = -0.002,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.166,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 0.011,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = 0.505,
#[Out]#  'voltage2': InputChannel; name: ai3; label: voltage2; V = -2.079}
# Thu, 20 Jul 2017 11:10:11
daqtransport.DAQ_Transport._daq_inputs
#[Out]# ['voltage']
# Thu, 20 Jul 2017 11:10:32
daqtransport.DAQ_Transport._daq_inputs = ['voltage', 'voltage2']
# Thu, 20 Jul 2017 11:11:08
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 11:11:15
dt.run()
# Thu, 20 Jul 2017 11:36:02
dt.plot()
# Thu, 20 Jul 2017 11:38:56
get_ipython().magic('pinfo reload')
# Thu, 20 Jul 2017 11:39:07
reload(daqtransport)
#[Out]# <module 'Nowack_Lab.Procedures.daqtransport' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqtransport.py'>
# Thu, 20 Jul 2017 11:39:29
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 11:39:34
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 11:40:27
ax.plot(dt.data2['bias']/dt.Rbias, dt.received2['voltage2']/10000)
#[Out]# [<matplotlib.lines.Line2D at 0x4334b908>]
# Thu, 20 Jul 2017 11:50:08
dt = daqtransport.DAQ_Transport(instruments, -200e-6, 200e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 11:50:13
dt.run()
# Thu, 20 Jul 2017 11:54:06
dt.plot()
# Thu, 20 Jul 2017 11:56:59
td.plot_both(gain2 = 25000)
# Thu, 20 Jul 2017 11:57:15
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 11:58:04
daqtransport.DAQ_Transport._daq_inputs = ['voltage', 'voltage2']
# Thu, 20 Jul 2017 11:58:23
dt = daqtransport.DAQ_Transport(instruments, -300e-6, 300e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 11:58:26
dt.run()
# Thu, 20 Jul 2017 12:02:03
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 12:05:11
dt = daqtransport.DAQ_Transport(instruments, -100e-6, 100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 12:05:15
dt.run()
# Thu, 20 Jul 2017 12:09:33
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 12:11:49
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 12:11:51
dt.run()
# Thu, 20 Jul 2017 12:15:27
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 12:16:21
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, .3, 100)
# Thu, 20 Jul 2017 12:16:27
dt.run()
# Thu, 20 Jul 2017 12:27:40
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 12:28:58
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 500)
# Thu, 20 Jul 2017 12:29:01
dt.run()
# Thu, 20 Jul 2017 12:46:01
dt.plot_both(gain2=2500)
# Thu, 20 Jul 2017 12:49:35
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = 0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.000}
# Thu, 20 Jul 2017 12:50:42
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 12:50:46
dt.run()
# Thu, 20 Jul 2017 12:54:16
dt.plot_both(gain2=2500)
# Thu, 20 Jul 2017 12:56:47
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 300)
# Thu, 20 Jul 2017 12:56:52
dt.run()
# Thu, 20 Jul 2017 13:07:06
dt.plot_both(gain2=2500)
# Thu, 20 Jul 2017 13:08:52
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 300)
# Thu, 20 Jul 2017 13:08:56
td.run()
# Thu, 20 Jul 2017 13:09:07
dt.run()
# Thu, 20 Jul 2017 13:30:53
dt.plot_both(gain2=2500)
# Thu, 20 Jul 2017 13:43:47
dt.squidarray
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe311208>
# Thu, 20 Jul 2017 13:43:58
pa
#[Out]# <Nowack_Lab.Instruments.preamp.SR5113 at 0xc36e550>
# Thu, 20 Jul 2017 13:44:07
pa2 = SR5113(port="COM2")
# Thu, 20 Jul 2017 13:44:44
pa.gain()
# Thu, 20 Jul 2017 13:44:47
pa.gain
#[Out]# 25000
# Thu, 20 Jul 2017 13:45:23
dt = daqtransport.DAQ_Transport(instruments, 100e-6, -100e-6, 3e3, 1, 300)
# Thu, 20 Jul 2017 13:45:27
dt.run()
# Thu, 20 Jul 2017 14:12:12
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 14:13:59
dt = daqtransport.DAQ_Transport(instruments, -10e-6, -10e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 14:14:01
dt.run()
# Thu, 20 Jul 2017 14:17:35
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 14:18:06
dt = daqtransport.DAQ_Transport(instruments, -10e-6, 10e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 14:18:09
dt.run()
# Thu, 20 Jul 2017 14:22:34
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 14:24:10
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.001,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = 0.001,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = 0.000}
# Thu, 20 Jul 2017 14:24:18
daq.outputs['bias']
#[Out]# OutputChannel; name: ao3; label: bias; V = -0.000
# Thu, 20 Jul 2017 14:24:21
daq.outputs['bias'].V
#[Out]# 0.00037897843222494017
# Thu, 20 Jul 2017 14:26:34
reload(daqtransport)
#[Out]# <module 'Nowack_Lab.Procedures.daqtransport' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\daqtransport.py'>
# Thu, 20 Jul 2017 14:26:42
dt = daqtransport.DAQ_Transport(instruments, -10e-6, 10e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 14:26:44
dt.run()
# Thu, 20 Jul 2017 14:47:33
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 14:48:11
daqtransport.DAQ_Transport._daq_inputs = ['voltage', 'voltage2']
# Thu, 20 Jul 2017 14:49:48
dt = daqtransport.DAQ_Transport(instruments, -500e-6, 500e-6, 3e3, 1, 200)
# Thu, 20 Jul 2017 14:49:55
dt.run()
# Thu, 20 Jul 2017 14:56:55
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 14:57:25
plt.style.available
#[Out]# ['seaborn-dark-palette',
#[Out]#  'seaborn-deep',
#[Out]#  'seaborn-ticks',
#[Out]#  'seaborn-whitegrid',
#[Out]#  'ggplot',
#[Out]#  'seaborn-dark',
#[Out]#  'seaborn-colorblind',
#[Out]#  'seaborn-pastel',
#[Out]#  'seaborn-poster',
#[Out]#  'grayscale',
#[Out]#  'seaborn-muted',
#[Out]#  'seaborn-darkgrid',
#[Out]#  '_classic_test',
#[Out]#  'bmh',
#[Out]#  'seaborn-paper',
#[Out]#  'classic',
#[Out]#  'seaborn-notebook',
#[Out]#  'dark_background',
#[Out]#  'seaborn-bright',
#[Out]#  'seaborn',
#[Out]#  'seaborn-talk',
#[Out]#  'fivethirtyeight',
#[Out]#  'seaborn-white']
# Thu, 20 Jul 2017 14:57:34
plt.style.reload_library()
# Thu, 20 Jul 2017 14:57:36
plt.style.available
#[Out]# ['seaborn-dark-palette',
#[Out]#  'seaborn-deep',
#[Out]#  'seaborn-ticks',
#[Out]#  'seaborn-whitegrid',
#[Out]#  'ggplot',
#[Out]#  'seaborn-dark',
#[Out]#  'seaborn-colorblind',
#[Out]#  'seaborn-pastel',
#[Out]#  'seaborn-poster',
#[Out]#  'grayscale',
#[Out]#  'seaborn-muted',
#[Out]#  'seaborn-darkgrid',
#[Out]#  '_classic_test',
#[Out]#  'bmh',
#[Out]#  'seaborn-paper',
#[Out]#  'classic',
#[Out]#  'seaborn-notebook',
#[Out]#  'dark_background',
#[Out]#  'seaborn-bright',
#[Out]#  'seaborn',
#[Out]#  'seaborn-talk',
#[Out]#  'fivethirtyeight',
#[Out]#  'seaborn-white']
# Thu, 20 Jul 2017 14:58:19
plt.style.reload_library()
# Thu, 20 Jul 2017 14:58:20
plt.style.available
#[Out]# ['seaborn-dark-palette',
#[Out]#  'seaborn-deep',
#[Out]#  'seaborn-ticks',
#[Out]#  'seaborn-whitegrid',
#[Out]#  'ggplot',
#[Out]#  'seaborn-dark',
#[Out]#  'seaborn-colorblind',
#[Out]#  'seaborn-pastel',
#[Out]#  'seaborn-poster',
#[Out]#  'grayscale',
#[Out]#  'seaborn-muted',
#[Out]#  'seaborn-darkgrid',
#[Out]#  '_classic_test',
#[Out]#  'bmh',
#[Out]#  'seaborn-paper',
#[Out]#  'classic',
#[Out]#  'seaborn-notebook',
#[Out]#  'dark_background',
#[Out]#  'seaborn-bright',
#[Out]#  'seaborn',
#[Out]#  'seaborn-talk',
#[Out]#  'fivethirtyeight',
#[Out]#  'seaborn-white']
# Thu, 20 Jul 2017 14:59:07
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 15:00:04
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 15:00:06
dt.run()
# Thu, 20 Jul 2017 15:13:53
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 15:16:29
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.001,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.001}
# Thu, 20 Jul 2017 15:20:08
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 15:20:12
dt.run()
# Thu, 20 Jul 2017 15:37:48
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 15:43:03
_ = daq.sweep({'bias': 0}, {'bias': 0.5})
# Thu, 20 Jul 2017 15:43:21
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 15:43:25
dt.run()
# Thu, 20 Jul 2017 15:57:03
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 15:57:56
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 15:58:27
ax.plot(dt.received1['voltage2'], "k.")
#[Out]# [<matplotlib.lines.Line2D at 0x4d942a90>]
# Thu, 20 Jul 2017 16:00:30
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 16:00:33
dt.run()
# Thu, 20 Jul 2017 16:15:33
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 16:21:23
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 16:21:25
dt.run()
# Thu, 20 Jul 2017 16:35:11
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 16:43:52
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 400)
# Thu, 20 Jul 2017 16:43:58
dt.run()
# Thu, 20 Jul 2017 16:57:40
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.002,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = -0.002,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = -0.000,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = -0.000,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = -0.003,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.003,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = -0.001,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.161,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.153,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.065,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.167,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.195,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.185,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.210,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.164,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = -0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = -0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = -0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = 0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = 0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.214,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.004,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.001,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = -0.009,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = 0.139,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = -0.021,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = 0.169,
#[Out]#  'voltage2': InputChannel; name: ai3; label: voltage2; V = 0.023}
# Thu, 20 Jul 2017 16:58:11
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:00:24
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 17:00:27
dt.run()
# Thu, 20 Jul 2017 17:04:16
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:05:34
DAQ_Transport._daq_inputs
#[Out]# ['voltage']
# Thu, 20 Jul 2017 17:05:58
DAQ_Transport._daq_inputs = ['voltage', 'voltage2']
# Thu, 20 Jul 2017 17:06:05
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 1, 100)
# Thu, 20 Jul 2017 17:06:10
dt._daq_inputs
#[Out]# ['voltage', 'voltage2']
# Thu, 20 Jul 2017 17:06:58
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 9, 100)
# Thu, 20 Jul 2017 17:07:21
dt.run()
# Thu, 20 Jul 2017 17:08:08
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:08:25
DAQ_Transport._daq_inputs
#[Out]# ['voltage', 'voltage2']
# Thu, 20 Jul 2017 17:08:53
dt._daq_inputs
#[Out]# ['voltage', 'voltage2']
# Thu, 20 Jul 2017 17:10:18
d, r - daq.sweep({'bias':0}, {'bias':1}, chan_in = ['voltage', 'voltage2'], sample_rate=9, numsteps=100)
# Thu, 20 Jul 2017 17:10:27
d, r = daq.sweep({'bias':0}, {'bias':1}, chan_in = ['voltage', 'voltage2'], sample_rate=9, numsteps=100)
# Thu, 20 Jul 2017 17:10:42
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 1.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.000}
# Thu, 20 Jul 2017 17:11:01
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 17:11:24
ax.plot(r['voltage'])
#[Out]# [<matplotlib.lines.Line2D at 0x4cdc4a90>]
# Thu, 20 Jul 2017 17:11:32
ax.plot(r['voltage2'])
#[Out]# [<matplotlib.lines.Line2D at 0x4f80df60>]
# Thu, 20 Jul 2017 17:12:58
d, r = daq.sweep({'bias':1}, {'bias':0}, chan_in = ['voltage', 'voltage2'], sample_rate=9, numsteps=100)
# Thu, 20 Jul 2017 17:13:13
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 17:13:20
ax.plot(r['voltage']
)
#[Out]# [<matplotlib.lines.Line2D at 0x4f1786d8>]
# Thu, 20 Jul 2017 17:13:26
ax.plot(r['voltage2'])
#[Out]# [<matplotlib.lines.Line2D at 0x4f175630>]
# Thu, 20 Jul 2017 17:13:50
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = 0.000}
# Thu, 20 Jul 2017 17:17:52
DAQ_Transport._daq_inputs
#[Out]# ['voltage', 'voltage2']
# Thu, 20 Jul 2017 17:18:03
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 9, 100)
# Thu, 20 Jul 2017 17:18:05
dt.run()
# Thu, 20 Jul 2017 17:18:36
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:19:58
dt.received2
#[Out]# {'t': array([  0.        ,   0.11111111,   0.22222222,   0.33333333,
#[Out]#           0.44444444,   0.55555556,   0.66666667,   0.77777778,
#[Out]#           0.88888889,   1.        ,   1.11111111,   1.22222222,
#[Out]#           1.33333333,   1.44444444,   1.55555556,   1.66666667,
#[Out]#           1.77777778,   1.88888889,   2.        ,   2.11111111,
#[Out]#           2.22222222,   2.33333333,   2.44444444,   2.55555556,
#[Out]#           2.66666667,   2.77777778,   2.88888889,   3.        ,
#[Out]#           3.11111111,   3.22222222,   3.33333333,   3.44444444,
#[Out]#           3.55555556,   3.66666667,   3.77777778,   3.88888889,
#[Out]#           4.        ,   4.11111111,   4.22222222,   4.33333333,
#[Out]#           4.44444444,   4.55555556,   4.66666667,   4.77777778,
#[Out]#           4.88888889,   5.        ,   5.11111111,   5.22222222,
#[Out]#           5.33333333,   5.44444444,   5.55555556,   5.66666667,
#[Out]#           5.77777778,   5.88888889,   6.        ,   6.11111111,
#[Out]#           6.22222222,   6.33333333,   6.44444444,   6.55555556,
#[Out]#           6.66666667,   6.77777778,   6.88888889,   7.        ,
#[Out]#           7.11111111,   7.22222222,   7.33333333,   7.44444444,
#[Out]#           7.55555556,   7.66666667,   7.77777778,   7.88888889,
#[Out]#           8.        ,   8.11111111,   8.22222222,   8.33333333,
#[Out]#           8.44444444,   8.55555556,   8.66666667,   8.77777778,
#[Out]#           8.88888889,   9.        ,   9.11111111,   9.22222222,
#[Out]#           9.33333333,   9.44444444,   9.55555556,   9.66666667,
#[Out]#           9.77777778,   9.88888889,  10.        ,  10.11111111,
#[Out]#          10.22222222,  10.33333333,  10.44444444,  10.55555556,
#[Out]#          10.66666667,  10.77777778,  10.88888889,  11.        ]),
#[Out]#  'voltage': array([-1.10280968, -1.10184338, -1.0677009 , -1.04644237, -1.02969323,
#[Out]#         -0.99812754, -0.97332593, -0.97719111, -0.93596246, -0.90536306,
#[Out]#         -0.89956528, -0.88056145, -0.85028416, -0.84190959, -0.81324279,
#[Out]#         -0.77587932, -0.78811908, -0.74560203, -0.72144461, -0.725954  ,
#[Out]#         -0.69503251, -0.6670099 , -0.667332  , -0.6393094 , -0.60871001,
#[Out]#         -0.60130174, -0.58068741, -0.55298691, -0.54622283, -0.51143615,
#[Out]#         -0.48212516, -0.48115886, -0.45506885, -0.42414736, -0.43831971,
#[Out]#         -0.39612476, -0.36778006, -0.36101598, -0.35103092, -0.31237905,
#[Out]#         -0.30658127, -0.30046139, -0.26535262, -0.25504545, -0.23314273,
#[Out]#         -0.20608642, -0.20318753, -0.18611629, -0.16067048, -0.15616109,
#[Out]#         -0.1258838 , -0.09753909, -0.093996  , -0.07595847, -0.04664746,
#[Out]#         -0.05405574, -0.02410054,  0.00198947, -0.00316411,  0.03065628,
#[Out]#          0.05771259,  0.06383247,  0.08283631,  0.11858929,  0.12664176,
#[Out]#          0.14918869,  0.17141352,  0.17978809,  0.18977316,  0.22939133,
#[Out]#          0.24581838,  0.25419295,  0.29542163,  0.29252273,  0.31893485,
#[Out]#          0.35694254,  0.35565414,  0.38045576,  0.39945961,  0.40493529,
#[Out]#          0.43746729,  0.47289819,  0.48288326,  0.49383463,  0.53570751,
#[Out]#          0.54408208,  0.5733931 ,  0.60173782,  0.61301129,  0.63330353,
#[Out]#          0.66809024,  0.67034493,  0.68870458,  0.72477969,  0.72671228,
#[Out]#          0.75376861,  0.79048792,  0.7962857 ,  0.82140944,  0.85587405]),
#[Out]#  'voltage2': array([-0.02055745, -0.02957622, -0.02925412, -0.02152375, -0.03183091,
#[Out]#         -0.01540387, -0.03054252, -0.02764363, -0.01991325, -0.02023535,
#[Out]#         -0.02410054, -0.02313424, -0.02410054, -0.02538894, -0.02506684,
#[Out]#         -0.02216795, -0.03118672, -0.01637017, -0.02506684, -0.02152375,
#[Out]#         -0.01540387, -0.03022042, -0.02345634, -0.02506684, -0.02184585,
#[Out]#         -0.02216795, -0.02442264, -0.02313424, -0.02249005, -0.01830276,
#[Out]#         -0.01894696, -0.01572597, -0.02345634, -0.02764363, -0.02216795,
#[Out]#         -0.02667733, -0.01733646, -0.02603313, -0.02764363, -0.03086462,
#[Out]#         -0.02184585, -0.02120165, -0.03440771, -0.02571103, -0.03247511,
#[Out]#         -0.03022042, -0.02249005, -0.02699943, -0.02442264, -0.02828783,
#[Out]#         -0.03215301, -0.02828783, -0.02925412, -0.03086462, -0.03795079,
#[Out]#         -0.02764363, -0.02828783, -0.02732153, -0.02281214, -0.02732153,
#[Out]#         -0.02925412, -0.02699943, -0.03279721, -0.03311931, -0.02925412,
#[Out]#         -0.03022042, -0.02313424, -0.03827289, -0.0360182 , -0.0369845 ,
#[Out]#         -0.02828783, -0.03376351, -0.03859499, -0.04117178, -0.0366624 ,
#[Out]#         -0.0366624 , -0.03344141, -0.03344141, -0.04213808, -0.03956129,
#[Out]#         -0.02699943, -0.04407067, -0.04181598, -0.03827289, -0.04407067,
#[Out]#         -0.05276734, -0.04181598, -0.05180105, -0.05244524, -0.04890216,
#[Out]#         -0.03956129, -0.04246018, -0.04600327, -0.04117178, -0.04632537,
#[Out]#         -0.04600327, -0.04568117, -0.05244524, -0.04439277, -0.04600327])}
# Thu, 20 Jul 2017 17:20:09
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = -0.004,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = -0.001,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.000,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = -0.002,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = 0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = 0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.147,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.137,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.024,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.147,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.186,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.176,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.205,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.160,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = 0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = -0.001,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.217,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.002,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = -0.001,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = 0.057,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.036,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 0.007,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = -0.219,
#[Out]#  'voltage2': InputChannel; name: ai3; label: voltage2; V = 0.047}
# Thu, 20 Jul 2017 17:20:23
dt = daqtransport.DAQ_Transport(instruments, -700e-6, 700e-6, 3e3, 9, 100)
# Thu, 20 Jul 2017 17:20:25
dt.run()
# Thu, 20 Jul 2017 17:20:58
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:24:46
dt = daqtransport.DAQ_Transport(instruments, -900e-6, 900e-6, 3e3, 9, 200)
# Thu, 20 Jul 2017 17:24:48
dt.run()
# Thu, 20 Jul 2017 17:25:49
dt.plot_both(\gain2=25000)
# Thu, 20 Jul 2017 17:25:53
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:27:28
dt = daqtransport.DAQ_Transport(instruments, -1e-3, 1e-3, 3e3, 27, 300)
# Thu, 20 Jul 2017 17:27:32
dt.run()
# Thu, 20 Jul 2017 17:28:04
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:31:14
dt = daqtransport.DAQ_Transport(instruments, -1.5e-3, 1.5e-3, 3e3, 27, 400)
# Thu, 20 Jul 2017 17:31:24
dt.run()
# Thu, 20 Jul 2017 17:32:06
dt.plot_both(gain2=25000)
# Thu, 20 Jul 2017 17:41:04
from Nowack_Lab.Instruments.keithley import Keithley2400
# Thu, 20 Jul 2017 17:41:18
k = Keithley2400(gpib_address=24)
# Thu, 20 Jul 2017 17:41:22
k.I
# Thu, 20 Jul 2017 17:41:32
k.enable
# Thu, 20 Jul 2017 17:41:41
k.I
# Thu, 20 Jul 2017 17:41:48
k.source
#[Out]# 'I'
# Thu, 20 Jul 2017 17:41:56
k.output
#[Out]# 'off'
# Thu, 20 Jul 2017 17:41:58
k.output = "On"
# Thu, 20 Jul 2017 17:42:02
k.output = "on"
# Thu, 20 Jul 2017 17:42:05
k.I
#[Out]# 9.1748e-09
# Thu, 20 Jul 2017 17:42:14
k.Iout
#[Out]# 0.0
# Thu, 20 Jul 2017 17:54:14
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.002,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = -0.003,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.001,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = -0.002,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = -0.003,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = -0.001,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.161,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.152,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.029,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.158,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.192,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.183,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.210,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.166,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = -0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = -0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = 0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = -0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = -0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = 0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.225,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.002,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = 0.000,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = -0.004,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.045,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = 0.019,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = -0.187,
#[Out]#  'voltage2': InputChannel; name: ai3; label: voltage2; V = 0.063}
# Thu, 20 Jul 2017 17:54:25
daq['ai10']
# Thu, 20 Jul 2017 17:54:31
daq.inputs
#[Out]# {'acx': InputChannel; name: ai4; label: acx; V = -0.003,
#[Out]#  'acy': InputChannel; name: ai5; label: acy; V = -0.001,
#[Out]#  'ai10': InputChannel; name: ai10; label: ai10; V = 0.000,
#[Out]#  'ai11': InputChannel; name: ai11; label: ai11; V = 0.002,
#[Out]#  'ai12': InputChannel; name: ai12; label: ai12; V = 0.002,
#[Out]#  'ai13': InputChannel; name: ai13; label: ai13; V = -0.002,
#[Out]#  'ai14': InputChannel; name: ai14; label: ai14; V = -0.000,
#[Out]#  'ai15': InputChannel; name: ai15; label: ai15; V = 0.000,
#[Out]#  'ai16': InputChannel; name: ai16; label: ai16; V = -0.155,
#[Out]#  'ai17': InputChannel; name: ai17; label: ai17; V = -0.148,
#[Out]#  'ai18': InputChannel; name: ai18; label: ai18; V = -0.170,
#[Out]#  'ai19': InputChannel; name: ai19; label: ai19; V = -0.194,
#[Out]#  'ai20': InputChannel; name: ai20; label: ai20; V = -0.201,
#[Out]#  'ai21': InputChannel; name: ai21; label: ai21; V = -0.186,
#[Out]#  'ai22': InputChannel; name: ai22; label: ai22; V = -0.215,
#[Out]#  'ai23': InputChannel; name: ai23; label: ai23; V = -0.170,
#[Out]#  'ai24': InputChannel; name: ai24; label: ai24; V = 0.000,
#[Out]#  'ai25': InputChannel; name: ai25; label: ai25; V = 0.000,
#[Out]#  'ai26': InputChannel; name: ai26; label: ai26; V = 0.000,
#[Out]#  'ai27': InputChannel; name: ai27; label: ai27; V = 0.000,
#[Out]#  'ai28': InputChannel; name: ai28; label: ai28; V = 0.000,
#[Out]#  'ai29': InputChannel; name: ai29; label: ai29; V = 0.000,
#[Out]#  'ai30': InputChannel; name: ai30; label: ai30; V = 0.000,
#[Out]#  'ai31': InputChannel; name: ai31; label: ai31; V = -0.000,
#[Out]#  'ai7': InputChannel; name: ai7; label: ai7; V = -0.229,
#[Out]#  'ai8': InputChannel; name: ai8; label: ai8; V = -0.000,
#[Out]#  'ai9': InputChannel; name: ai9; label: ai9; V = -0.002,
#[Out]#  'cap': InputChannel; name: ai0; label: cap; V = 0.021,
#[Out]#  'dc': InputChannel; name: ai6; label: dc; V = -0.060,
#[Out]#  'theta': InputChannel; name: ai1; label: theta; V = -0.013,
#[Out]#  'voltage': InputChannel; name: ai2; label: voltage; V = -0.202,
#[Out]#  'voltage2': InputChannel; name: ai3; label: voltage2; V = 0.078}
# Thu, 20 Jul 2017 17:54:53
daq.inputs['ai10'].V
#[Out]# -0.004774604363692005
# Thu, 20 Jul 2017 18:01:25
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = -0.001,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.000,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = 0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = -0.001}
# Thu, 20 Jul 2017 18:03:15
s
#[Out]# <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe311208>
# Thu, 20 Jul 2017 18:03:18
s.reset()
# Thu, 20 Jul 2017 18:03:33
plane
# Thu, 20 Jul 2017 18:03:35
pf
#[Out]# <Nowack_Lab.Procedures.planefit.Planefit at 0x10116d30>
# Thu, 20 Jul 2017 18:03:55
scan = Scanplane(instruments, pf, span=[100,100], center = [-220, 50],  numpts=[500, 500], scanheight=10, scan_rate=100)
# Thu, 20 Jul 2017 18:05:51
scan.run()
# Thu, 20 Jul 2017 18:13:33
scan = Scanplane(instruments, pf, span=[100,100], center = [-220, 50],  numpts=[500, 50], scanheight=10, scan_rate=100)
# Thu, 20 Jul 2017 18:13:37
scan.run()
# Thu, 20 Jul 2017 18:18:26
s.sensitivity
#[Out]# 'High'
# Thu, 20 Jul 2017 18:18:39
s.sensitivity = "Med"
# Thu, 20 Jul 2017 18:18:43
s.reset()
# Thu, 20 Jul 2017 18:18:52
s.__dict__
#[Out]# {'_A_bias': 50,
#[Out]#  '_A_flux': 10,
#[Out]#  '_S_bias': 980,
#[Out]#  '_S_flux': 100,
#[Out]#  '_arrayLocked': False,
#[Out]#  '_feedbackResistor': '10kOhm',
#[Out]#  '_integratorCapacitor': '15nF',
#[Out]#  '_offset': 0.31,
#[Out]#  '_save_dict': {'Array bias': 50,
#[Out]#   'Array flux': 10,
#[Out]#   'Array locked': False,
#[Out]#   'Feedback resistor': '10kOhm',
#[Out]#   'Integrator capacitor': '15nF',
#[Out]#   'Preamp voltage offset': 0.31,
#[Out]#   'SQUID bias': 980,
#[Out]#   'SQUID flux': 100,
#[Out]#   'SQUID locked': True,
#[Out]#   'Test input': 'S_flux',
#[Out]#   'Test signal': 'Off',
#[Out]#   'channel': 1,
#[Out]#   'resetIntegrator': False,
#[Out]#   'sensitivity': 'Med'},
#[Out]#  '_sensitivity': 'Med',
#[Out]#  '_squidLocked': True,
#[Out]#  '_testInput': 'S_flux',
#[Out]#  '_testSignal': 'Off',
#[Out]#  'channel': 1,
#[Out]#  'pci': <Nowack_Lab.Instruments.squidarray.PCI100 at 0xe311048>,
#[Out]#  'resetIntegrator': False}
# Thu, 20 Jul 2017 18:20:06
scan = Scanplane(instruments, pf, span=[50,20], center = [-230, 50],  numpts=[100, 20], scanheight=10, scan_rate=100)
# Thu, 20 Jul 2017 18:20:09
scan.run()
# Thu, 20 Jul 2017 18:23:45
from Nowack_Lab.Procedures import scanspectra as ss
# Thu, 20 Jul 2017 18:24:33
from Nowack_Lab.Procedures import scanspectra as ss
# Thu, 20 Jul 2017 18:26:22
spec = ss.Scanspectra(instruments, plane, span=[50, 50], center = [-230, 50], scanheight=10, monitor_time = 30, sample_rate=900)
# Thu, 20 Jul 2017 18:26:31
spec = ss.Scanspectra(instruments, pf, span=[50, 50], center = [-230, 50], scanheight=10, monitor_time = 30, sample_rate=900)
# Thu, 20 Jul 2017 18:26:51
spec.run()
# Thu, 20 Jul 2017 18:28:12
spec = ss.Scanspectra(instruments, pf, span=[50, 50], center = [-230, 50], numpts=[2,2], scanheight=10, monitor_time = 30, sample_rate=900)
# Thu, 20 Jul 2017 18:28:14
spec.run()
# Thu, 20 Jul 2017 18:30:38
fig, ax = plt.subplots()
# Thu, 20 Jul 2017 18:30:57
spec.t
#[Out]# array([  0.00000000e+00,   1.11111111e-03,   2.22222222e-03, ...,
#[Out]#          2.99966667e+01,   2.99977778e+01,   2.99988889e+01])
# Thu, 20 Jul 2017 18:30:59
spec.f
#[Out]# array([  0.00000000e+00,   3.33333333e-02,   6.66666667e-02, ...,
#[Out]#          4.49933333e+02,   4.49966667e+02,   4.50000000e+02])
# Thu, 20 Jul 2017 18:31:07
spec.psd[0,0]
#[Out]# array([  2.19462847e-06,   1.29891916e-05,   1.32038853e-05, ...,
#[Out]#          1.81280529e-05,   4.02175829e-05,   3.69702344e-05])
# Thu, 20 Jul 2017 18:31:32
for s in spec.psd.flatten():
    ax.plot(spec.f, s)
    
# Thu, 20 Jul 2017 18:31:59
spec.psd.flatten.shape
# Thu, 20 Jul 2017 18:32:04
spec.psd.flatten().shape
#[Out]# (54004,)
# Thu, 20 Jul 2017 18:32:11
spec.psd.shape
#[Out]# (2, 2, 13501)
# Thu, 20 Jul 2017 18:32:47
for row in spec.psd:
    for s in row:
        ax.plot(spec.f, s)
        
# Thu, 20 Jul 2017 18:38:09
spec = ss.Scanspectra(instruments, pf, span=[10, 10], center = [-228, 50], numpts=[30,30], scanheight=10, monitor_time = 30, sample_rate=900)
# Thu, 20 Jul 2017 18:38:11
spec.run()
# Fri, 21 Jul 2017 08:40:05
fig, ax = plt.subplots()
# Fri, 21 Jul 2017 08:40:23
ax.imshow(spec.Vavg)
# Fri, 21 Jul 2017 08:40:36
spec.Vavg
#[Out]# {'acx': array([[-0.00219781, -0.00251991, -0.00219781, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00219781, -0.00251991, -0.00251991,
#[Out]#          -0.00284201, -0.00316411, -0.00316411, -0.00316411, -0.00251991,
#[Out]#          -0.00251991, -0.00316411, -0.00251991, -0.00284201, -0.00219781,
#[Out]#          -0.00284201, -0.00284201, -0.00251991, -0.00251991, -0.00284201,
#[Out]#          -0.00219781, -0.00219781, -0.00284201, -0.00284201, -0.00251991],
#[Out]#         [-0.00316411, -0.00219781, -0.00284201, -0.00187571, -0.00219781,
#[Out]#          -0.00251991, -0.00348621, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00284201, -0.00284201, -0.00251991, -0.00219781, -0.00284201,
#[Out]#          -0.00251991, -0.00219781, -0.00251991, -0.00284201, -0.00219781,
#[Out]#          -0.00251991, -0.00316411, -0.00316411, -0.00251991, -0.00316411,
#[Out]#          -0.00284201, -0.00251991, -0.00251991, -0.00284201, -0.00284201],
#[Out]#         [-0.00251991, -0.00251991, -0.00251991, -0.00219781, -0.00284201,
#[Out]#          -0.00284201, -0.00284201, -0.00187571, -0.00316411, -0.00251991,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00219781, -0.00316411,
#[Out]#          -0.00219781, -0.00316411, -0.00251991, -0.00251991, -0.00251991,
#[Out]#          -0.00251991, -0.00251991, -0.00348621, -0.00219781, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00316411, -0.00251991, -0.00219781],
#[Out]#         [-0.00251991, -0.00284201, -0.00219781, -0.00284201, -0.00316411,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00251991, -0.00219781,
#[Out]#          -0.00316411, -0.00316411, -0.00348621, -0.00219781, -0.00219781,
#[Out]#          -0.00187571, -0.00219781, -0.00251991, -0.00219781, -0.00187571,
#[Out]#          -0.00251991, -0.00284201, -0.00219781, -0.00251991, -0.00219781,
#[Out]#          -0.00219781, -0.00251991, -0.00284201, -0.00284201, -0.00251991],
#[Out]#         [-0.00284201, -0.00251991, -0.00251991, -0.00187571, -0.00219781,
#[Out]#          -0.00187571, -0.00316411, -0.00219781, -0.00251991, -0.00284201,
#[Out]#          -0.00316411, -0.00219781, -0.00348621, -0.00251991, -0.00284201,
#[Out]#          -0.00348621, -0.00316411, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00316411, -0.00251991, -0.00284201, -0.00219781, -0.00284201,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00316411, -0.00348621],
#[Out]#         [-0.00251991, -0.00251991, -0.00316411, -0.00187571, -0.00219781,
#[Out]#          -0.00187571, -0.00219781, -0.00219781, -0.00251991, -0.00219781,
#[Out]#          -0.00187571, -0.00123152, -0.00251991, -0.00251991, -0.00219781,
#[Out]#          -0.00251991, -0.00316411, -0.00284201, -0.00284201, -0.00284201,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00316411, -0.00380831,
#[Out]#          -0.00284201, -0.00187571, -0.00251991, -0.00219781, -0.00284201],
#[Out]#         [-0.00284201, -0.00251991, -0.00251991, -0.00316411, -0.00316411,
#[Out]#          -0.00316411, -0.00284201, -0.00251991, -0.00251991, -0.00251991,
#[Out]#          -0.00284201, -0.00284201, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00187571, -0.00284201, -0.00251991, -0.00316411,
#[Out]#          -0.00219781, -0.00251991, -0.00284201, -0.00316411, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00219781, -0.00251991, -0.00251991],
#[Out]#         [-0.00284201, -0.00251991, -0.00284201, -0.00251991, -0.00284201,
#[Out]#          -0.00284201, -0.00284201, -0.00284201, -0.00155362, -0.00284201,
#[Out]#          -0.00187571, -0.00284201, -0.00251991, -0.00251991, -0.00284201,
#[Out]#          -0.00284201, -0.00219781, -0.00251991, -0.00219781, -0.00316411,
#[Out]#          -0.00219781, -0.00219781, -0.00219781, -0.00316411, -0.00219781,
#[Out]#          -0.00219781, -0.00316411, -0.00316411, -0.00284201, -0.00251991],
#[Out]#         [-0.00284201, -0.00187571, -0.00251991, -0.00316411, -0.00251991,
#[Out]#          -0.00251991, -0.00187571, -0.00251991, -0.00187571, -0.00251991,
#[Out]#          -0.00251991, -0.00251991, -0.00284201, -0.00316411, -0.00284201,
#[Out]#          -0.00316411, -0.00284201, -0.00219781, -0.00187571, -0.00251991,
#[Out]#          -0.00284201, -0.00155362, -0.00316411, -0.00251991, -0.00251991,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00316411, -0.00284201],
#[Out]#         [-0.00251991, -0.00219781, -0.00219781, -0.00219781, -0.00316411,
#[Out]#          -0.00219781, -0.00284201, -0.00251991, -0.00284201, -0.00284201,
#[Out]#          -0.00219781, -0.00219781, -0.00219781, -0.00219781, -0.00284201,
#[Out]#          -0.00219781, -0.00187571, -0.00251991, -0.00251991, -0.00284201,
#[Out]#          -0.00251991, -0.00284201, -0.00348621, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00284201, -0.00219781, -0.00219781],
#[Out]#         [-0.00316411, -0.00251991, -0.00316411, -0.00284201, -0.00219781,
#[Out]#          -0.00251991, -0.00284201, -0.00251991, -0.00187571, -0.00348621,
#[Out]#          -0.00284201, -0.00187571, -0.00284201, -0.00284201, -0.00316411,
#[Out]#          -0.00187571, -0.00284201, -0.00284201, -0.00348621, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00251991, -0.00187571, -0.00348621,
#[Out]#          -0.00251991, -0.00284201, -0.00316411, -0.00316411, -0.00187571],
#[Out]#         [-0.00284201, -0.00284201, -0.00251991, -0.00187571, -0.00219781,
#[Out]#          -0.00251991, -0.00251991, -0.00187571, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00284201, -0.00219781, -0.00316411, -0.00284201,
#[Out]#          -0.00251991, -0.00187571, -0.00251991, -0.00219781, -0.00316411,
#[Out]#          -0.00187571, -0.00155362, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00155362, -0.00251991, -0.00251991, -0.00251991],
#[Out]#         [-0.00187571, -0.00284201, -0.00251991, -0.00348621, -0.00219781,
#[Out]#          -0.00251991, -0.00219781, -0.00316411, -0.00284201, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00251991, -0.00284201, -0.00251991,
#[Out]#          -0.00284201, -0.00251991, -0.00284201, -0.00316411, -0.00251991,
#[Out]#          -0.00219781, -0.00219781, -0.00251991, -0.00316411, -0.00187571,
#[Out]#          -0.00284201, -0.00316411, -0.00251991, -0.00219781, -0.00251991],
#[Out]#         [-0.00284201, -0.00284201, -0.00219781, -0.00316411, -0.00219781,
#[Out]#          -0.00251991, -0.00251991, -0.00219781, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00316411, -0.00284201, -0.00219781, -0.00284201,
#[Out]#          -0.00284201, -0.00187571, -0.00219781, -0.00316411, -0.00219781,
#[Out]#          -0.00316411, -0.00251991, -0.00284201, -0.00251991, -0.00316411,
#[Out]#          -0.00316411, -0.00251991, -0.00251991, -0.00316411, -0.00251991],
#[Out]#         [-0.00284201, -0.00251991, -0.00187571, -0.00251991, -0.00187571,
#[Out]#          -0.00284201, -0.00219781, -0.00219781, -0.00284201, -0.00251991,
#[Out]#          -0.00187571, -0.00251991, -0.00187571, -0.00316411, -0.00284201,
#[Out]#          -0.00219781, -0.00284201, -0.00316411, -0.00251991, -0.00316411,
#[Out]#          -0.00284201, -0.00251991, -0.00284201, -0.00187571, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00251991, -0.00219781, -0.00284201],
#[Out]#         [-0.00284201, -0.00284201, -0.00155362, -0.00284201, -0.00219781,
#[Out]#          -0.00251991, -0.00380831, -0.00251991, -0.00251991, -0.00284201,
#[Out]#          -0.00219781, -0.00219781, -0.00316411, -0.00316411, -0.00251991,
#[Out]#          -0.00251991, -0.00219781, -0.00284201, -0.00219781, -0.00316411,
#[Out]#          -0.00316411, -0.00251991, -0.00219781, -0.00251991, -0.00187571,
#[Out]#          -0.00251991, -0.00219781, -0.00219781, -0.00251991, -0.00251991],
#[Out]#         [-0.00219781, -0.00284201, -0.00219781, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00316411, -0.00251991, -0.00187571,
#[Out]#          -0.00251991, -0.00219781, -0.00316411, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00251991, -0.00316411, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00316411, -0.00187571, -0.00284201, -0.00316411,
#[Out]#          -0.00187571, -0.00251991, -0.00316411, -0.00316411, -0.00219781],
#[Out]#         [-0.00251991, -0.00219781, -0.00348621, -0.00219781, -0.00251991,
#[Out]#          -0.00251991, -0.00251991, -0.00219781, -0.00251991, -0.00251991,
#[Out]#          -0.00219781, -0.00348621, -0.00219781, -0.00251991, -0.00284201,
#[Out]#          -0.00219781, -0.00251991, -0.00251991, -0.00251991, -0.00251991,
#[Out]#          -0.00251991, -0.00348621, -0.00251991, -0.00284201, -0.00219781,
#[Out]#          -0.00316411, -0.00187571, -0.00187571, -0.00219781, -0.00187571],
#[Out]#         [-0.00251991, -0.00284201, -0.00284201, -0.00219781, -0.00251991,
#[Out]#          -0.00187571, -0.00251991, -0.00284201, -0.00251991, -0.00251991,
#[Out]#          -0.00284201, -0.00219781, -0.00187571, -0.00219781, -0.00284201,
#[Out]#          -0.00251991, -0.00251991, -0.00251991, -0.00251991, -0.00187571,
#[Out]#          -0.00251991, -0.00316411, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00187571, -0.00348621, -0.00219781, -0.00251991],
#[Out]#         [-0.00219781, -0.00251991, -0.00284201, -0.00219781, -0.00284201,
#[Out]#          -0.00251991, -0.00251991, -0.00348621, -0.00251991, -0.00219781,
#[Out]#          -0.00219781, -0.00284201, -0.00219781, -0.00219781, -0.00251991,
#[Out]#          -0.00251991, -0.00251991, -0.00251991, -0.00251991, -0.00251991,
#[Out]#          -0.00155362, -0.00155362, -0.00251991, -0.00187571, -0.00284201,
#[Out]#          -0.00251991, -0.00251991, -0.00348621, -0.00251991, -0.00219781],
#[Out]#         [-0.00284201, -0.00284201, -0.00316411, -0.00155362, -0.00219781,
#[Out]#          -0.00251991, -0.00284201, -0.00219781, -0.00219781, -0.00219781,
#[Out]#          -0.00251991, -0.00251991, -0.00251991, -0.00251991, -0.00219781,
#[Out]#          -0.00348621, -0.00187571, -0.00316411, -0.00251991, -0.00219781,
#[Out]#          -0.00187571, -0.00316411, -0.00219781, -0.00219781, -0.00284201,
#[Out]#          -0.00316411, -0.00251991, -0.00251991, -0.00251991, -0.00219781],
#[Out]#         [-0.00251991, -0.00251991, -0.00187571, -0.00251991, -0.00284201,
#[Out]#          -0.00251991, -0.00187571, -0.00219781, -0.00155362, -0.00251991,
#[Out]#          -0.00284201, -0.00316411, -0.00219781, -0.00316411, -0.00251991,
#[Out]#          -0.00348621, -0.00219781, -0.00251991, -0.00187571, -0.00284201,
#[Out]#          -0.00316411, -0.00284201, -0.00284201, -0.00284201, -0.00316411,
#[Out]#          -0.00219781, -0.00348621, -0.00316411, -0.00284201, -0.00219781],
#[Out]#         [-0.00219781, -0.00251991, -0.00348621, -0.00284201, -0.00219781,
#[Out]#          -0.00155362, -0.00219781, -0.00219781, -0.00187571, -0.00284201,
#[Out]#          -0.00251991, -0.00219781, -0.00284201, -0.00284201, -0.00219781,
#[Out]#          -0.00251991, -0.00251991, -0.00251991, -0.00284201, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00284201, -0.00219781, -0.00316411,
#[Out]#          -0.00155362, -0.00219781, -0.00251991, -0.00316411, -0.00316411],
#[Out]#         [-0.00284201, -0.00187571, -0.00284201, -0.00187571, -0.00316411,
#[Out]#          -0.00187571, -0.00219781, -0.00187571, -0.00251991, -0.00251991,
#[Out]#          -0.00251991, -0.00251991, -0.00219781, -0.00251991, -0.00316411,
#[Out]#          -0.00284201, -0.00284201, -0.00251991, -0.00316411, -0.00219781,
#[Out]#          -0.00219781, -0.00219781, -0.00219781, -0.00380831, -0.00187571,
#[Out]#          -0.00251991, -0.00251991, -0.00251991, -0.00219781, -0.00251991],
#[Out]#         [-0.00187571, -0.00219781, -0.00284201, -0.00251991, -0.00251991,
#[Out]#          -0.00316411, -0.00284201, -0.00284201, -0.00251991, -0.00251991,
#[Out]#          -0.00251991, -0.00284201, -0.00316411, -0.00251991, -0.00251991,
#[Out]#          -0.00316411, -0.00251991, -0.00284201, -0.00219781, -0.00219781,
#[Out]#          -0.00219781, -0.00284201, -0.00316411, -0.00316411, -0.00219781,
#[Out]#          -0.00251991, -0.00316411, -0.00316411, -0.00251991, -0.00284201],
#[Out]#         [-0.00251991, -0.00219781, -0.00251991, -0.00284201, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00284201, -0.00316411, -0.00284201,
#[Out]#          -0.00316411, -0.00219781, -0.00251991, -0.00219781, -0.00219781,
#[Out]#          -0.00284201, -0.00219781, -0.00251991, -0.00187571, -0.00251991,
#[Out]#          -0.00284201, -0.00219781, -0.00348621, -0.00219781, -0.00219781,
#[Out]#          -0.00284201, -0.00219781, -0.00284201, -0.00251991, -0.00219781],
#[Out]#         [-0.00251991, -0.00155362, -0.00187571, -0.00316411, -0.00284201,
#[Out]#          -0.00187571, -0.00251991, -0.00219781, -0.00251991, -0.00348621,
#[Out]#          -0.00284201, -0.00251991, -0.00219781, -0.00187571, -0.00219781,
#[Out]#          -0.00219781, -0.00251991, -0.00219781, -0.00251991, -0.00219781,
#[Out]#          -0.00284201, -0.00316411, -0.00316411, -0.00219781, -0.00316411,
#[Out]#          -0.00284201, -0.00219781, -0.00123152, -0.00251991, -0.00284201],
#[Out]#         [-0.00187571, -0.00316411, -0.00187571, -0.00316411, -0.00316411,
#[Out]#          -0.00251991, -0.00187571, -0.00251991, -0.00187571, -0.00251991,
#[Out]#          -0.00284201, -0.00251991, -0.00251991, -0.00251991, -0.00316411,
#[Out]#          -0.00219781, -0.00316411, -0.00251991, -0.00284201, -0.00251991,
#[Out]#          -0.00219781, -0.00251991, -0.00284201, -0.00316411, -0.00251991,
#[Out]#          -0.00284201, -0.00251991, -0.00284201, -0.00284201, -0.00284201],
#[Out]#         [-0.00219781, -0.00155362, -0.00284201, -0.00251991, -0.00219781,
#[Out]#          -0.00251991, -0.00284201, -0.00284201, -0.00251991, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00251991, -0.00251991, -0.00316411,
#[Out]#          -0.00251991, -0.00251991, -0.00219781, -0.00316411, -0.00316411,
#[Out]#          -0.00251991, -0.00219781, -0.00219781, -0.00219781, -0.00284201,
#[Out]#          -0.00348621, -0.00251991, -0.00251991, -0.00284201, -0.00187571],
#[Out]#         [-0.00219781, -0.00284201, -0.00251991, -0.00251991, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00284201, -0.00284201, -0.00251991,
#[Out]#          -0.00316411, -0.00219781, -0.00219781, -0.00251991, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00251991, -0.00251991, -0.00219781,
#[Out]#          -0.00284201, -0.00251991, -0.00380831, -0.00251991, -0.00251991,
#[Out]#          -0.00284201, -0.00251991, -0.00219781, -0.00316411, -0.00251991]]),
#[Out]#  'acy': array([[-0.00155362, -0.00155362, -0.00155362, -0.00219781, -0.00123152,
#[Out]#          -0.00155362, -0.00155362, -0.00187571, -0.00155362, -0.00058732,
#[Out]#          -0.00123152, -0.00187571, -0.00219781, -0.00123152, -0.00155362,
#[Out]#          -0.00155362, -0.00090942, -0.00123152, -0.00187571, -0.00219781,
#[Out]#          -0.00123152, -0.00058732, -0.00155362, -0.00219781, -0.00090942,
#[Out]#          -0.00123152, -0.00187571, -0.00155362, -0.00090942, -0.00090942],
#[Out]#         [-0.00123152, -0.00155362, -0.00058732, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00155362, -0.00187571, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00090942, -0.00187571, -0.00090942, -0.00123152,
#[Out]#          -0.00155362, -0.00155362, -0.00123152, -0.00090942, -0.00155362,
#[Out]#          -0.00155362, -0.00123152, -0.00219781, -0.00187571, -0.00090942,
#[Out]#          -0.00090942, -0.00123152, -0.00251991, -0.00155362, -0.00187571],
#[Out]#         [-0.00155362, -0.00090942, -0.00090942, -0.00219781, -0.00155362,
#[Out]#          -0.00187571, -0.00123152, -0.00058732, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00090942, -0.00187571, -0.00058732, -0.00123152,
#[Out]#          -0.00090942, -0.00155362, -0.00155362, -0.00123152, -0.00187571,
#[Out]#          -0.00155362, -0.00123152, -0.00155362, -0.00187571, -0.00251991,
#[Out]#          -0.00155362, -0.00219781, -0.00155362, -0.00123152, -0.00090942],
#[Out]#         [-0.00123152, -0.00219781, -0.00187571, -0.00155362, -0.00058732,
#[Out]#          -0.00123152, -0.00155362, -0.00155362, -0.00219781, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00187571, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00123152, -0.00187571, -0.00123152, -0.00090942,
#[Out]#          -0.00090942, -0.00219781, -0.00090942, -0.00123152, -0.00155362],
#[Out]#         [-0.00155362, -0.00090942, -0.00123152, -0.00123152, -0.00123152,
#[Out]#          -0.00155362, -0.00187571, -0.00123152, -0.00251991, -0.00187571,
#[Out]#          -0.00155362, -0.00155362, -0.00219781, -0.00123152, -0.00187571,
#[Out]#          -0.00187571, -0.00123152, -0.00090942, -0.00123152, -0.00187571,
#[Out]#          -0.00187571, -0.00123152, -0.00155362, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00058732, -0.00155362, -0.00155362, -0.00123152],
#[Out]#         [-0.00155362, -0.00187571, -0.00219781, -0.00090942, -0.00155362,
#[Out]#          -0.00090942, -0.00219781, -0.00187571, -0.00251991, -0.00187571,
#[Out]#          -0.00123152, -0.00187571, -0.00155362, -0.00155362, -0.00251991,
#[Out]#          -0.00123152, -0.00155362, -0.00187571, -0.00187571, -0.00187571,
#[Out]#          -0.00155362, -0.00123152, -0.00123152, -0.00187571, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00219781, -0.00251991, -0.00123152],
#[Out]#         [-0.00123152, -0.00187571, -0.00187571, -0.00155362, -0.00090942,
#[Out]#          -0.00123152, -0.00123152, -0.00187571, -0.00090942, -0.00058732,
#[Out]#          -0.00090942, -0.00155362, -0.00123152, -0.00155362, -0.00187571,
#[Out]#          -0.00187571, -0.00123152, -0.00123152, -0.00187571, -0.00123152,
#[Out]#          -0.00090942, -0.00187571, -0.00155362, -0.00187571, -0.00123152,
#[Out]#          -0.00284201, -0.00155362, -0.00219781, -0.00155362, -0.00123152],
#[Out]#         [-0.00090942, -0.00155362, -0.00155362, -0.00123152, -0.00123152,
#[Out]#          -0.00155362, -0.00187571, -0.00219781, -0.00123152, -0.00219781,
#[Out]#          -0.00123152, -0.00123152, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00123152, -0.00187571, -0.00123152, -0.00123152, -0.00155362,
#[Out]#          -0.00155362, -0.00123152, -0.00187571, -0.00090942, -0.00123152,
#[Out]#          -0.00187571, -0.00155362, -0.00155362, -0.00187571, -0.00123152],
#[Out]#         [-0.00155362, -0.00058732, -0.00123152, -0.00187571, -0.00187571,
#[Out]#          -0.00219781, -0.00123152, -0.00155362, -0.00155362, -0.00123152,
#[Out]#          -0.00155362, -0.00058732, -0.00155362, -0.00187571, -0.00187571,
#[Out]#          -0.00155362, -0.00090942, -0.00155362, -0.00123152, -0.00187571,
#[Out]#          -0.00090942, -0.00251991, -0.00187571, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00123152, -0.00155362, -0.00155362, -0.00187571],
#[Out]#         [-0.00187571, -0.00187571, -0.00155362, -0.00284201, -0.00219781,
#[Out]#          -0.00123152, -0.00155362, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00123152, -0.00155362, -0.00219781, -0.00219781,
#[Out]#          -0.00219781, -0.00187571, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00155362, -0.00123152, -0.00187571, -0.00155362, -0.00090942,
#[Out]#          -0.00155362, -0.00090942, -0.00123152, -0.00123152, -0.00123152],
#[Out]#         [-0.00187571, -0.00090942, -0.00123152, -0.00090942, -0.00219781,
#[Out]#          -0.00187571, -0.00219781, -0.00155362, -0.00123152, -0.00155362,
#[Out]#          -0.00090942, -0.00123152, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00219781, -0.00187571, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00155362, -0.00187571, -0.00123152, -0.00090942,
#[Out]#          -0.00058732, -0.00155362, -0.00187571, -0.00123152, -0.00187571],
#[Out]#         [-0.00187571, -0.00187571, -0.00155362, -0.00219781, -0.00155362,
#[Out]#          -0.00155362, -0.00155362, -0.00155362, -0.00155362, -0.00155362,
#[Out]#          -0.00187571, -0.00123152, -0.00123152, -0.00187571, -0.00219781,
#[Out]#          -0.00187571, -0.00123152, -0.00155362, -0.00155362, -0.00155362,
#[Out]#          -0.00090942, -0.00123152, -0.00187571, -0.00090942, -0.00187571,
#[Out]#          -0.00058732, -0.00187571, -0.00187571, -0.00187571, -0.00123152],
#[Out]#         [-0.00123152, -0.00187571, -0.00123152, -0.00155362, -0.00187571,
#[Out]#          -0.00187571, -0.00123152, -0.00123152, -0.00155362, -0.00187571,
#[Out]#          -0.00090942, -0.00155362, -0.00155362, -0.00155362, -0.00187571,
#[Out]#          -0.00026522, -0.00219781, -0.00155362, -0.00155362, -0.00187571,
#[Out]#          -0.00090942, -0.00187571, -0.00187571, -0.00187571, -0.00219781,
#[Out]#          -0.00155362, -0.00155362, -0.00187571, -0.00123152, -0.00090942],
#[Out]#         [-0.00219781, -0.00219781, -0.00155362, -0.00219781, -0.00187571,
#[Out]#          -0.00123152, -0.00155362, -0.00123152, -0.00155362, -0.00155362,
#[Out]#          -0.00187571, -0.00187571, -0.00219781, -0.00187571, -0.00123152,
#[Out]#          -0.00058732, -0.00058732, -0.00155362, -0.00123152, -0.00155362,
#[Out]#          -0.00187571, -0.00123152, -0.00123152, -0.00090942, -0.00090942,
#[Out]#          -0.00251991, -0.00187571, -0.00155362, -0.00187571, -0.00155362],
#[Out]#         [-0.00187571, -0.00090942, -0.00187571, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00187571, -0.00123152, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00123152, -0.00090942, -0.00155362, -0.00187571,
#[Out]#          -0.00090942, -0.00123152, -0.00219781, -0.00090942, -0.00251991,
#[Out]#          -0.00187571, -0.00187571, -0.00187571, -0.00123152, -0.00090942,
#[Out]#          -0.00090942, -0.00155362, -0.00090942, -0.00058732, -0.00155362],
#[Out]#         [-0.00123152, -0.00090942, -0.00155362, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00155362, -0.00187571, -0.00155362, -0.00090942,
#[Out]#          -0.00123152, -0.00187571, -0.00123152, -0.00123152, -0.00187571,
#[Out]#          -0.00219781, -0.00187571, -0.00155362, -0.00123152, -0.00187571,
#[Out]#          -0.00155362, -0.00187571, -0.00155362, -0.00155362, -0.00155362,
#[Out]#          -0.00123152, -0.00123152, -0.00090942, -0.00155362, -0.00123152],
#[Out]#         [-0.00155362, -0.00155362, -0.00058732, -0.00187571, -0.00058732,
#[Out]#          -0.00123152, -0.00155362, -0.00187571, -0.00155362, -0.00155362,
#[Out]#          -0.00187571, -0.00187571, -0.00123152, -0.00187571, -0.00123152,
#[Out]#          -0.00187571, -0.00219781, -0.00155362, -0.00219781, -0.00090942,
#[Out]#          -0.00155362, -0.00155362, -0.00187571, -0.00219781, -0.00251991,
#[Out]#          -0.00155362, -0.00155362, -0.00155362, -0.00090942, -0.00123152],
#[Out]#         [-0.00123152, -0.00058732, -0.00219781, -0.00123152, -0.00090942,
#[Out]#          -0.00090942, -0.00155362, -0.00090942, -0.00123152, -0.00090942,
#[Out]#          -0.00155362, -0.00219781, -0.00123152, -0.00155362, -0.00187571,
#[Out]#          -0.00155362, -0.00090942, -0.00155362, -0.00219781, -0.00155362,
#[Out]#          -0.00123152, -0.00187571, -0.00155362, -0.00090942, -0.00187571,
#[Out]#          -0.00219781, -0.00155362, -0.00155362, -0.00187571, -0.00155362],
#[Out]#         [-0.00155362, -0.00090942, -0.00187571, -0.00155362, -0.00123152,
#[Out]#          -0.00155362, -0.00187571, -0.00219781, -0.00123152, -0.00155362,
#[Out]#          -0.00123152, -0.00187571, -0.00155362, -0.00123152, -0.00187571,
#[Out]#          -0.00187571, -0.00219781, -0.00219781, -0.00155362, -0.00155362,
#[Out]#          -0.00187571, -0.00090942, -0.00187571, -0.00090942, -0.00187571,
#[Out]#          -0.00123152, -0.00123152, -0.00123152, -0.00155362, -0.00187571],
#[Out]#         [-0.00187571, -0.00155362, -0.00187571, -0.00187571, -0.00187571,
#[Out]#          -0.00187571, -0.00155362, -0.00123152, -0.00187571, -0.00123152,
#[Out]#          -0.00155362, -0.00123152, -0.00090942, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00219781, -0.00123152, -0.00155362, -0.00155362,
#[Out]#          -0.00123152, -0.00026522, -0.00155362, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00090942, -0.00123152, -0.00187571, -0.00219781],
#[Out]#         [-0.00123152, -0.00123152, -0.00155362, -0.00090942, -0.00187571,
#[Out]#          -0.00090942, -0.00187571, -0.00155362, -0.00187571, -0.00155362,
#[Out]#          -0.00058732, -0.00123152, -0.00155362, -0.00090942, -0.00155362,
#[Out]#          -0.00187571, -0.00090942, -0.00155362, -0.00058732, -0.00155362,
#[Out]#          -0.00123152, -0.00058732, -0.00155362, -0.00123152, -0.00219781,
#[Out]#          -0.00187571, -0.00155362, -0.00123152, -0.00155362, -0.00123152],
#[Out]#         [-0.00187571, -0.00219781, -0.00123152, -0.00090942, -0.00187571,
#[Out]#          -0.00123152, -0.00090942, -0.00123152, -0.00155362, -0.00155362,
#[Out]#          -0.00155362, -0.00155362, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00187571, -0.00155362, -0.00090942, -0.00187571, -0.00155362,
#[Out]#          -0.00155362, -0.00090942, -0.00155362, -0.00155362, -0.00219781,
#[Out]#          -0.00123152, -0.00123152, -0.00123152, -0.00123152, -0.00123152],
#[Out]#         [-0.00155362, -0.00219781, -0.00090942, -0.00251991, -0.00123152,
#[Out]#          -0.00187571, -0.00155362, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00155362, -0.00187571, -0.00058732, -0.00123152, -0.00155362,
#[Out]#          -0.00219781, -0.00090942, -0.00187571, -0.00090942, -0.00123152,
#[Out]#          -0.00251991, -0.00090942, -0.00155362, -0.00123152, -0.00219781,
#[Out]#          -0.00123152, -0.00187571, -0.00187571, -0.00123152, -0.00187571],
#[Out]#         [-0.00123152, -0.00155362, -0.00123152, -0.00251991, -0.00090942,
#[Out]#          -0.00155362, -0.00058732, -0.00187571, -0.00123152, -0.00219781,
#[Out]#          -0.00123152, -0.00123152, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00090942, -0.00123152, -0.00123152, -0.00219781, -0.00155362,
#[Out]#          -0.00187571, -0.00155362, -0.00123152, -0.00155362, -0.00187571,
#[Out]#          -0.00187571, -0.00155362, -0.00187571, -0.00090942, -0.00187571],
#[Out]#         [-0.00155362, -0.00155362, -0.00058732, -0.00090942, -0.00187571,
#[Out]#          -0.00187571, -0.00123152, -0.00058732, -0.00123152, -0.00187571,
#[Out]#          -0.00123152, -0.00219781, -0.00123152, -0.00123152, -0.00219781,
#[Out]#          -0.00090942, -0.00155362, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00155362, -0.00187571, -0.00123152, -0.00123152, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00090942, -0.00187571, -0.00123152],
#[Out]#         [-0.00187571, -0.00090942, -0.00155362, -0.00090942, -0.00155362,
#[Out]#          -0.00155362, -0.00090942, -0.00187571, -0.00090942, -0.00090942,
#[Out]#          -0.00123152, -0.00155362, -0.00123152, -0.00187571, -0.00187571,
#[Out]#          -0.00123152, -0.00187571, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00123152, -0.00187571, -0.00219781, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00123152, -0.00187571, -0.00058732],
#[Out]#         [-0.00155362, -0.00187571, -0.00090942, -0.00155362, -0.00123152,
#[Out]#          -0.00155362, -0.00058732, -0.00090942, -0.00123152, -0.00187571,
#[Out]#          -0.00155362, -0.00251991, -0.00155362, -0.00155362, -0.00123152,
#[Out]#          -0.00187571, -0.00155362, -0.00187571, -0.00219781, -0.00219781,
#[Out]#          -0.00090942, -0.00187571, -0.00123152, -0.00219781, -0.00123152,
#[Out]#          -0.00155362, -0.00155362, -0.00090942, -0.00123152, -0.00155362],
#[Out]#         [-0.00123152, -0.00187571, -0.00187571, -0.00090942, -0.00123152,
#[Out]#          -0.00187571, -0.00187571, -0.00123152, -0.00090942, -0.00155362,
#[Out]#          -0.00090942, -0.00090942, -0.00155362, -0.00123152, -0.00123152,
#[Out]#          -0.00155362, -0.00187571, -0.00090942, -0.00058732, -0.00187571,
#[Out]#          -0.00219781, -0.00187571, -0.00219781, -0.00219781, -0.00155362,
#[Out]#          -0.00187571, -0.00123152, -0.00123152, -0.00219781, -0.00219781],
#[Out]#         [-0.00155362, -0.00219781, -0.00155362, -0.00155362, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00123152, -0.00090942, -0.00123152,
#[Out]#          -0.00123152, -0.00155362, -0.00090942, -0.00155362, -0.00219781,
#[Out]#          -0.00155362, -0.00155362, -0.00187571, -0.00123152, -0.00123152,
#[Out]#          -0.00155362, -0.00155362, -0.00219781, -0.00123152, -0.00123152,
#[Out]#          -0.00187571, -0.00090942, -0.00187571, -0.00187571, -0.00155362],
#[Out]#         [-0.00187571, -0.00251991, -0.00155362, -0.00187571, -0.00090942,
#[Out]#          -0.00123152, -0.00090942, -0.00123152, -0.00187571, -0.00187571,
#[Out]#          -0.00187571, -0.00219781, -0.00187571, -0.00123152, -0.00219781,
#[Out]#          -0.00187571, -0.00090942, -0.00187571, -0.00155362, -0.00187571,
#[Out]#          -0.00090942, -0.00155362, -0.00123152, -0.00187571, -0.00155362,
#[Out]#          -0.00123152, -0.00187571, -0.00123152, -0.00187571, -0.00251991]]),
#[Out]#  'cap': array([[ 0.77116197,  0.77051777,  0.77083987,  0.77051777,  0.77083987,
#[Out]#           0.77019567,  0.77019567,  0.77083987,  0.77051777,  0.77148407,
#[Out]#           0.77148407,  0.77148407,  0.77083987,  0.77051777,  0.77309456,
#[Out]#           0.77309456,  0.77373876,  0.77470506,  0.77406086,  0.77083987,
#[Out]#           0.77180616,  0.77212826,  0.77277246,  0.77373876,  0.77212826,
#[Out]#           0.77309456,  0.77406086,  0.77502716,  0.77502716,  0.77245036],
#[Out]#         [ 0.77309456,  0.77438296,  0.77438296,  0.77309456,  0.77309456,
#[Out]#           0.77470506,  0.77438296,  0.77502716,  0.77406086,  0.77406086,
#[Out]#           0.77373876,  0.77470506,  0.77502716,  0.77245036,  0.77438296,
#[Out]#           0.77502716,  0.77502716,  0.77438296,  0.77309456,  0.77309456,
#[Out]#           0.77406086,  0.77534926,  0.77470506,  0.77438296,  0.77470506,
#[Out]#           0.77502716,  0.77470506,  0.77083987,  0.77180616,  0.77309456],
#[Out]#         [ 0.77341666,  0.77438296,  0.77083987,  0.77019567,  0.77051777,
#[Out]#           0.77212826,  0.77277246,  0.77373876,  0.77406086,  0.77341666,
#[Out]#           0.77277246,  0.77373876,  0.77470506,  0.77245036,  0.77309456,
#[Out]#           0.77212826,  0.77341666,  0.77309456,  0.77406086,  0.77051777,
#[Out]#           0.77083987,  0.77051777,  0.77148407,  0.77212826,  0.77180616,
#[Out]#           0.77277246,  0.77245036,  0.77212826,  0.77245036,  0.77470506],
#[Out]#         [ 0.76955147,  0.77083987,  0.77083987,  0.77180616,  0.77277246,
#[Out]#           0.77373876,  0.77245036,  0.77083987,  0.77116197,  0.77277246,
#[Out]#           0.77212826,  0.77309456,  0.77309456,  0.77341666,  0.77309456,
#[Out]#           0.77438296,  0.77406086,  0.77438296,  0.77534926,  0.77470506,
#[Out]#           0.77406086,  0.77438296,  0.77406086,  0.77534926,  0.77373876,
#[Out]#           0.77502716,  0.77470506,  0.77502716,  0.77599345,  0.77631555],
#[Out]#         [ 0.77438296,  0.77470506,  0.77534926,  0.77502716,  0.77534926,
#[Out]#           0.77534926,  0.77567135,  0.77502716,  0.77567135,  0.77534926,
#[Out]#           0.77534926,  0.77470506,  0.77567135,  0.77567135,  0.77502716,
#[Out]#           0.77534926,  0.77567135,  0.77534926,  0.77502716,  0.77438296,
#[Out]#           0.77631555,  0.77534926,  0.77502716,  0.77567135,  0.77502716,
#[Out]#           0.77599345,  0.77502716,  0.77502716,  0.77534926,  0.77567135],
#[Out]#         [ 0.77470506,  0.77502716,  0.77534926,  0.77502716,  0.77534926,
#[Out]#           0.77502716,  0.77534926,  0.77567135,  0.77567135,  0.77083987,
#[Out]#           0.77212826,  0.77277246,  0.77309456,  0.77083987,  0.77309456,
#[Out]#           0.77116197,  0.77116197,  0.77051777,  0.77212826,  0.77148407,
#[Out]#           0.77245036,  0.77309456,  0.77341666,  0.77309456,  0.77180616,
#[Out]#           0.77180616,  0.77116197,  0.77116197,  0.77148407,  0.77148407],
#[Out]#         [ 0.77148407,  0.77148407,  0.77245036,  0.77406086,  0.77406086,
#[Out]#           0.77470506,  0.77341666,  0.77470506,  0.77502716,  0.77470506,
#[Out]#           0.77534926,  0.77534926,  0.77534926,  0.77438296,  0.77534926,
#[Out]#           0.77406086,  0.77438296,  0.77502716,  0.77341666,  0.77502716,
#[Out]#           0.77502716,  0.77438296,  0.77373876,  0.77470506,  0.77567135,
#[Out]#           0.77470506,  0.77341666,  0.77116197,  0.77051777,  0.77148407],
#[Out]#         [ 0.77373876,  0.77341666,  0.77212826,  0.77212826,  0.77245036,
#[Out]#           0.77277246,  0.77309456,  0.77438296,  0.77277246,  0.77373876,
#[Out]#           0.77309456,  0.77373876,  0.77406086,  0.77406086,  0.77567135,
#[Out]#           0.77567135,  0.77470506,  0.77470506,  0.77567135,  0.77567135,
#[Out]#           0.77502716,  0.77534926,  0.77567135,  0.77567135,  0.77534926,
#[Out]#           0.77470506,  0.77470506,  0.77502716,  0.77534926,  0.77534926],
#[Out]#         [ 0.77470506,  0.77341666,  0.77470506,  0.77406086,  0.77470506,
#[Out]#           0.77534926,  0.77470506,  0.77534926,  0.77502716,  0.77470506,
#[Out]#           0.77534926,  0.77502716,  0.77406086,  0.77406086,  0.77277246,
#[Out]#           0.77406086,  0.77438296,  0.77309456,  0.77438296,  0.77470506,
#[Out]#           0.77599345,  0.77373876,  0.77406086,  0.77406086,  0.77502716,
#[Out]#           0.77438296,  0.77470506,  0.77502716,  0.77534926,  0.77534926],
#[Out]#         [ 0.77373876,  0.77438296,  0.77470506,  0.77470506,  0.77599345,
#[Out]#           0.77470506,  0.77502716,  0.77438296,  0.77438296,  0.77438296,
#[Out]#           0.77406086,  0.77534926,  0.77341666,  0.77470506,  0.77373876,
#[Out]#           0.77470506,  0.77470506,  0.77406086,  0.77438296,  0.77470506,
#[Out]#           0.77438296,  0.77502716,  0.77277246,  0.77438296,  0.77502716,
#[Out]#           0.77116197,  0.77051777,  0.77051777,  0.77116197,  0.77051777],
#[Out]#         [ 0.77019567,  0.77019567,  0.77051777,  0.77212826,  0.77116197,
#[Out]#           0.77245036,  0.77245036,  0.77406086,  0.77341666,  0.77309456,
#[Out]#           0.77438296,  0.77406086,  0.77406086,  0.77438296,  0.77406086,
#[Out]#           0.77534926,  0.77470506,  0.77534926,  0.77470506,  0.77567135,
#[Out]#           0.77534926,  0.77567135,  0.77438296,  0.77406086,  0.77438296,
#[Out]#           0.77502716,  0.77470506,  0.77502716,  0.77406086,  0.77406086],
#[Out]#         [ 0.77406086,  0.77373876,  0.77502716,  0.77438296,  0.77502716,
#[Out]#           0.77438296,  0.77470506,  0.77341666,  0.77470506,  0.77438296,
#[Out]#           0.77502716,  0.77470506,  0.77534926,  0.77599345,  0.77438296,
#[Out]#           0.77406086,  0.77567135,  0.77534926,  0.77534926,  0.77502716,
#[Out]#           0.77534926,  0.77502716,  0.77438296,  0.77502716,  0.77534926,
#[Out]#           0.77534926,  0.77502716,  0.77406086,  0.77502716,  0.77534926],
#[Out]#         [ 0.77438296,  0.77502716,  0.77502716,  0.77438296,  0.77470506,
#[Out]#           0.77438296,  0.77470506,  0.77341666,  0.77438296,  0.77599345,
#[Out]#           0.77212826,  0.77406086,  0.77438296,  0.77502716,  0.77534926,
#[Out]#           0.77502716,  0.77534926,  0.77470506,  0.77438296,  0.77470506,
#[Out]#           0.77502716,  0.77373876,  0.77083987,  0.77083987,  0.77309456,
#[Out]#           0.77277246,  0.77277246,  0.77502716,  0.77534926,  0.77019567],
#[Out]#         [ 0.77116197,  0.77148407,  0.77051777,  0.77083987,  0.77083987,
#[Out]#           0.77083987,  0.77083987,  0.77116197,  0.77019567,  0.77180616,
#[Out]#           0.77341666,  0.77373876,  0.77309456,  0.77406086,  0.77470506,
#[Out]#           0.77567135,  0.77438296,  0.77438296,  0.77534926,  0.77599345,
#[Out]#           0.77502716,  0.77534926,  0.77534926,  0.77534926,  0.77534926,
#[Out]#           0.77567135,  0.77502716,  0.77534926,  0.77502716,  0.77534926],
#[Out]#         [ 0.77502716,  0.77470506,  0.77470506,  0.77534926,  0.77534926,
#[Out]#           0.77534926,  0.77438296,  0.77470506,  0.77502716,  0.77534926,
#[Out]#           0.77502716,  0.77534926,  0.77406086,  0.77534926,  0.77502716,
#[Out]#           0.77502716,  0.77438296,  0.77470506,  0.77502716,  0.77470506,
#[Out]#           0.77534926,  0.77438296,  0.77534926,  0.77502716,  0.77534926,
#[Out]#           0.77567135,  0.77502716,  0.77470506,  0.77534926,  0.77502716],
#[Out]#         [ 0.77438296,  0.77470506,  0.77502716,  0.77534926,  0.77567135,
#[Out]#           0.77470506,  0.77470506,  0.77534926,  0.77438296,  0.77534926,
#[Out]#           0.77470506,  0.77534926,  0.77502716,  0.77567135,  0.77534926,
#[Out]#           0.77470506,  0.77502716,  0.77470506,  0.77534926,  0.77567135,
#[Out]#           0.77502716,  0.77470506,  0.77470506,  0.77534926,  0.77534926,
#[Out]#           0.77534926,  0.77534926,  0.77470506,  0.77502716,  0.77470506],
#[Out]#         [ 0.77470506,  0.77470506,  0.77470506,  0.77534926,  0.77502716,
#[Out]#           0.77470506,  0.77502716,  0.77470506,  0.77567135,  0.77470506,
#[Out]#           0.77470506,  0.77470506,  0.77083987,  0.77148407,  0.77212826,
#[Out]#           0.77309456,  0.77373876,  0.77534926,  0.77502716,  0.77083987,
#[Out]#           0.77116197,  0.77245036,  0.77502716,  0.77534926,  0.77373876,
#[Out]#           0.77341666,  0.77438296,  0.77502716,  0.77470506,  0.77534926],
#[Out]#         [ 0.77406086,  0.77373876,  0.77341666,  0.77534926,  0.77534926,
#[Out]#           0.77470506,  0.77567135,  0.77502716,  0.77534926,  0.77051777,
#[Out]#           0.77051777,  0.77051777,  0.77083987,  0.77083987,  0.77051777,
#[Out]#           0.77212826,  0.77116197,  0.77116197,  0.77083987,  0.77051777,
#[Out]#           0.77148407,  0.77116197,  0.77212826,  0.77341666,  0.77309456,
#[Out]#           0.77148407,  0.77116197,  0.77116197,  0.77083987,  0.77116197],
#[Out]#         [ 0.77083987,  0.77083987,  0.77051777,  0.77083987,  0.77083987,
#[Out]#           0.77083987,  0.77148407,  0.77341666,  0.77309456,  0.77438296,
#[Out]#           0.77438296,  0.77502716,  0.77502716,  0.77470506,  0.77567135,
#[Out]#           0.77567135,  0.77567135,  0.77470506,  0.77470506,  0.77534926,
#[Out]#           0.77502716,  0.77470506,  0.77502716,  0.77502716,  0.77438296,
#[Out]#           0.77534926,  0.77534926,  0.77470506,  0.77502716,  0.77567135],
#[Out]#         [ 0.77502716,  0.77502716,  0.77502716,  0.77534926,  0.77534926,
#[Out]#           0.77470506,  0.77470506,  0.77567135,  0.77534926,  0.77470506,
#[Out]#           0.77502716,  0.77470506,  0.77534926,  0.77502716,  0.77502716,
#[Out]#           0.77567135,  0.77470506,  0.77470506,  0.77502716,  0.77567135,
#[Out]#           0.77470506,  0.77534926,  0.77502716,  0.77534926,  0.77567135,
#[Out]#           0.77534926,  0.77470506,  0.77534926,  0.77502716,  0.77567135],
#[Out]#         [ 0.77567135,  0.77470506,  0.77534926,  0.77502716,  0.77534926,
#[Out]#           0.77502716,  0.77567135,  0.77534926,  0.77470506,  0.77502716,
#[Out]#           0.77502716,  0.77534926,  0.77502716,  0.77534926,  0.77534926,
#[Out]#           0.77502716,  0.77567135,  0.77470506,  0.77534926,  0.77470506,
#[Out]#           0.77534926,  0.77534926,  0.77470506,  0.77502716,  0.77502716,
#[Out]#           0.77502716,  0.77470506,  0.77470506,  0.77534926,  0.77502716],
#[Out]#         [ 0.77534926,  0.77502716,  0.77470506,  0.77502716,  0.77534926,
#[Out]#           0.77502716,  0.77502716,  0.77470506,  0.77470506,  0.77502716,
#[Out]#           0.77502716,  0.77502716,  0.77470506,  0.77470506,  0.77502716,
#[Out]#           0.77534926,  0.77438296,  0.77502716,  0.77470506,  0.77502716,
#[Out]#           0.77438296,  0.77438296,  0.77502716,  0.77567135,  0.77502716,
#[Out]#           0.77534926,  0.77534926,  0.77534926,  0.77470506,  0.77534926],
#[Out]#         [ 0.77470506,  0.77534926,  0.77502716,  0.77567135,  0.77502716,
#[Out]#           0.77502716,  0.77502716,  0.77438296,  0.77470506,  0.77534926,
#[Out]#           0.77470506,  0.77438296,  0.77534926,  0.77470506,  0.77470506,
#[Out]#           0.77438296,  0.77470506,  0.77470506,  0.77534926,  0.77470506,
#[Out]#           0.77502716,  0.77534926,  0.77502716,  0.77534926,  0.77502716,
#[Out]#           0.77502716,  0.77470506,  0.77470506,  0.77470506,  0.77470506],
#[Out]#         [ 0.77470506,  0.77470506,  0.77502716,  0.77502716,  0.77502716,
#[Out]#           0.77534926,  0.77502716,  0.77470506,  0.77470506,  0.77534926,
#[Out]#           0.77534926,  0.77534926,  0.77534926,  0.77567135,  0.77502716,
#[Out]#           0.77534926,  0.77534926,  0.77534926,  0.77470506,  0.77502716,
#[Out]#           0.77534926,  0.77567135,  0.77567135,  0.77534926,  0.77470506,
#[Out]#           0.77470506,  0.77534926,  0.77534926,  0.77470506,  0.77502716],
#[Out]#         [ 0.77470506,  0.77438296,  0.77470506,  0.77341666,  0.77502716,
#[Out]#           0.77502716,  0.77470506,  0.77502716,  0.77502716,  0.77502716,
#[Out]#           0.77470506,  0.77534926,  0.77470506,  0.77116197,  0.77051777,
#[Out]#           0.77341666,  0.77470506,  0.77406086,  0.77470506,  0.77470506,
#[Out]#           0.77406086,  0.77534926,  0.77502716,  0.77470506,  0.77502716,
#[Out]#           0.77502716,  0.77534926,  0.77502716,  0.77534926,  0.77502716],
#[Out]#         [ 0.77373876,  0.77470506,  0.77438296,  0.77502716,  0.77470506,
#[Out]#           0.77534926,  0.77502716,  0.77534926,  0.77502716,  0.77470506,
#[Out]#           0.77470506,  0.77502716,  0.77534926,  0.77470506,  0.77567135,
#[Out]#           0.77502716,  0.77470506,  0.77406086,  0.77438296,  0.77341666,
#[Out]#           0.77470506,  0.77470506,  0.77470506,  0.77567135,  0.77470506,
#[Out]#           0.77567135,  0.77534926,  0.77502716,  0.77502716,  0.77502716],
#[Out]#         [ 0.77373876,  0.77470506,  0.77502716,  0.77534926,  0.77438296,
#[Out]#           0.77470506,  0.77534926,  0.77534926,  0.77502716,  0.77470506,
#[Out]#           0.77470506,  0.77502716,  0.77438296,  0.77567135,  0.77534926,
#[Out]#           0.77470506,  0.77534926,  0.77502716,  0.77502716,  0.77502716,
#[Out]#           0.77406086,  0.77470506,  0.77470506,  0.77212826,  0.77567135,
#[Out]#           0.77502716,  0.77406086,  0.77470506,  0.77567135,  0.77534926],
#[Out]#         [ 0.77470506,  0.77502716,  0.77406086,  0.77309456,  0.77470506,
#[Out]#           0.77502716,  0.77470506,  0.77534926,  0.77534926,  0.77567135,
#[Out]#           0.77502716,  0.77534926,  0.77502716,  0.77470506,  0.77470506,
#[Out]#           0.77438296,  0.77470506,  0.77534926,  0.77502716,  0.77470506,
#[Out]#           0.77567135,  0.77502716,  0.77567135,  0.77502716,  0.77470506,
#[Out]#           0.77502716,  0.77470506,  0.77502716,  0.77470506,  0.77534926],
#[Out]#         [ 0.77341666,  0.77438296,  0.77373876,  0.77502716,  0.77438296,
#[Out]#           0.77470506,  0.77502716,  0.77470506,  0.77470506,  0.77470506,
#[Out]#           0.77502716,  0.77502716,  0.77438296,  0.77406086,  0.77502716,
#[Out]#           0.77534926,  0.77502716,  0.77341666,  0.77502716,  0.77534926,
#[Out]#           0.77470506,  0.77567135,  0.77373876,  0.77438296,  0.77502716,
#[Out]#           0.77470506,  0.77470506,  0.77502716,  0.77534926,  0.77502716],
#[Out]#         [ 0.77470506,  0.77438296,  0.77438296,  0.77502716,  0.77438296,
#[Out]#           0.77567135,  0.77438296,  0.77470506,  0.77567135,  0.77438296,
#[Out]#           0.77470506,  0.77502716,  0.77438296,  0.77502716,  0.77502716,
#[Out]#           0.77438296,  0.77470506,  0.77534926,  0.77502716,  0.77470506,
#[Out]#           0.77502716,  0.77502716,  0.77470506,  0.77502716,  0.77502716,
#[Out]#           0.77502716,  0.77470506,  0.77534926,  0.77534926,  0.77438296]]),
#[Out]#  'dc': array([[ 0.13612974,  0.14249785,  0.14734766,  0.15030463,  0.15367389,
#[Out]#           0.15708918,  0.16111171,  0.16354049,  0.16592509,  0.16718722,
#[Out]#           0.16906696,  0.17106462,  0.17255195,  0.17283959,  0.17291789,
#[Out]#           0.1728497 ,  0.17287761,  0.17159179,  0.16978769,  0.16816774,
#[Out]#           0.16523801,  0.16280137,  0.16011161,  0.15683169,  0.15261249,
#[Out]#           0.14829341,  0.14324841,  0.13876579,  0.13265552,  0.12818408],
#[Out]#         [ 0.14215615,  0.14786756,  0.15132999,  0.15637788,  0.15982739,
#[Out]#           0.16359829,  0.16751002,  0.17069236,  0.17384604,  0.17609388,
#[Out]#           0.1774866 ,  0.17943801,  0.18069419,  0.18189595,  0.18247994,
#[Out]#           0.18326505,  0.18307232,  0.18122184,  0.18139074,  0.18071773,
#[Out]#           0.17794605,  0.17482414,  0.17067949,  0.16885357,  0.16510825,
#[Out]#           0.16045266,  0.15469018,  0.15068505,  0.14742348,  0.14097532],
#[Out]#         [ 0.14575809,  0.14953938,  0.15341828,  0.15889267,  0.163491  ,
#[Out]#           0.16818358,  0.17241958,  0.17561384,  0.17883459,  0.18235611,
#[Out]#           0.1850736 ,  0.18851425,  0.19014675,  0.19140869,  0.19125464,
#[Out]#           0.19223754,  0.19188293,  0.19118945,  0.18953603,  0.18851489,
#[Out]#           0.18653715,  0.18513906,  0.18118006,  0.1778801 ,  0.17392192,
#[Out]#           0.17001273,  0.16527201,  0.15884548,  0.15463874,  0.14780605],
#[Out]#         [ 0.14843765,  0.15377007,  0.15976637,  0.16495842,  0.17265689,
#[Out]#           0.18414661,  0.18883409,  0.19367365,  0.19815722,  0.20222478,
#[Out]#           0.20533004,  0.20809539,  0.21119828,  0.21338701,  0.21512466,
#[Out]#           0.21662079,  0.21750222,  0.21822373,  0.21756325,  0.21647494,
#[Out]#           0.21364889,  0.21062965,  0.20959998,  0.20751486,  0.20412206,
#[Out]#           0.19969896,  0.19587857,  0.19337659,  0.19099118,  0.19282459],
#[Out]#         [ 0.16948632,  0.17866791,  0.18767058,  0.20029914,  0.22893765,
#[Out]#           0.24235059,  0.25049162,  0.25860233,  0.2651887 ,  0.27260251,
#[Out]#           0.27714504,  0.2822068 ,  0.28493065,  0.28772136,  0.28968579,
#[Out]#           0.29034406,  0.29148642,  0.28950043,  0.28767165,  0.28520394,
#[Out]#           0.28281539,  0.27808384,  0.27266502,  0.26743221,  0.26231705,
#[Out]#           0.25555791,  0.24665121,  0.23631297,  0.22767728,  0.21670666],
#[Out]#         [ 0.19873265,  0.21100542,  0.21977188,  0.22947663,  0.24014054,
#[Out]#           0.24795402,  0.25677181,  0.2637642 ,  0.27281808,  0.27869706,
#[Out]#           0.28232388,  0.28804559,  0.29261392,  0.29463297,  0.29743212,
#[Out]#           0.29927141,  0.2997465 ,  0.29896593,  0.29833026,  0.29585228,
#[Out]#           0.29271627,  0.28944068,  0.28495344,  0.28025283,  0.27367134,
#[Out]#           0.26646827,  0.25779761,  0.24849189,  0.2394967 ,  0.22930218],
#[Out]#         [ 0.20285255,  0.21236596,  0.22222251,  0.23224378,  0.24274034,
#[Out]#           0.25056836,  0.25945467,  0.26863691,  0.27592197,  0.28312885,
#[Out]#           0.28678707,  0.29304829,  0.29768503,  0.3006441 ,  0.30319245,
#[Out]#           0.30514736,  0.30561965,  0.30615818,  0.30516056,  0.30286594,
#[Out]#           0.30069108,  0.29617423,  0.29236847,  0.28779257,  0.28034304,
#[Out]#           0.27239742,  0.26451964,  0.25542045,  0.24591245,  0.23574987],
#[Out]#         [ 0.20085097,  0.21103143,  0.22186236,  0.23349975,  0.24377127,
#[Out]#           0.25318941,  0.26204046,  0.27230267,  0.27908103,  0.28721626,
#[Out]#           0.29286349,  0.29870446,  0.30209324,  0.30586226,  0.3100746 ,
#[Out]#           0.31146516,  0.3125918 ,  0.31285077,  0.31201861,  0.30867485,
#[Out]#           0.3067191 ,  0.30344203,  0.29819128,  0.29305612,  0.28758268,
#[Out]#           0.27977431,  0.27149144,  0.25929998,  0.25172671,  0.24218568],
#[Out]#         [ 0.19974538,  0.21243846,  0.22104272,  0.2321091 ,  0.24322192,
#[Out]#           0.25266173,  0.26208823,  0.26998197,  0.2792756 ,  0.28771916,
#[Out]#           0.29253075,  0.29900513,  0.30321153,  0.30829727,  0.31124698,
#[Out]#           0.31354558,  0.31453279,  0.31391007,  0.31368189,  0.31169414,
#[Out]#           0.31092905,  0.30729557,  0.30142751,  0.29743732,  0.28974746,
#[Out]#           0.28244463,  0.2742162 ,  0.26568959,  0.25604585,  0.2442149 ],
#[Out]#         [ 0.19682858,  0.21310614,  0.22339307,  0.2327661 ,  0.24393898,
#[Out]#           0.25312378,  0.2619916 ,  0.27215869,  0.28070189,  0.28786253,
#[Out]#           0.2938535 ,  0.30047832,  0.30597665,  0.31096141,  0.31473021,
#[Out]#           0.31746763,  0.31675868,  0.31828369,  0.31771692,  0.31607368,
#[Out]#           0.31348544,  0.31080316,  0.30474842,  0.30121153,  0.29175   ,
#[Out]#           0.28587922,  0.27766356,  0.26812694,  0.26032991,  0.24924023],
#[Out]#         [ 0.19462236,  0.20767336,  0.21854238,  0.2300556 ,  0.24209514,
#[Out]#           0.2518002 ,  0.26235818,  0.27071866,  0.27881213,  0.28638907,
#[Out]#           0.2934512 ,  0.29960453,  0.30465641,  0.30897521,  0.31276753,
#[Out]#           0.31410452,  0.31652544,  0.31674661,  0.31636961,  0.31576957,
#[Out]#           0.31349634,  0.31090852,  0.30498034,  0.30044667,  0.29537238,
#[Out]#           0.2877263 ,  0.2793132 ,  0.27018783,  0.26019533,  0.2502043 ],
#[Out]#         [ 0.19320259,  0.20500889,  0.21639095,  0.22699071,  0.23900779,
#[Out]#           0.24968848,  0.25938366,  0.26848405,  0.27632141,  0.28390205,
#[Out]#           0.29068406,  0.29904959,  0.30324471,  0.30818423,  0.31217136,
#[Out]#           0.31408131,  0.3162665 ,  0.31695647,  0.31658286,  0.31680324,
#[Out]#           0.31454986,  0.31130412,  0.30686846,  0.30286107,  0.29692925,
#[Out]#           0.29058962,  0.28145321,  0.27163324,  0.26251448,  0.25248787],
#[Out]#         [ 0.1890537 ,  0.19975825,  0.21202985,  0.22520219,  0.23588518,
#[Out]#           0.24463848,  0.2550324 ,  0.26484581,  0.27368376,  0.28030647,
#[Out]#           0.28893363,  0.29559919,  0.30086419,  0.30538032,  0.30872603,
#[Out]#           0.31173094,  0.31521269,  0.31624471,  0.31700992,  0.31588973,
#[Out]#           0.31366561,  0.31033845,  0.30700749,  0.30266263,  0.29428657,
#[Out]#           0.28939011,  0.28090553,  0.27172971,  0.26119353,  0.25114746],
#[Out]#         [ 0.18666452,  0.19601772,  0.20641421,  0.22005682,  0.23115632,
#[Out]#           0.24188368,  0.25149334,  0.26084442,  0.26909364,  0.28028755,
#[Out]#           0.28507929,  0.29233013,  0.29695129,  0.30291441,  0.30622127,
#[Out]#           0.30981103,  0.31198909,  0.31382135,  0.31423865,  0.31311353,
#[Out]#           0.31148363,  0.30881657,  0.30390088,  0.29936451,  0.29383965,
#[Out]#           0.28762993,  0.27938236,  0.27103989,  0.26105007,  0.25137881],
#[Out]#         [ 0.18006417,  0.19277166,  0.20302691,  0.21546188,  0.22704433,
#[Out]#           0.2368505 ,  0.24534286,  0.2553033 ,  0.26473766,  0.2737205 ,
#[Out]#           0.28150738,  0.28836199,  0.29388579,  0.29900105,  0.30271707,
#[Out]#           0.30577625,  0.30849671,  0.31073814,  0.31043539,  0.30925713,
#[Out]#           0.30856096,  0.30609492,  0.30127752,  0.2970819 ,  0.29118255,
#[Out]#           0.28460709,  0.27543906,  0.2667581 ,  0.25842355,  0.24589551],
#[Out]#         [ 0.17413286,  0.18768045,  0.19665183,  0.20798329,  0.21930588,
#[Out]#           0.23049985,  0.24050687,  0.2493497 ,  0.25878087,  0.26746813,
#[Out]#           0.27455203,  0.28173736,  0.28735993,  0.29396684,  0.29813676,
#[Out]#           0.30072889,  0.3039154 ,  0.30516135,  0.30515728,  0.30465957,
#[Out]#           0.30293765,  0.30026003,  0.29493662,  0.29116808,  0.28604599,
#[Out]#           0.27925919,  0.27179797,  0.26227993,  0.2536533 ,  0.24430957],
#[Out]#         [ 0.16845221,  0.18066209,  0.18991357,  0.20190386,  0.21204364,
#[Out]#           0.22143668,  0.2337064 ,  0.24283338,  0.25115062,  0.25938548,
#[Out]#           0.26677459,  0.2737668 ,  0.28052504,  0.28508919,  0.28982504,
#[Out]#           0.29320836,  0.29525496,  0.29712728,  0.29749105,  0.29714377,
#[Out]#           0.29596399,  0.29360942,  0.29073996,  0.28655655,  0.28031181,
#[Out]#           0.2765915 ,  0.26601353,  0.25773907,  0.24963825,  0.23963328],
#[Out]#         [ 0.16181836,  0.17238391,  0.18216029,  0.19298118,  0.20567275,
#[Out]#           0.21671482,  0.22456043,  0.23472532,  0.24438238,  0.25247155,
#[Out]#           0.25995084,  0.26680787,  0.27387092,  0.27801637,  0.28356301,
#[Out]#           0.28721927,  0.2897364 ,  0.29137446,  0.29193438,  0.29223344,
#[Out]#           0.29013598,  0.28731239,  0.28364188,  0.28016372,  0.27466907,
#[Out]#           0.267983  ,  0.2600219 ,  0.25208261,  0.24369148,  0.23469233],
#[Out]#         [ 0.15433607,  0.16606489,  0.17406557,  0.18531657,  0.19718949,
#[Out]#           0.20639048,  0.2171225 ,  0.22582104,  0.23596159,  0.24381198,
#[Out]#           0.25010665,  0.25888393,  0.26396623,  0.26932187,  0.27401958,
#[Out]#           0.27727373,  0.28081897,  0.2818931 ,  0.28306987,  0.28299493,
#[Out]#           0.28187347,  0.27979762,  0.27652509,  0.27215652,  0.26775851,
#[Out]#           0.26067997,  0.25466588,  0.24533662,  0.23761284,  0.22693515],
#[Out]#         [ 0.14740272,  0.15620169,  0.16549361,  0.17691392,  0.18838397,
#[Out]#           0.19678513,  0.20732432,  0.21477981,  0.22416921,  0.23348275,
#[Out]#           0.2412261 ,  0.24804382,  0.25364857,  0.25991599,  0.2644954 ,
#[Out]#           0.26784667,  0.26948527,  0.27221704,  0.27262853,  0.27186257,
#[Out]#           0.27156465,  0.26888531,  0.26695589,  0.26264703,  0.25711988,
#[Out]#           0.25136355,  0.24293558,  0.23547341,  0.22800329,  0.21842461],
#[Out]#         [ 0.13727648,  0.14608484,  0.15666521,  0.16744064,  0.1781342 ,
#[Out]#           0.18776163,  0.19498423,  0.20508262,  0.21335878,  0.22248514,
#[Out]#           0.22804045,  0.23742571,  0.24262652,  0.24881377,  0.25376852,
#[Out]#           0.25604471,  0.25940428,  0.26082471,  0.26190596,  0.2617093 ,
#[Out]#           0.26107809,  0.25955803,  0.25707838,  0.25311205,  0.24827244,
#[Out]#           0.24278236,  0.23555269,  0.2287416 ,  0.21982372,  0.21117356],
#[Out]#         [ 0.13167109,  0.14002534,  0.14681576,  0.1591344 ,  0.16930072,
#[Out]#           0.17749211,  0.18710192,  0.19534266,  0.20335068,  0.21207042,
#[Out]#           0.21894515,  0.2254874 ,  0.23168582,  0.23744902,  0.24193203,
#[Out]#           0.24503422,  0.24815065,  0.24976725,  0.25074636,  0.25110107,
#[Out]#           0.24984106,  0.248799  ,  0.24621417,  0.24273832,  0.23757868,
#[Out]#           0.23238069,  0.22710332,  0.22074221,  0.21173938,  0.20389677],
#[Out]#         [ 0.12366105,  0.1329155 ,  0.13988745,  0.14980701,  0.15907916,
#[Out]#           0.16611571,  0.1785913 ,  0.1858005 ,  0.19338184,  0.20243541,
#[Out]#           0.20820043,  0.2148099 ,  0.22136631,  0.22670803,  0.23132723,
#[Out]#           0.23394687,  0.23701752,  0.23821646,  0.23962338,  0.24069933,
#[Out]#           0.24000164,  0.2391551 ,  0.236062  ,  0.23246745,  0.22900355,
#[Out]#           0.22309525,  0.21736382,  0.21023834,  0.20177608,  0.1937257 ],
#[Out]#         [ 0.11339602,  0.12320163,  0.13170991,  0.13938472,  0.1486522 ,
#[Out]#           0.15641899,  0.16523382,  0.17325299,  0.1815541 ,  0.18939165,
#[Out]#           0.19553823,  0.20198484,  0.20716727,  0.21383666,  0.21791781,
#[Out]#           0.22128911,  0.2237913 ,  0.22599902,  0.22794894,  0.2278269 ,
#[Out]#           0.22695333,  0.22539021,  0.22171588,  0.21864046,  0.21506444,
#[Out]#           0.21166558,  0.20549166,  0.19775134,  0.19141126,  0.18317744],
#[Out]#         [ 0.10630039,  0.11404328,  0.12028676,  0.12901224,  0.13816594,
#[Out]#           0.14650427,  0.15538235,  0.16239964,  0.16857057,  0.17633428,
#[Out]#           0.18330578,  0.18990406,  0.19516492,  0.20097705,  0.20549332,
#[Out]#           0.20905441,  0.21059821,  0.21196286,  0.21457006,  0.2140875 ,
#[Out]#           0.21372215,  0.212965  ,  0.20955447,  0.20680372,  0.20321675,
#[Out]#           0.19947558,  0.1935967 ,  0.18816552,  0.18163541,  0.17365061],
#[Out]#         [ 0.097635  ,  0.10523662,  0.11337744,  0.12023566,  0.1289377 ,
#[Out]#           0.13631396,  0.14282582,  0.15208429,  0.15906411,  0.16447332,
#[Out]#           0.17136028,  0.17779153,  0.18310359,  0.18788099,  0.1920821 ,
#[Out]#           0.19461901,  0.19865506,  0.20048263,  0.20086566,  0.20126615,
#[Out]#           0.20135945,  0.1994903 ,  0.1973196 ,  0.19496475,  0.19136453,
#[Out]#           0.18683291,  0.18170485,  0.17577637,  0.16983394,  0.16267807],
#[Out]#         [ 0.09027284,  0.09683341,  0.10220616,  0.10981374,  0.11843925,
#[Out]#           0.12401429,  0.13150355,  0.13806911,  0.14415639,  0.1513745 ,
#[Out]#           0.15734112,  0.16294084,  0.16819971,  0.17256411,  0.17648278,
#[Out]#           0.17938543,  0.18319902,  0.18469423,  0.18552294,  0.18559451,
#[Out]#           0.18585717,  0.18436106,  0.18296896,  0.179974  ,  0.17745283,
#[Out]#           0.17209739,  0.16768534,  0.16345122,  0.1567523 ,  0.14976965],
#[Out]#         [ 0.08190497,  0.08605774,  0.09104509,  0.09827546,  0.1054179 ,
#[Out]#           0.11204548,  0.11778331,  0.12473566,  0.13100542,  0.13738886,
#[Out]#           0.14240752,  0.14792919,  0.15284387,  0.15692944,  0.16127175,
#[Out]#           0.16300283,  0.1659984 ,  0.16867088,  0.16932745,  0.16992317,
#[Out]#           0.16955968,  0.16854488,  0.16704823,  0.16482661,  0.16198974,
#[Out]#           0.15781918,  0.15436953,  0.14960056,  0.14333759,  0.13717743],
#[Out]#         [ 0.07275831,  0.07766347,  0.08368455,  0.08943863,  0.09616515,
#[Out]#           0.10332558,  0.10877257,  0.11456527,  0.12067347,  0.12604248,
#[Out]#           0.13078644,  0.13698465,  0.14090454,  0.14554858,  0.14799968,
#[Out]#           0.15100071,  0.15407452,  0.15579682,  0.15672262,  0.15744176,
#[Out]#           0.15658066,  0.15607006,  0.15507921,  0.15305971,  0.14935524,
#[Out]#           0.14628837,  0.14288365,  0.13786141,  0.13342035,  0.12791356],
#[Out]#         [ 0.06623215,  0.07072462,  0.07588564,  0.08203093,  0.08739816,
#[Out]#           0.09421123,  0.09881109,  0.10521256,  0.11057455,  0.11618316,
#[Out]#           0.12027407,  0.12514527,  0.12842342,  0.13275465,  0.13655667,
#[Out]#           0.13889628,  0.14213852,  0.14249631,  0.14494094,  0.14484606,
#[Out]#           0.14422987,  0.14404086,  0.14267763,  0.14117409,  0.13856319,
#[Out]#           0.13497279,  0.13116577,  0.12720472,  0.12219174,  0.11820715]])}
# Fri, 21 Jul 2017 08:41:01
spec.Vavg['dc']
#[Out]# array([[ 0.13612974,  0.14249785,  0.14734766,  0.15030463,  0.15367389,
#[Out]#          0.15708918,  0.16111171,  0.16354049,  0.16592509,  0.16718722,
#[Out]#          0.16906696,  0.17106462,  0.17255195,  0.17283959,  0.17291789,
#[Out]#          0.1728497 ,  0.17287761,  0.17159179,  0.16978769,  0.16816774,
#[Out]#          0.16523801,  0.16280137,  0.16011161,  0.15683169,  0.15261249,
#[Out]#          0.14829341,  0.14324841,  0.13876579,  0.13265552,  0.12818408],
#[Out]#        [ 0.14215615,  0.14786756,  0.15132999,  0.15637788,  0.15982739,
#[Out]#          0.16359829,  0.16751002,  0.17069236,  0.17384604,  0.17609388,
#[Out]#          0.1774866 ,  0.17943801,  0.18069419,  0.18189595,  0.18247994,
#[Out]#          0.18326505,  0.18307232,  0.18122184,  0.18139074,  0.18071773,
#[Out]#          0.17794605,  0.17482414,  0.17067949,  0.16885357,  0.16510825,
#[Out]#          0.16045266,  0.15469018,  0.15068505,  0.14742348,  0.14097532],
#[Out]#        [ 0.14575809,  0.14953938,  0.15341828,  0.15889267,  0.163491  ,
#[Out]#          0.16818358,  0.17241958,  0.17561384,  0.17883459,  0.18235611,
#[Out]#          0.1850736 ,  0.18851425,  0.19014675,  0.19140869,  0.19125464,
#[Out]#          0.19223754,  0.19188293,  0.19118945,  0.18953603,  0.18851489,
#[Out]#          0.18653715,  0.18513906,  0.18118006,  0.1778801 ,  0.17392192,
#[Out]#          0.17001273,  0.16527201,  0.15884548,  0.15463874,  0.14780605],
#[Out]#        [ 0.14843765,  0.15377007,  0.15976637,  0.16495842,  0.17265689,
#[Out]#          0.18414661,  0.18883409,  0.19367365,  0.19815722,  0.20222478,
#[Out]#          0.20533004,  0.20809539,  0.21119828,  0.21338701,  0.21512466,
#[Out]#          0.21662079,  0.21750222,  0.21822373,  0.21756325,  0.21647494,
#[Out]#          0.21364889,  0.21062965,  0.20959998,  0.20751486,  0.20412206,
#[Out]#          0.19969896,  0.19587857,  0.19337659,  0.19099118,  0.19282459],
#[Out]#        [ 0.16948632,  0.17866791,  0.18767058,  0.20029914,  0.22893765,
#[Out]#          0.24235059,  0.25049162,  0.25860233,  0.2651887 ,  0.27260251,
#[Out]#          0.27714504,  0.2822068 ,  0.28493065,  0.28772136,  0.28968579,
#[Out]#          0.29034406,  0.29148642,  0.28950043,  0.28767165,  0.28520394,
#[Out]#          0.28281539,  0.27808384,  0.27266502,  0.26743221,  0.26231705,
#[Out]#          0.25555791,  0.24665121,  0.23631297,  0.22767728,  0.21670666],
#[Out]#        [ 0.19873265,  0.21100542,  0.21977188,  0.22947663,  0.24014054,
#[Out]#          0.24795402,  0.25677181,  0.2637642 ,  0.27281808,  0.27869706,
#[Out]#          0.28232388,  0.28804559,  0.29261392,  0.29463297,  0.29743212,
#[Out]#          0.29927141,  0.2997465 ,  0.29896593,  0.29833026,  0.29585228,
#[Out]#          0.29271627,  0.28944068,  0.28495344,  0.28025283,  0.27367134,
#[Out]#          0.26646827,  0.25779761,  0.24849189,  0.2394967 ,  0.22930218],
#[Out]#        [ 0.20285255,  0.21236596,  0.22222251,  0.23224378,  0.24274034,
#[Out]#          0.25056836,  0.25945467,  0.26863691,  0.27592197,  0.28312885,
#[Out]#          0.28678707,  0.29304829,  0.29768503,  0.3006441 ,  0.30319245,
#[Out]#          0.30514736,  0.30561965,  0.30615818,  0.30516056,  0.30286594,
#[Out]#          0.30069108,  0.29617423,  0.29236847,  0.28779257,  0.28034304,
#[Out]#          0.27239742,  0.26451964,  0.25542045,  0.24591245,  0.23574987],
#[Out]#        [ 0.20085097,  0.21103143,  0.22186236,  0.23349975,  0.24377127,
#[Out]#          0.25318941,  0.26204046,  0.27230267,  0.27908103,  0.28721626,
#[Out]#          0.29286349,  0.29870446,  0.30209324,  0.30586226,  0.3100746 ,
#[Out]#          0.31146516,  0.3125918 ,  0.31285077,  0.31201861,  0.30867485,
#[Out]#          0.3067191 ,  0.30344203,  0.29819128,  0.29305612,  0.28758268,
#[Out]#          0.27977431,  0.27149144,  0.25929998,  0.25172671,  0.24218568],
#[Out]#        [ 0.19974538,  0.21243846,  0.22104272,  0.2321091 ,  0.24322192,
#[Out]#          0.25266173,  0.26208823,  0.26998197,  0.2792756 ,  0.28771916,
#[Out]#          0.29253075,  0.29900513,  0.30321153,  0.30829727,  0.31124698,
#[Out]#          0.31354558,  0.31453279,  0.31391007,  0.31368189,  0.31169414,
#[Out]#          0.31092905,  0.30729557,  0.30142751,  0.29743732,  0.28974746,
#[Out]#          0.28244463,  0.2742162 ,  0.26568959,  0.25604585,  0.2442149 ],
#[Out]#        [ 0.19682858,  0.21310614,  0.22339307,  0.2327661 ,  0.24393898,
#[Out]#          0.25312378,  0.2619916 ,  0.27215869,  0.28070189,  0.28786253,
#[Out]#          0.2938535 ,  0.30047832,  0.30597665,  0.31096141,  0.31473021,
#[Out]#          0.31746763,  0.31675868,  0.31828369,  0.31771692,  0.31607368,
#[Out]#          0.31348544,  0.31080316,  0.30474842,  0.30121153,  0.29175   ,
#[Out]#          0.28587922,  0.27766356,  0.26812694,  0.26032991,  0.24924023],
#[Out]#        [ 0.19462236,  0.20767336,  0.21854238,  0.2300556 ,  0.24209514,
#[Out]#          0.2518002 ,  0.26235818,  0.27071866,  0.27881213,  0.28638907,
#[Out]#          0.2934512 ,  0.29960453,  0.30465641,  0.30897521,  0.31276753,
#[Out]#          0.31410452,  0.31652544,  0.31674661,  0.31636961,  0.31576957,
#[Out]#          0.31349634,  0.31090852,  0.30498034,  0.30044667,  0.29537238,
#[Out]#          0.2877263 ,  0.2793132 ,  0.27018783,  0.26019533,  0.2502043 ],
#[Out]#        [ 0.19320259,  0.20500889,  0.21639095,  0.22699071,  0.23900779,
#[Out]#          0.24968848,  0.25938366,  0.26848405,  0.27632141,  0.28390205,
#[Out]#          0.29068406,  0.29904959,  0.30324471,  0.30818423,  0.31217136,
#[Out]#          0.31408131,  0.3162665 ,  0.31695647,  0.31658286,  0.31680324,
#[Out]#          0.31454986,  0.31130412,  0.30686846,  0.30286107,  0.29692925,
#[Out]#          0.29058962,  0.28145321,  0.27163324,  0.26251448,  0.25248787],
#[Out]#        [ 0.1890537 ,  0.19975825,  0.21202985,  0.22520219,  0.23588518,
#[Out]#          0.24463848,  0.2550324 ,  0.26484581,  0.27368376,  0.28030647,
#[Out]#          0.28893363,  0.29559919,  0.30086419,  0.30538032,  0.30872603,
#[Out]#          0.31173094,  0.31521269,  0.31624471,  0.31700992,  0.31588973,
#[Out]#          0.31366561,  0.31033845,  0.30700749,  0.30266263,  0.29428657,
#[Out]#          0.28939011,  0.28090553,  0.27172971,  0.26119353,  0.25114746],
#[Out]#        [ 0.18666452,  0.19601772,  0.20641421,  0.22005682,  0.23115632,
#[Out]#          0.24188368,  0.25149334,  0.26084442,  0.26909364,  0.28028755,
#[Out]#          0.28507929,  0.29233013,  0.29695129,  0.30291441,  0.30622127,
#[Out]#          0.30981103,  0.31198909,  0.31382135,  0.31423865,  0.31311353,
#[Out]#          0.31148363,  0.30881657,  0.30390088,  0.29936451,  0.29383965,
#[Out]#          0.28762993,  0.27938236,  0.27103989,  0.26105007,  0.25137881],
#[Out]#        [ 0.18006417,  0.19277166,  0.20302691,  0.21546188,  0.22704433,
#[Out]#          0.2368505 ,  0.24534286,  0.2553033 ,  0.26473766,  0.2737205 ,
#[Out]#          0.28150738,  0.28836199,  0.29388579,  0.29900105,  0.30271707,
#[Out]#          0.30577625,  0.30849671,  0.31073814,  0.31043539,  0.30925713,
#[Out]#          0.30856096,  0.30609492,  0.30127752,  0.2970819 ,  0.29118255,
#[Out]#          0.28460709,  0.27543906,  0.2667581 ,  0.25842355,  0.24589551],
#[Out]#        [ 0.17413286,  0.18768045,  0.19665183,  0.20798329,  0.21930588,
#[Out]#          0.23049985,  0.24050687,  0.2493497 ,  0.25878087,  0.26746813,
#[Out]#          0.27455203,  0.28173736,  0.28735993,  0.29396684,  0.29813676,
#[Out]#          0.30072889,  0.3039154 ,  0.30516135,  0.30515728,  0.30465957,
#[Out]#          0.30293765,  0.30026003,  0.29493662,  0.29116808,  0.28604599,
#[Out]#          0.27925919,  0.27179797,  0.26227993,  0.2536533 ,  0.24430957],
#[Out]#        [ 0.16845221,  0.18066209,  0.18991357,  0.20190386,  0.21204364,
#[Out]#          0.22143668,  0.2337064 ,  0.24283338,  0.25115062,  0.25938548,
#[Out]#          0.26677459,  0.2737668 ,  0.28052504,  0.28508919,  0.28982504,
#[Out]#          0.29320836,  0.29525496,  0.29712728,  0.29749105,  0.29714377,
#[Out]#          0.29596399,  0.29360942,  0.29073996,  0.28655655,  0.28031181,
#[Out]#          0.2765915 ,  0.26601353,  0.25773907,  0.24963825,  0.23963328],
#[Out]#        [ 0.16181836,  0.17238391,  0.18216029,  0.19298118,  0.20567275,
#[Out]#          0.21671482,  0.22456043,  0.23472532,  0.24438238,  0.25247155,
#[Out]#          0.25995084,  0.26680787,  0.27387092,  0.27801637,  0.28356301,
#[Out]#          0.28721927,  0.2897364 ,  0.29137446,  0.29193438,  0.29223344,
#[Out]#          0.29013598,  0.28731239,  0.28364188,  0.28016372,  0.27466907,
#[Out]#          0.267983  ,  0.2600219 ,  0.25208261,  0.24369148,  0.23469233],
#[Out]#        [ 0.15433607,  0.16606489,  0.17406557,  0.18531657,  0.19718949,
#[Out]#          0.20639048,  0.2171225 ,  0.22582104,  0.23596159,  0.24381198,
#[Out]#          0.25010665,  0.25888393,  0.26396623,  0.26932187,  0.27401958,
#[Out]#          0.27727373,  0.28081897,  0.2818931 ,  0.28306987,  0.28299493,
#[Out]#          0.28187347,  0.27979762,  0.27652509,  0.27215652,  0.26775851,
#[Out]#          0.26067997,  0.25466588,  0.24533662,  0.23761284,  0.22693515],
#[Out]#        [ 0.14740272,  0.15620169,  0.16549361,  0.17691392,  0.18838397,
#[Out]#          0.19678513,  0.20732432,  0.21477981,  0.22416921,  0.23348275,
#[Out]#          0.2412261 ,  0.24804382,  0.25364857,  0.25991599,  0.2644954 ,
#[Out]#          0.26784667,  0.26948527,  0.27221704,  0.27262853,  0.27186257,
#[Out]#          0.27156465,  0.26888531,  0.26695589,  0.26264703,  0.25711988,
#[Out]#          0.25136355,  0.24293558,  0.23547341,  0.22800329,  0.21842461],
#[Out]#        [ 0.13727648,  0.14608484,  0.15666521,  0.16744064,  0.1781342 ,
#[Out]#          0.18776163,  0.19498423,  0.20508262,  0.21335878,  0.22248514,
#[Out]#          0.22804045,  0.23742571,  0.24262652,  0.24881377,  0.25376852,
#[Out]#          0.25604471,  0.25940428,  0.26082471,  0.26190596,  0.2617093 ,
#[Out]#          0.26107809,  0.25955803,  0.25707838,  0.25311205,  0.24827244,
#[Out]#          0.24278236,  0.23555269,  0.2287416 ,  0.21982372,  0.21117356],
#[Out]#        [ 0.13167109,  0.14002534,  0.14681576,  0.1591344 ,  0.16930072,
#[Out]#          0.17749211,  0.18710192,  0.19534266,  0.20335068,  0.21207042,
#[Out]#          0.21894515,  0.2254874 ,  0.23168582,  0.23744902,  0.24193203,
#[Out]#          0.24503422,  0.24815065,  0.24976725,  0.25074636,  0.25110107,
#[Out]#          0.24984106,  0.248799  ,  0.24621417,  0.24273832,  0.23757868,
#[Out]#          0.23238069,  0.22710332,  0.22074221,  0.21173938,  0.20389677],
#[Out]#        [ 0.12366105,  0.1329155 ,  0.13988745,  0.14980701,  0.15907916,
#[Out]#          0.16611571,  0.1785913 ,  0.1858005 ,  0.19338184,  0.20243541,
#[Out]#          0.20820043,  0.2148099 ,  0.22136631,  0.22670803,  0.23132723,
#[Out]#          0.23394687,  0.23701752,  0.23821646,  0.23962338,  0.24069933,
#[Out]#          0.24000164,  0.2391551 ,  0.236062  ,  0.23246745,  0.22900355,
#[Out]#          0.22309525,  0.21736382,  0.21023834,  0.20177608,  0.1937257 ],
#[Out]#        [ 0.11339602,  0.12320163,  0.13170991,  0.13938472,  0.1486522 ,
#[Out]#          0.15641899,  0.16523382,  0.17325299,  0.1815541 ,  0.18939165,
#[Out]#          0.19553823,  0.20198484,  0.20716727,  0.21383666,  0.21791781,
#[Out]#          0.22128911,  0.2237913 ,  0.22599902,  0.22794894,  0.2278269 ,
#[Out]#          0.22695333,  0.22539021,  0.22171588,  0.21864046,  0.21506444,
#[Out]#          0.21166558,  0.20549166,  0.19775134,  0.19141126,  0.18317744],
#[Out]#        [ 0.10630039,  0.11404328,  0.12028676,  0.12901224,  0.13816594,
#[Out]#          0.14650427,  0.15538235,  0.16239964,  0.16857057,  0.17633428,
#[Out]#          0.18330578,  0.18990406,  0.19516492,  0.20097705,  0.20549332,
#[Out]#          0.20905441,  0.21059821,  0.21196286,  0.21457006,  0.2140875 ,
#[Out]#          0.21372215,  0.212965  ,  0.20955447,  0.20680372,  0.20321675,
#[Out]#          0.19947558,  0.1935967 ,  0.18816552,  0.18163541,  0.17365061],
#[Out]#        [ 0.097635  ,  0.10523662,  0.11337744,  0.12023566,  0.1289377 ,
#[Out]#          0.13631396,  0.14282582,  0.15208429,  0.15906411,  0.16447332,
#[Out]#          0.17136028,  0.17779153,  0.18310359,  0.18788099,  0.1920821 ,
#[Out]#          0.19461901,  0.19865506,  0.20048263,  0.20086566,  0.20126615,
#[Out]#          0.20135945,  0.1994903 ,  0.1973196 ,  0.19496475,  0.19136453,
#[Out]#          0.18683291,  0.18170485,  0.17577637,  0.16983394,  0.16267807],
#[Out]#        [ 0.09027284,  0.09683341,  0.10220616,  0.10981374,  0.11843925,
#[Out]#          0.12401429,  0.13150355,  0.13806911,  0.14415639,  0.1513745 ,
#[Out]#          0.15734112,  0.16294084,  0.16819971,  0.17256411,  0.17648278,
#[Out]#          0.17938543,  0.18319902,  0.18469423,  0.18552294,  0.18559451,
#[Out]#          0.18585717,  0.18436106,  0.18296896,  0.179974  ,  0.17745283,
#[Out]#          0.17209739,  0.16768534,  0.16345122,  0.1567523 ,  0.14976965],
#[Out]#        [ 0.08190497,  0.08605774,  0.09104509,  0.09827546,  0.1054179 ,
#[Out]#          0.11204548,  0.11778331,  0.12473566,  0.13100542,  0.13738886,
#[Out]#          0.14240752,  0.14792919,  0.15284387,  0.15692944,  0.16127175,
#[Out]#          0.16300283,  0.1659984 ,  0.16867088,  0.16932745,  0.16992317,
#[Out]#          0.16955968,  0.16854488,  0.16704823,  0.16482661,  0.16198974,
#[Out]#          0.15781918,  0.15436953,  0.14960056,  0.14333759,  0.13717743],
#[Out]#        [ 0.07275831,  0.07766347,  0.08368455,  0.08943863,  0.09616515,
#[Out]#          0.10332558,  0.10877257,  0.11456527,  0.12067347,  0.12604248,
#[Out]#          0.13078644,  0.13698465,  0.14090454,  0.14554858,  0.14799968,
#[Out]#          0.15100071,  0.15407452,  0.15579682,  0.15672262,  0.15744176,
#[Out]#          0.15658066,  0.15607006,  0.15507921,  0.15305971,  0.14935524,
#[Out]#          0.14628837,  0.14288365,  0.13786141,  0.13342035,  0.12791356],
#[Out]#        [ 0.06623215,  0.07072462,  0.07588564,  0.08203093,  0.08739816,
#[Out]#          0.09421123,  0.09881109,  0.10521256,  0.11057455,  0.11618316,
#[Out]#          0.12027407,  0.12514527,  0.12842342,  0.13275465,  0.13655667,
#[Out]#          0.13889628,  0.14213852,  0.14249631,  0.14494094,  0.14484606,
#[Out]#          0.14422987,  0.14404086,  0.14267763,  0.14117409,  0.13856319,
#[Out]#          0.13497279,  0.13116577,  0.12720472,  0.12219174,  0.11820715]])
# Fri, 21 Jul 2017 08:41:07
ax.imshow(spec.Vavg['dc'])
#[Out]# <matplotlib.image.AxesImage at 0x4afccc50>
# Fri, 21 Jul 2017 08:42:25
fig, ax = plt.subplot()
# Fri, 21 Jul 2017 08:42:34
fig, ax = plt.subplots()
# Fri, 21 Jul 2017 08:43:21
spec.psd.shape
#[Out]# (30, 30, 13501)
# Fri, 21 Jul 2017 08:43:36
psdAve = np.mean(spec.psd, axis=-1)
# Fri, 21 Jul 2017 08:43:42
import numpy as np
# Fri, 21 Jul 2017 08:43:43
psdAve = np.mean(spec.psd, axis=-1)
# Fri, 21 Jul 2017 08:43:45
psdAve.shape
#[Out]# (30, 30)
# Fri, 21 Jul 2017 08:43:51
ax.imshow(psdAve)
#[Out]# <matplotlib.image.AxesImage at 0x4c9e1da0>
# Fri, 21 Jul 2017 08:44:15
fig, ax = plt.subplots()
# Fri, 21 Jul 2017 08:44:22
ax.imshow(spec.Vavg['dc'])
#[Out]# <matplotlib.image.AxesImage at 0x4ee00588>
# Fri, 21 Jul 2017 08:48:50
daq.outputs
#[Out]# {'bias': OutputChannel; name: ao3; label: bias; V = 0.000,
#[Out]#  'x': OutputChannel; name: ao0; label: x; V = -0.001,
#[Out]#  'y': OutputChannel; name: ao1; label: y; V = -0.000,
#[Out]#  'z': OutputChannel; name: ao2; label: z; V = 0.000}
