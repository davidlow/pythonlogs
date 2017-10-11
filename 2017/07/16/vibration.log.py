# IPython log file

# Sun, 16 Jul 2017 23:24:38
get_ipython().magic('run -i qtconsole/2017/07/setups/setup_20170714.py')
# Sun, 16 Jul 2017 23:24:49
pf = Planefit.load()
# Sun, 16 Jul 2017 23:24:53
pf
#[Out]# <Nowack_Lab.Procedures.planefit.Planefit at 0xe7062b0>
# Sun, 16 Jul 2017 23:25:01
import numpy as np
# Sun, 16 Jul 2017 23:25:07
from importlib import reload
# Sun, 16 Jul 2017 23:25:14
get_ipython().magic('load qtconsole/2017/07/setups/vibration_20170716.py')
# Sun, 16 Jul 2017 23:25:25
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:25:37
import Nowack_Lab.Procedures.vibration
# Sun, 16 Jul 2017 23:25:41
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:26:54
plt
#[Out]# <module 'matplotlib.pyplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py'>
# Sun, 16 Jul 2017 23:26:58
v.dc
#[Out]# array([[-0.39209205,  0.18126701, -0.39196781],
#[Out]#        [-0.6498775 ,  0.76267649, -0.53539051],
#[Out]#        [-0.37243092, -0.22017736, -0.12037449]])
# Sun, 16 Jul 2017 23:27:51
fig,ax = plt.subplots()
# Sun, 16 Jul 2017 23:28:05
image = ax.imshow(v.dc)
# Sun, 16 Jul 2017 23:28:20
cbar = plt.colorbar(image)
# Sun, 16 Jul 2017 23:29:14
image = ax.imshow(v.dc, extend=[v.X.min(), v.X.max(), v.Y.min(), v.Y.max())

]
# Sun, 16 Jul 2017 23:29:29
image = ax.imshow(v.dc, extend=[v.X.min(), v.X.max(), v.Y.min(), v.Y.max()])
# Sun, 16 Jul 2017 23:29:37
image = ax.imshow(v.dc, extent=[v.X.min(), v.X.max(), v.Y.min(), v.Y.max()])
# Sun, 16 Jul 2017 23:34:02
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:35:14
plt.show()
# Sun, 16 Jul 2017 23:36:19
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:37:36
plt.show()
# Sun, 16 Jul 2017 23:37:56
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:39:15
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:40:49
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:42:07
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:43:50
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:45:48
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=30,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 23:54:44
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,1),
                ys=np.linspace(25,65,1),
                measure_time=30,
                averages=5
)
v.run()

# Sun, 16 Jul 2017 23:58:23
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,1),
                ys=np.linspace(25,65,1),
                measure_time=30,
                averages=10
)
v.run()

# Mon, 17 Jul 2017 00:08:01
get_ipython().magic('load qtconsole/2017/07/setups/vibration_20170716.py')
# Mon, 17 Jul 2017 00:09:05
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,21),
                ys=np.linspace(25,65,9),
                measure_time=30,
                averages=5
)
v.run()

# Mon, 17 Jul 2017 11:56:09
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,21),
                ys=np.linspace(25,65,9),
                measure_time=30,
                averages=5,
                scanheight=40
)
v.run()

