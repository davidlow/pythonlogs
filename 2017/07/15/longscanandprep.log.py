# IPython log file

get_ipython().magic('load qtconsole/2017/07/setups/startlog_20170703.py')
# Sat, 15 Jul 2017 17:47:42
get_ipython().magic('run -i qtconsole/2017/07/setups/setup_20170714.py')
# Sat, 15 Jul 2017 17:48:03
pf = Planefit.load()
# Sat, 15 Jul 2017 17:48:14
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  corrected lockin, now outputting x and y, not R and theta
'''
sc.run()

# Sat, 15 Jul 2017 17:48:24
pf.Z
#[Out]# array([[ 217.32455444,  216.09138489,  218.04899597,  223.94503784],
#[Out]#        [ 230.94483948,  215.2273407 ,  234.47645569,  235.68205261],
#[Out]#        [ 245.35163879,  243.02536011,  246.22119141,  243.06193542],
#[Out]#        [ 250.88485718,  252.848526  ,  252.88038635,  257.07608032]], dtype=float32)
# Sat, 15 Jul 2017 17:48:54
sc
#[Out]# <Nowack_Lab.Procedures.scanplane.Scanplane at 0xe70f748>
# Sat, 15 Jul 2017 17:48:56
sc.Z
# Sat, 15 Jul 2017 17:48:59
sc.Y
#[Out]# array([[-400.        , -400.        , -400.        , ..., -400.        ,
#[Out]#         -400.        , -400.        ],
#[Out]#        [-369.23076923, -369.23076923, -369.23076923, ..., -369.23076923,
#[Out]#         -369.23076923, -369.23076923],
#[Out]#        [-338.46153846, -338.46153846, -338.46153846, ..., -338.46153846,
#[Out]#         -338.46153846, -338.46153846],
#[Out]#        ..., 
#[Out]#        [ 338.46153846,  338.46153846,  338.46153846, ...,  338.46153846,
#[Out]#          338.46153846,  338.46153846],
#[Out]#        [ 369.23076923,  369.23076923,  369.23076923, ...,  369.23076923,
#[Out]#          369.23076923,  369.23076923],
#[Out]#        [ 400.        ,  400.        ,  400.        , ...,  400.        ,
#[Out]#          400.        ,  400.        ]])
# Sat, 15 Jul 2017 17:49:01
sc.X
#[Out]# array([[-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ],
#[Out]#        [-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ],
#[Out]#        [-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ],
#[Out]#        ..., 
#[Out]#        [-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ],
#[Out]#        [-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ],
#[Out]#        [-400.       , -399.5997999, -399.1995998, ...,  399.1995998,
#[Out]#          399.5997999,  400.       ]])
# Sat, 15 Jul 2017 17:49:02
sc.Z
# Sat, 15 Jul 2017 17:49:50
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0xe70f278>
# Sat, 15 Jul 2017 17:50:04
pf.plane.plane(sc.X, sc.Y)
# Sat, 15 Jul 2017 17:50:13
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0xe70f278>
# Sat, 15 Jul 2017 17:50:31
pf = Planefit.load(instruments=instruments)
# Sat, 15 Jul 2017 17:50:32
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0x13b30a58>
# Sat, 15 Jul 2017 17:54:01
pf
#[Out]# <Nowack_Lab.Utilities.save.Measurement at 0x13b30a58>
# Sat, 15 Jul 2017 17:54:05
pf.plane
# Sat, 15 Jul 2017 17:54:38
pf = Planefit(instruments=instruments)
# Sat, 15 Jul 2017 17:54:41
pf.run()
# Sat, 15 Jul 2017 18:12:45
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  corrected lockin, now outputting x and y, not R and theta
'''
sc.run()

# Sat, 15 Jul 2017 18:21:23
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=15)
sc.notes = '''
[dhl88]  corrected lockin, now outputting x and y, not R and theta
'''
sc.run()

# Sat, 15 Jul 2017 18:27:30
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=23)
sc.notes = '''
[dhl88]  checking scan height for out of contact scan
'''
sc.run()

# Sat, 15 Jul 2017 18:31:23
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2000,27],scan_rate=100, scanheight=30)
sc.notes = '''
[dhl88]  checking scan height for out of contact scan
'''
sc.run()
# Sat, 15 Jul 2017 18:42:47
get_ipython().magic('load qtconsole/2017/07/setups/longscan_20170715.py')
# Sat, 15 Jul 2017 18:42:50
# %load qtconsole/2017/07/setups/longscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[800,800], center=[0,0], 
            numpts=[2340,780],scan_rate=10, scanheight=30)
sc.notes = '''
[dhl88]  Long scan
'''
sc.run()

# Sun, 16 Jul 2017 16:55:16
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[100,100], center=[275,50], 
            numpts=[2000,27],scan_rate=10, scanheight=30)
sc.notes = '''
[dhl88]  scan near a vortex
'''
sc.run()

# Sun, 16 Jul 2017 17:07:55
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[100,10], center=[275,40], 
            numpts=[2000,27],scan_rate=10, scanheight=30)
sc.notes = '''
[dhl88]  scan near a vortex
'''
sc.run()

# Sun, 16 Jul 2017 18:15:30
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[100,10], center=[275,40], 
            numpts=[2000,27],scan_rate=10, scanheight=60)
sc.notes = '''
[dhl88]  scan near a vortex
'''
sc.run()

# Sun, 16 Jul 2017 18:37:14
sc
#[Out]# <Nowack_Lab.Procedures.scanplane.Scanplane at 0x13c016a0>
# Sun, 16 Jul 2017 18:37:22
sc.Vfull.dc
#[Out]# array([-1.43618207, -1.59529896, -1.41041415, ..., -1.41234674,
#[Out]#        -1.46356048, -1.45164282])
# Sun, 16 Jul 2017 18:37:41
size(sc.Vfull.dc)
# Sun, 16 Jul 2017 18:37:45
length(sc.Vfull.dc)
# Sun, 16 Jul 2017 18:37:49
len(sc.Vfull.dc)
#[Out]# 9001
# Sun, 16 Jul 2017 18:37:58
plt
#[Out]# <module 'matplotlib.pyplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py'>
# Sun, 16 Jul 2017 18:38:15
sc.X
#[Out]# array([[ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ],
#[Out]#        [ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ],
#[Out]#        [ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ],
#[Out]#        ..., 
#[Out]#        [ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ],
#[Out]#        [ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ],
#[Out]#        [ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#          324.94997499,  325.        ]])
# Sun, 16 Jul 2017 18:38:19
sc.X[-1]
#[Out]# array([ 225.        ,  225.05002501,  225.10005003, ...,  324.89994997,
#[Out]#         324.94997499,  325.        ])
# Sun, 16 Jul 2017 18:38:22
get_ipython().magic('ls ')
# Sun, 16 Jul 2017 18:38:24
sc
#[Out]# <Nowack_Lab.Procedures.scanplane.Scanplane at 0x13c016a0>
# Sun, 16 Jul 2017 18:38:55
sc.V.dc
#[Out]# array([[-1.34309547, -1.3423417 , -1.34526734, ..., -1.35129876,
#[Out]#         -1.3769194 , -1.37208437],
#[Out]#        [-1.39141031, -1.30692323, -1.39628095, ..., -1.37835813,
#[Out]#         -1.35745345, -1.26514753],
#[Out]#        [-1.4886842 , -1.33928039, -1.40229368, ..., -1.36766345,
#[Out]#         -1.42683604, -1.41653403],
#[Out]#        ..., 
#[Out]#        [-1.50833224, -1.50523677, -1.47922425, ..., -1.42643499,
#[Out]#         -1.47458806, -1.40365007],
#[Out]#        [-1.44294614, -1.53178924, -1.57230393, ..., -1.46851378,
#[Out]#         -1.43700254, -1.42072132],
#[Out]#        [-1.43618207, -1.502829  , -1.42250696, ..., -1.39418433,
#[Out]#         -1.47559415, -1.45164282]])
# Sun, 16 Jul 2017 18:39:00
sc.V.dc[-1]
#[Out]# array([-1.43618207, -1.502829  , -1.42250696, ..., -1.39418433,
#[Out]#        -1.47559415, -1.45164282])
# Sun, 16 Jul 2017 18:39:19
fig,ax = plt.subplots()
# Sun, 16 Jul 2017 18:39:34
ax.plot(sc.X[-1], sc.V.dc[-1])
#[Out]# [<matplotlib.lines.Line2D at 0x5c108d0>]
# Sun, 16 Jul 2017 18:39:51
fig,ax = plt.subplots()
# Sun, 16 Jul 2017 18:40:18
ax.plot(sc.X[-1], sc.V.dc[-1],marker='o', linestyle='',markersize=2))
# Sun, 16 Jul 2017 18:40:21
ax.plot(sc.X[-1], sc.V.dc[-1],marker='o', linestyle='',markersize=2)
#[Out]# [<matplotlib.lines.Line2D at 0x11d350b8>]
# Sun, 16 Jul 2017 18:42:46
# %load qtconsole/2017/07/setups/quickscan_20170715.py
plt.close('all')
sc = Scanplane(instruments,pf,span=[100,10], center=[275,40], 
            numpts=[2000,27],scan_rate=10, scanheight=30)
sc.notes = '''
[dhl88]  scan near a vortex
'''
sc.run()

# Sun, 16 Jul 2017 18:51:43
sc.preamp.gain
#[Out]# 5
# Sun, 16 Jul 2017 18:51:51
fig,ax = plt.subplots()
# Sun, 16 Jul 2017 18:52:42
import Nowack_Lab.Utilities.conversions as conv
# Sun, 16 Jul 2017 18:52:50
conv.Vsquid_to_phi0
#[Out]# {'High': 0.06944444444444445,
#[Out]#  'Low': 6.944444444444445,
#[Out]#  'Med': 0.6944444444444444}
# Sun, 16 Jul 2017 18:53:50
ax.plot(sc.X[-1], sc.V.dc[-1]/sc.preamp.gain*conv.Vsquid_to_phi0['High'],marker='o', linestyle='',markersize=2)
#[Out]# [<matplotlib.lines.Line2D at 0x10620f60>]
# Sun, 16 Jul 2017 18:54:25
ax.plot(sc.X[0], sc.V.dc[0]/sc.preamp.gain*conv.Vsquid_to_phi0['High'],marker='o', linestyle='',markersize=2)
#[Out]# [<matplotlib.lines.Line2D at 0x10ede208>]
# Sun, 16 Jul 2017 18:54:52
ax.plot(sc.X[13], sc.V.dc[13]/sc.preamp.gain*conv.Vsquid_to_phi0['High'],marker='o', linestyle='',markersize=2)
#[Out]# [<matplotlib.lines.Line2D at 0x10ede358>]
# Sun, 16 Jul 2017 19:56:33
np
# Sun, 16 Jul 2017 19:56:39
import numpy as np
# Sun, 16 Jul 2017 19:56:46
help(np.zero)
# Sun, 16 Jul 2017 19:56:50
help(np.zeros)
# Sun, 16 Jul 2017 19:57:03
np.zeros((2,2,2))
#[Out]# array([[[ 0.,  0.],
#[Out]#         [ 0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.],
#[Out]#         [ 0.,  0.]]])
# Sun, 16 Jul 2017 19:57:33
np.zeros((2,3,4))
#[Out]# array([[[ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.]]])
# Sun, 16 Jul 2017 19:59:30
xs,ys = np.meshgrid([1,2,3],[1,2,3])
# Sun, 16 Jul 2017 19:59:31
xs
#[Out]# array([[1, 2, 3],
#[Out]#        [1, 2, 3],
#[Out]#        [1, 2, 3]])
# Sun, 16 Jul 2017 19:59:34
ys
#[Out]# array([[1, 1, 1],
#[Out]#        [2, 2, 2],
#[Out]#        [3, 3, 3]])
# Sun, 16 Jul 2017 20:00:11
xs,ys = np.meshgrid([1,2,3],[1,2,3])
# Sun, 16 Jul 2017 20:00:18
help(np.meshgrid)
# Sun, 16 Jul 2017 20:00:48
xs,ys = np.meshgrid([1,2,3],[4,5,6],[7,8])
# Sun, 16 Jul 2017 20:00:53
xs,ys,zs = np.meshgrid([1,2,3],[4,5,6],[7,8])
# Sun, 16 Jul 2017 20:00:54
zs
#[Out]# array([[[7, 8],
#[Out]#         [7, 8],
#[Out]#         [7, 8]],
#[Out]# 
#[Out]#        [[7, 8],
#[Out]#         [7, 8],
#[Out]#         [7, 8]],
#[Out]# 
#[Out]#        [[7, 8],
#[Out]#         [7, 8],
#[Out]#         [7, 8]]])
# Sun, 16 Jul 2017 20:00:58
xs
#[Out]# array([[[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3]]])
# Sun, 16 Jul 2017 20:01:09
ys
#[Out]# array([[[4, 4],
#[Out]#         [4, 4],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[5, 5],
#[Out]#         [5, 5],
#[Out]#         [5, 5]],
#[Out]# 
#[Out]#        [[6, 6],
#[Out]#         [6, 6],
#[Out]#         [6, 6]]])
# Sun, 16 Jul 2017 20:01:47
xs,ys,zs = np.meshgrid([1,2,3],[7,8],[4,5,6])
# Sun, 16 Jul 2017 20:01:48
xs
#[Out]# array([[[1, 1, 1],
#[Out]#         [2, 2, 2],
#[Out]#         [3, 3, 3]],
#[Out]# 
#[Out]#        [[1, 1, 1],
#[Out]#         [2, 2, 2],
#[Out]#         [3, 3, 3]]])
# Sun, 16 Jul 2017 20:01:50
ys
#[Out]# array([[[7, 7, 7],
#[Out]#         [7, 7, 7],
#[Out]#         [7, 7, 7]],
#[Out]# 
#[Out]#        [[8, 8, 8],
#[Out]#         [8, 8, 8],
#[Out]#         [8, 8, 8]]])
# Sun, 16 Jul 2017 20:01:54
zs
#[Out]# array([[[4, 5, 6],
#[Out]#         [4, 5, 6],
#[Out]#         [4, 5, 6]],
#[Out]# 
#[Out]#        [[4, 5, 6],
#[Out]#         [4, 5, 6],
#[Out]#         [4, 5, 6]]])
# Sun, 16 Jul 2017 20:10:12
xs
#[Out]# array([[[1, 1, 1],
#[Out]#         [2, 2, 2],
#[Out]#         [3, 3, 3]],
#[Out]# 
#[Out]#        [[1, 1, 1],
#[Out]#         [2, 2, 2],
#[Out]#         [3, 3, 3]]])
# Sun, 16 Jul 2017 20:10:22
xs,ys = np.meshgrid([1,2,3],[1,2,3])
# Sun, 16 Jul 2017 20:10:23
xs
#[Out]# array([[1, 2, 3],
#[Out]#        [1, 2, 3],
#[Out]#        [1, 2, 3]])
# Sun, 16 Jul 2017 20:10:25
xs[0]
#[Out]# array([1, 2, 3])
# Sun, 16 Jul 2017 20:13:28
np.zeros((1,2,3))
#[Out]# array([[[ 0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.]]])
# Sun, 16 Jul 2017 20:13:34
np.zeros((2,3,4))
#[Out]# array([[[ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.],
#[Out]#         [ 0.,  0.,  0.,  0.]]])
# Sun, 16 Jul 2017 20:14:02
np.zeros((2,3,4))[0]
#[Out]# array([[ 0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.]])
# Sun, 16 Jul 2017 21:03:26
x,y,z = np.meshgrid([100,200],[1,2,3,4],[10,20,30,40])
# Sun, 16 Jul 2017 21:03:27
x
#[Out]# array([[[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]]])
# Sun, 16 Jul 2017 21:03:36
y
#[Out]# array([[[1, 1, 1, 1],
#[Out]#         [1, 1, 1, 1]],
#[Out]# 
#[Out]#        [[2, 2, 2, 2],
#[Out]#         [2, 2, 2, 2]],
#[Out]# 
#[Out]#        [[3, 3, 3, 3],
#[Out]#         [3, 3, 3, 3]],
#[Out]# 
#[Out]#        [[4, 4, 4, 4],
#[Out]#         [4, 4, 4, 4]]])
# Sun, 16 Jul 2017 21:03:37
z
#[Out]# array([[[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]]])
# Sun, 16 Jul 2017 21:03:47
x[0]
#[Out]# array([[100, 100, 100, 100],
#[Out]#        [200, 200, 200, 200]])
# Sun, 16 Jul 2017 21:03:59
z,y,x = np.meshgrid([100,200],[1,2,3,4],[10,20,30,40])
# Sun, 16 Jul 2017 21:04:00
z
#[Out]# array([[[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]],
#[Out]# 
#[Out]#        [[100, 100, 100, 100],
#[Out]#         [200, 200, 200, 200]]])
# Sun, 16 Jul 2017 21:04:07
y
#[Out]# array([[[1, 1, 1, 1],
#[Out]#         [1, 1, 1, 1]],
#[Out]# 
#[Out]#        [[2, 2, 2, 2],
#[Out]#         [2, 2, 2, 2]],
#[Out]# 
#[Out]#        [[3, 3, 3, 3],
#[Out]#         [3, 3, 3, 3]],
#[Out]# 
#[Out]#        [[4, 4, 4, 4],
#[Out]#         [4, 4, 4, 4]]])
# Sun, 16 Jul 2017 21:04:08
x
#[Out]# array([[[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]],
#[Out]# 
#[Out]#        [[10, 20, 30, 40],
#[Out]#         [10, 20, 30, 40]]])
# Sun, 16 Jul 2017 21:04:34
x,y,z = np.meshgrid([1,2,3,4],[10,20,30,40],[100,200])
# Sun, 16 Jul 2017 21:04:35
x
#[Out]# array([[[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]]])
# Sun, 16 Jul 2017 21:04:38
y
#[Out]# array([[[10, 10],
#[Out]#         [10, 10],
#[Out]#         [10, 10],
#[Out]#         [10, 10]],
#[Out]# 
#[Out]#        [[20, 20],
#[Out]#         [20, 20],
#[Out]#         [20, 20],
#[Out]#         [20, 20]],
#[Out]# 
#[Out]#        [[30, 30],
#[Out]#         [30, 30],
#[Out]#         [30, 30],
#[Out]#         [30, 30]],
#[Out]# 
#[Out]#        [[40, 40],
#[Out]#         [40, 40],
#[Out]#         [40, 40],
#[Out]#         [40, 40]]])
# Sun, 16 Jul 2017 21:04:39
z
#[Out]# array([[[100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200]],
#[Out]# 
#[Out]#        [[100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200]],
#[Out]# 
#[Out]#        [[100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200]],
#[Out]# 
#[Out]#        [[100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200],
#[Out]#         [100, 200]]])
# Sun, 16 Jul 2017 21:04:42
x
#[Out]# array([[[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]]])
# Sun, 16 Jul 2017 21:04:45
x,y,z = np.meshgrid([1,2,3,4],[10,20,30,40],[100,200])
# Sun, 16 Jul 2017 21:25:37
x,y,z = np.meshgrid([1,2,3,4],[100,200],




)
# Sun, 16 Jul 2017 21:25:43
x
#[Out]# array([[[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]],
#[Out]# 
#[Out]#        [[1, 1],
#[Out]#         [2, 2],
#[Out]#         [3, 3],
#[Out]#         [4, 4]]])
# Sun, 16 Jul 2017 21:25:46
len(x)
#[Out]# 4
# Sun, 16 Jul 2017 21:25:47
size(x)
# Sun, 16 Jul 2017 21:25:52
x.size
#[Out]# 32
# Sun, 16 Jul 2017 21:25:54
x.len
# Sun, 16 Jul 2017 21:25:58
x.dim
# Sun, 16 Jul 2017 21:26:01
dim(x)
# Sun, 16 Jul 2017 21:26:21
x.shape
#[Out]# (4, 4, 2)
# Sun, 16 Jul 2017 21:26:29
np.zeros(x.shape)
#[Out]# array([[[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]]])
# Sun, 16 Jul 2017 21:28:45
x,y = np.meshgrid([1,2,3,4],[10,20,30,40])
# Sun, 16 Jul 2017 21:28:46
x
#[Out]# array([[1, 2, 3, 4],
#[Out]#        [1, 2, 3, 4],
#[Out]#        [1, 2, 3, 4],
#[Out]#        [1, 2, 3, 4]])
# Sun, 16 Jul 2017 21:28:47
y
#[Out]# array([[10, 10, 10, 10],
#[Out]#        [20, 20, 20, 20],
#[Out]#        [30, 30, 30, 30],
#[Out]#        [40, 40, 40, 40]])
# Sun, 16 Jul 2017 21:29:04
x[0]
#[Out]# array([1, 2, 3, 4])
# Sun, 16 Jul 2017 21:29:07
x[0][0]
#[Out]# 1
# Sun, 16 Jul 2017 21:29:13
y[0][0]
#[Out]# 10
# Sun, 16 Jul 2017 21:29:16
x[0][1]
#[Out]# 2
# Sun, 16 Jul 2017 21:29:22
y[0][1]
#[Out]# 10
# Sun, 16 Jul 2017 21:33:19
sc
#[Out]# <Nowack_Lab.Procedures.scanplane.Scanplane at 0x11d11e48>
# Sun, 16 Jul 2017 21:33:22
sc.filename
#[Out]# '2017-07-16_184246_Scanplane'
# Sun, 16 Jul 2017 21:34:42
np
#[Out]# <module 'numpy' from 'C:\\Anaconda3\\lib\\site-packages\\numpy\\__init__.py'>
# Sun, 16 Jul 2017 21:34:57
np.chararray(x.shape)
#[Out]# chararray([[b'\x8c', b'1', b'\xc6', b'\x18'],
#[Out]#            [b'c', '', b'o', b'@'],
#[Out]#            [b'\xe5', b'\xa7', b's', b'L'],
#[Out]#            [b'\\', b'\x9b', b'\xb2', b'?']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:14
np.chararray(x.shape)
#[Out]# chararray([['', '', '', ''],
#[Out]#            ['', '', b'j', b'@'],
#[Out]#            ['', '', '', ''],
#[Out]#            ['', b'\x10', b'w', b'@']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:17
np.chararray(x.shape)
#[Out]# chararray([[b'\xc0', '', b'0', b'\x04'],
#[Out]#            [b'\xea', b'\x18', b'\xff', b'?'],
#[Out]#            [b'\x18', b'\xfa', b'W', b'\x07'],
#[Out]#            [b'\xd2', b'6', b'\x9f', b'@']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:18
np.chararray(x.shape)
#[Out]# chararray([[b'\xa4', '', b'\xca', b'\xe4'],
#[Out]#            [b'#', b'\xdc', b'A', b'@'],
#[Out]#            [b'\xd2', b'\xfe', b'w', b'\x01'],
#[Out]#            [b'*', b'N', b't', b'@']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:18
np.chararray(x.shape)
#[Out]# chararray([['', '', '', ''],
#[Out]#            ['', '', b'\xf0', b'\x7f'],
#[Out]#            ['', '', '', ''],
#[Out]#            ['', '', b'\xf0', b'\x7f']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:19
np.chararray(x.shape)
#[Out]# chararray([['', '', '', ''],
#[Out]#            ['', '', b'\xf0', b'\x7f'],
#[Out]#            ['', '', '', ''],
#[Out]#            ['', '', b'\xf0', b'\x7f']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:22
x.shape
#[Out]# (4, 4)
# Sun, 16 Jul 2017 21:35:30
a = np.chararray(x.shape)
# Sun, 16 Jul 2017 21:35:30
a
#[Out]# chararray([['', '', '', ''],
#[Out]#            ['', '', b'?', b'@'],
#[Out]#            [b'\xcc', b'\xcc', b'\xcc', b'\xcc'],
#[Out]#            [b'\xcc', b'\xcc', b'\x1e', b'\xc0']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:33
a[0]
#[Out]# chararray(['', '', '', ''],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:37
a[0][0]
#[Out]# ''
# Sun, 16 Jul 2017 21:35:41
a[0][0] = 'hello'
# Sun, 16 Jul 2017 21:35:42
a
#[Out]# chararray([[b'h', '', '', ''],
#[Out]#            ['', '', b'?', b'@'],
#[Out]#            [b'\xcc', b'\xcc', b'\xcc', b'\xcc'],
#[Out]#            [b'\xcc', b'\xcc', b'\x1e', b'\xc0']],
#[Out]#           dtype='|S1')
# Sun, 16 Jul 2017 21:35:48
a[0][0]
#[Out]# b'h'
# Sun, 16 Jul 2017 21:35:52
a[0][1]
#[Out]# ''
# Sun, 16 Jul 2017 21:35:56
a[1][]
# Sun, 16 Jul 2017 21:35:58
a[1][0]
#[Out]# ''
# Sun, 16 Jul 2017 21:44:06
import Nowack_Lab.Procedures.vibration
# Sun, 16 Jul 2017 21:44:14
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:44:18
v = Vibration
# Sun, 16 Jul 2017 21:44:37
pf
#[Out]# <Nowack_Lab.Procedures.planefit.Planefit at 0x13b30898>
# Sun, 16 Jul 2017 21:46:17
v = Vibration(pf, liC.R, instruments=instruments,np.linspace(225,325,
))
# Sun, 16 Jul 2017 21:46:24
np.linspace(225,325,100)
#[Out]# array([ 225.        ,  226.01010101,  227.02020202,  228.03030303,
#[Out]#         229.04040404,  230.05050505,  231.06060606,  232.07070707,
#[Out]#         233.08080808,  234.09090909,  235.1010101 ,  236.11111111,
#[Out]#         237.12121212,  238.13131313,  239.14141414,  240.15151515,
#[Out]#         241.16161616,  242.17171717,  243.18181818,  244.19191919,
#[Out]#         245.2020202 ,  246.21212121,  247.22222222,  248.23232323,
#[Out]#         249.24242424,  250.25252525,  251.26262626,  252.27272727,
#[Out]#         253.28282828,  254.29292929,  255.3030303 ,  256.31313131,
#[Out]#         257.32323232,  258.33333333,  259.34343434,  260.35353535,
#[Out]#         261.36363636,  262.37373737,  263.38383838,  264.39393939,
#[Out]#         265.4040404 ,  266.41414141,  267.42424242,  268.43434343,
#[Out]#         269.44444444,  270.45454545,  271.46464646,  272.47474747,
#[Out]#         273.48484848,  274.49494949,  275.50505051,  276.51515152,
#[Out]#         277.52525253,  278.53535354,  279.54545455,  280.55555556,
#[Out]#         281.56565657,  282.57575758,  283.58585859,  284.5959596 ,
#[Out]#         285.60606061,  286.61616162,  287.62626263,  288.63636364,
#[Out]#         289.64646465,  290.65656566,  291.66666667,  292.67676768,
#[Out]#         293.68686869,  294.6969697 ,  295.70707071,  296.71717172,
#[Out]#         297.72727273,  298.73737374,  299.74747475,  300.75757576,
#[Out]#         301.76767677,  302.77777778,  303.78787879,  304.7979798 ,
#[Out]#         305.80808081,  306.81818182,  307.82828283,  308.83838384,
#[Out]#         309.84848485,  310.85858586,  311.86868687,  312.87878788,
#[Out]#         313.88888889,  314.8989899 ,  315.90909091,  316.91919192,
#[Out]#         317.92929293,  318.93939394,  319.94949495,  320.95959596,
#[Out]#         321.96969697,  322.97979798,  323.98989899,  325.        ])
# Sun, 16 Jul 2017 21:46:29
np.linspace(225,325,10)
#[Out]# array([ 225.        ,  236.11111111,  247.22222222,  258.33333333,
#[Out]#         269.44444444,  280.55555556,  291.66666667,  302.77777778,
#[Out]#         313.88888889,  325.        ])
# Sun, 16 Jul 2017 21:46:32
np.linspace(225,325,11)
#[Out]# array([ 225.,  235.,  245.,  255.,  265.,  275.,  285.,  295.,  305.,
#[Out]#         315.,  325.])
# Sun, 16 Jul 2017 21:46:36
np.linspace(225,325,21)
#[Out]# array([ 225.,  230.,  235.,  240.,  245.,  250.,  255.,  260.,  265.,
#[Out]#         270.,  275.,  280.,  285.,  290.,  295.,  300.,  305.,  310.,
#[Out]#         315.,  320.,  325.])
# Sun, 16 Jul 2017 21:47:09
np.linspace(222,322,21)
#[Out]# array([ 222.,  227.,  232.,  237.,  242.,  247.,  252.,  257.,  262.,
#[Out]#         267.,  272.,  277.,  282.,  287.,  292.,  297.,  302.,  307.,
#[Out]#         312.,  317.,  322.])
# Sun, 16 Jul 2017 21:48:31
np.linspace(25,65,11)
#[Out]# array([ 25.,  29.,  33.,  37.,  41.,  45.,  49.,  53.,  57.,  61.,  65.])
# Sun, 16 Jul 2017 21:48:44
np.linspace(25,65,9)
#[Out]# array([ 25.,  30.,  35.,  40.,  45.,  50.,  55.,  60.,  65.])
# Sun, 16 Jul 2017 21:48:51
9*11
#[Out]# 99
# Sun, 16 Jul 2017 21:50:32
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:50:35
v.run()
# Sun, 16 Jul 2017 21:51:15
from importlib import reload
# Sun, 16 Jul 2017 21:51:26
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:51:30
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:51:35
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:51:37
v.run()
# Sun, 16 Jul 2017 21:51:55
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:51:58
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:52:00
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:52:03
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:52:05
v.run()
# Sun, 16 Jul 2017 21:52:58
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:53:00
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:53:02
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:53:04
v.run()
# Sun, 16 Jul 2017 21:53:53
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:53:55
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:53:56
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:53:58
v.run()
# Sun, 16 Jul 2017 21:54:30
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:54:31
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:54:34
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:54:35
v.run()
# Sun, 16 Jul 2017 21:56:03
print( (1,2,3))
# Sun, 16 Jul 2017 21:56:06
print( *(1,2,3))
# Sun, 16 Jul 2017 21:56:18
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 21:56:20
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 21:56:23
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 21:56:25
v.run()
# Sun, 16 Jul 2017 22:01:19
spectrum
# Sun, 16 Jul 2017 22:01:33
help(plt.close)
# Sun, 16 Jul 2017 22:03:49
a = np.array([1,2,3,4])
# Sun, 16 Jul 2017 22:03:57
b = np.array([1,2,3,4])
# Sun, 16 Jul 2017 22:03:58
a==b
#[Out]# array([ True,  True,  True,  True], dtype=bool)
# Sun, 16 Jul 2017 22:04:07
np.sum(a==b)
#[Out]# 4
# Sun, 16 Jul 2017 22:04:22
np.mean(a==b)
#[Out]# 1.0
# Sun, 16 Jul 2017 22:05:36
b = np.array([1,2,3,5])
# Sun, 16 Jul 2017 22:05:44
np.mean(a==b)
#[Out]# 0.75
# Sun, 16 Jul 2017 22:07:02
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 22:07:06
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 22:07:09
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 22:07:13
v.run()
# Sun, 16 Jul 2017 22:08:24
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 22:08:26
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 22:08:28
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 22:08:34
v.run()
# Sun, 16 Jul 2017 22:10:14
v
#[Out]# <Nowack_Lab.Procedures.vibration.Vibration at 0x3624aba8>
# Sun, 16 Jul 2017 22:10:16
v.Z
#[Out]# array([[ 210.72593577,  210.79248929,  210.85904281,  210.92559633,
#[Out]#          210.99214985,  211.05870337,  211.12525689,  211.19181041,
#[Out]#          211.25836393,  211.32491745,  211.39147097,  211.45802449,
#[Out]#          211.52457801,  211.59113152,  211.65768504,  211.72423856,
#[Out]#          211.79079208,  211.8573456 ,  211.92389912,  211.99045264,
#[Out]#          212.05700616],
#[Out]#        [ 211.1218759 ,  211.18842942,  211.25498294,  211.32153646,
#[Out]#          211.38808998,  211.45464349,  211.52119701,  211.58775053,
#[Out]#          211.65430405,  211.72085757,  211.78741109,  211.85396461,
#[Out]#          211.92051813,  211.98707165,  212.05362517,  212.12017869,
#[Out]#          212.18673221,  212.25328573,  212.31983925,  212.38639277,
#[Out]#          212.45294629],
#[Out]#        [ 211.51781602,  211.58436954,  211.65092306,  211.71747658,
#[Out]#          211.7840301 ,  211.85058362,  211.91713714,  211.98369066,
#[Out]#          212.05024418,  212.1167977 ,  212.18335122,  212.24990474,
#[Out]#          212.31645826,  212.38301178,  212.4495653 ,  212.51611882,
#[Out]#          212.58267234,  212.64922586,  212.71577938,  212.7823329 ,
#[Out]#          212.84888642],
#[Out]#        [ 211.91375615,  211.98030967,  212.04686319,  212.11341671,
#[Out]#          212.17997023,  212.24652375,  212.31307727,  212.37963079,
#[Out]#          212.44618431,  212.51273783,  212.57929135,  212.64584487,
#[Out]#          212.71239839,  212.77895191,  212.84550543,  212.91205895,
#[Out]#          212.97861247,  213.04516599,  213.11171951,  213.17827303,
#[Out]#          213.24482655],
#[Out]#        [ 212.30969628,  212.3762498 ,  212.44280332,  212.50935684,
#[Out]#          212.57591036,  212.64246388,  212.7090174 ,  212.77557092,
#[Out]#          212.84212444,  212.90867796,  212.97523148,  213.041785  ,
#[Out]#          213.10833852,  213.17489204,  213.24144556,  213.30799908,
#[Out]#          213.3745526 ,  213.44110612,  213.50765964,  213.57421316,
#[Out]#          213.64076668],
#[Out]#        [ 212.70563641,  212.77218993,  212.83874345,  212.90529697,
#[Out]#          212.97185049,  213.03840401,  213.10495753,  213.17151105,
#[Out]#          213.23806457,  213.30461809,  213.37117161,  213.43772513,
#[Out]#          213.50427865,  213.57083217,  213.63738569,  213.70393921,
#[Out]#          213.77049273,  213.83704625,  213.90359977,  213.97015329,
#[Out]#          214.0367068 ],
#[Out]#        [ 213.10157654,  213.16813006,  213.23468358,  213.3012371 ,
#[Out]#          213.36779062,  213.43434414,  213.50089766,  213.56745118,
#[Out]#          213.6340047 ,  213.70055822,  213.76711174,  213.83366525,
#[Out]#          213.90021877,  213.96677229,  214.03332581,  214.09987933,
#[Out]#          214.16643285,  214.23298637,  214.29953989,  214.36609341,
#[Out]#          214.43264693],
#[Out]#        [ 213.49751667,  213.56407019,  213.6306237 ,  213.69717722,
#[Out]#          213.76373074,  213.83028426,  213.89683778,  213.9633913 ,
#[Out]#          214.02994482,  214.09649834,  214.16305186,  214.22960538,
#[Out]#          214.2961589 ,  214.36271242,  214.42926594,  214.49581946,
#[Out]#          214.56237298,  214.6289265 ,  214.69548002,  214.76203354,
#[Out]#          214.82858706],
#[Out]#        [ 213.89345679,  213.96001031,  214.02656383,  214.09311735,
#[Out]#          214.15967087,  214.22622439,  214.29277791,  214.35933143,
#[Out]#          214.42588495,  214.49243847,  214.55899199,  214.62554551,
#[Out]#          214.69209903,  214.75865255,  214.82520607,  214.89175959,
#[Out]#          214.95831311,  215.02486663,  215.09142015,  215.15797367,
#[Out]#          215.22452719]])
# Sun, 16 Jul 2017 22:10:27
z[9]
# Sun, 16 Jul 2017 22:10:35
z[8]
# Sun, 16 Jul 2017 22:10:42
v.z
# Sun, 16 Jul 2017 22:10:44
v.Z
#[Out]# array([[ 210.72593577,  210.79248929,  210.85904281,  210.92559633,
#[Out]#          210.99214985,  211.05870337,  211.12525689,  211.19181041,
#[Out]#          211.25836393,  211.32491745,  211.39147097,  211.45802449,
#[Out]#          211.52457801,  211.59113152,  211.65768504,  211.72423856,
#[Out]#          211.79079208,  211.8573456 ,  211.92389912,  211.99045264,
#[Out]#          212.05700616],
#[Out]#        [ 211.1218759 ,  211.18842942,  211.25498294,  211.32153646,
#[Out]#          211.38808998,  211.45464349,  211.52119701,  211.58775053,
#[Out]#          211.65430405,  211.72085757,  211.78741109,  211.85396461,
#[Out]#          211.92051813,  211.98707165,  212.05362517,  212.12017869,
#[Out]#          212.18673221,  212.25328573,  212.31983925,  212.38639277,
#[Out]#          212.45294629],
#[Out]#        [ 211.51781602,  211.58436954,  211.65092306,  211.71747658,
#[Out]#          211.7840301 ,  211.85058362,  211.91713714,  211.98369066,
#[Out]#          212.05024418,  212.1167977 ,  212.18335122,  212.24990474,
#[Out]#          212.31645826,  212.38301178,  212.4495653 ,  212.51611882,
#[Out]#          212.58267234,  212.64922586,  212.71577938,  212.7823329 ,
#[Out]#          212.84888642],
#[Out]#        [ 211.91375615,  211.98030967,  212.04686319,  212.11341671,
#[Out]#          212.17997023,  212.24652375,  212.31307727,  212.37963079,
#[Out]#          212.44618431,  212.51273783,  212.57929135,  212.64584487,
#[Out]#          212.71239839,  212.77895191,  212.84550543,  212.91205895,
#[Out]#          212.97861247,  213.04516599,  213.11171951,  213.17827303,
#[Out]#          213.24482655],
#[Out]#        [ 212.30969628,  212.3762498 ,  212.44280332,  212.50935684,
#[Out]#          212.57591036,  212.64246388,  212.7090174 ,  212.77557092,
#[Out]#          212.84212444,  212.90867796,  212.97523148,  213.041785  ,
#[Out]#          213.10833852,  213.17489204,  213.24144556,  213.30799908,
#[Out]#          213.3745526 ,  213.44110612,  213.50765964,  213.57421316,
#[Out]#          213.64076668],
#[Out]#        [ 212.70563641,  212.77218993,  212.83874345,  212.90529697,
#[Out]#          212.97185049,  213.03840401,  213.10495753,  213.17151105,
#[Out]#          213.23806457,  213.30461809,  213.37117161,  213.43772513,
#[Out]#          213.50427865,  213.57083217,  213.63738569,  213.70393921,
#[Out]#          213.77049273,  213.83704625,  213.90359977,  213.97015329,
#[Out]#          214.0367068 ],
#[Out]#        [ 213.10157654,  213.16813006,  213.23468358,  213.3012371 ,
#[Out]#          213.36779062,  213.43434414,  213.50089766,  213.56745118,
#[Out]#          213.6340047 ,  213.70055822,  213.76711174,  213.83366525,
#[Out]#          213.90021877,  213.96677229,  214.03332581,  214.09987933,
#[Out]#          214.16643285,  214.23298637,  214.29953989,  214.36609341,
#[Out]#          214.43264693],
#[Out]#        [ 213.49751667,  213.56407019,  213.6306237 ,  213.69717722,
#[Out]#          213.76373074,  213.83028426,  213.89683778,  213.9633913 ,
#[Out]#          214.02994482,  214.09649834,  214.16305186,  214.22960538,
#[Out]#          214.2961589 ,  214.36271242,  214.42926594,  214.49581946,
#[Out]#          214.56237298,  214.6289265 ,  214.69548002,  214.76203354,
#[Out]#          214.82858706],
#[Out]#        [ 213.89345679,  213.96001031,  214.02656383,  214.09311735,
#[Out]#          214.15967087,  214.22622439,  214.29277791,  214.35933143,
#[Out]#          214.42588495,  214.49243847,  214.55899199,  214.62554551,
#[Out]#          214.69209903,  214.75865255,  214.82520607,  214.89175959,
#[Out]#          214.95831311,  215.02486663,  215.09142015,  215.15797367,
#[Out]#          215.22452719]])
# Sun, 16 Jul 2017 22:10:47
v.Z[9]
# Sun, 16 Jul 2017 22:10:49
v.Z[8]
#[Out]# array([ 213.89345679,  213.96001031,  214.02656383,  214.09311735,
#[Out]#         214.15967087,  214.22622439,  214.29277791,  214.35933143,
#[Out]#         214.42588495,  214.49243847,  214.55899199,  214.62554551,
#[Out]#         214.69209903,  214.75865255,  214.82520607,  214.89175959,
#[Out]#         214.95831311,  215.02486663,  215.09142015,  215.15797367,
#[Out]#         215.22452719])
# Sun, 16 Jul 2017 22:14:17
help(fig.clf)
# Sun, 16 Jul 2017 22:14:31
fig.clf()
# Sun, 16 Jul 2017 22:14:42
fig.close()


# Sun, 16 Jul 2017 22:14:47
plt.close(fig)
# Sun, 16 Jul 2017 22:15:25
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 22:15:28
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 22:15:32
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 22:15:38
v.run()
# Sun, 16 Jul 2017 22:16:10
reload(Nowack_Lab.Procedures.vibration)
#[Out]# <module 'Nowack_Lab.Procedures.vibration' from 'C:\\Users\\B82A\\Documents\\GitHub\\Nowack_Lab\\Procedures\\vibration.py'>
# Sun, 16 Jul 2017 22:16:11
from Nowack_Lab.Procedures.vibration import Vibration
# Sun, 16 Jul 2017 22:16:13
v = Vibration(pf, liC.R, instruments=instruments, xs=np.linspace(222,322,21), ys=np.linspace(25,65,9),measure_time=.1,averages=1)
# Sun, 16 Jul 2017 22:16:15
v.run()
# Sun, 16 Jul 2017 22:35:50
v
#[Out]# <Nowack_Lab.Procedures.vibration.Vibration at 0x13db8668>
# Sun, 16 Jul 2017 22:35:53
v.freqs
#[Out]# []
# Sun, 16 Jul 2017 22:36:07
v.psdaves
#[Out]# [array([  2.91520547e-04,   3.05214104e-04,   3.77430362e-04, ...,
#[Out]#           1.46590396e-07,   1.25670723e-07,   5.78588016e-08]),
#[Out]#  array([  7.12553992e-04,   9.89243301e-04,   7.79775729e-04, ...,
#[Out]#           1.04444043e-07,   1.40230731e-07,   7.43434486e-08]),
#[Out]#  array([  5.34936314e-04,   9.49634477e-04,   9.08787251e-04, ...,
#[Out]#           4.39278513e-07,   5.11101236e-07,   3.92584427e-07]),
#[Out]#  array([  3.32755544e-04,   8.09712764e-04,   5.26435745e-04, ...,
#[Out]#           2.05274256e-07,   1.17650794e-07,   1.59539271e-07]),
#[Out]#  array([  7.59827352e-04,   1.40613842e-03,   1.59796852e-03, ...,
#[Out]#           2.94926094e-07,   2.17303053e-07,   3.85065618e-08]),
#[Out]#  array([  5.92970251e-04,   7.81249937e-04,   3.94104546e-04, ...,
#[Out]#           1.85109305e-07,   9.64831438e-08,   2.16352377e-08]),
#[Out]#  array([  6.19656144e-04,   8.56187668e-04,   8.47553598e-04, ...,
#[Out]#           3.84978559e-07,   4.53587670e-07,   3.66852148e-07]),
#[Out]#  array([  5.89109128e-05,   8.58690408e-04,   9.64439197e-04, ...,
#[Out]#           1.15868317e-07,   1.98694877e-07,   2.14030334e-07]),
#[Out]#  array([  1.92518531e-03,   2.99008904e-03,   3.22364086e-03, ...,
#[Out]#           1.84276148e-07,   1.08351030e-07,   5.21969208e-08]),
#[Out]#  array([  8.23215006e-04,   1.09095827e-03,   1.80740268e-04, ...,
#[Out]#           2.44322072e-07,   4.13125050e-07,   4.02033091e-07]),
#[Out]#  array([  1.42797334e-03,   1.81446402e-03,   1.60224252e-03, ...,
#[Out]#           5.93291594e-07,   4.89211814e-07,   5.94924578e-08]),
#[Out]#  array([  1.49791800e-04,   9.07777188e-04,   1.43259234e-03, ...,
#[Out]#           5.64757508e-07,   3.70790887e-07,   1.23707123e-07]),
#[Out]#  array([  4.45008186e-04,   1.22830331e-03,   1.64478570e-03, ...,
#[Out]#           1.17102247e-07,   1.58365207e-08,   1.48546756e-09]),
#[Out]#  array([  6.45722000e-04,   9.23459067e-04,   5.32367474e-04, ...,
#[Out]#           1.16019314e-07,   1.59545160e-07,   8.51691635e-08]),
#[Out]#  array([  5.68043732e-04,   7.24234420e-04,   4.66842877e-04, ...,
#[Out]#           4.06338642e-07,   2.16643174e-07,   1.18201184e-07]),
#[Out]#  array([  3.76712098e-04,   7.19818210e-04,   6.40487586e-04, ...,
#[Out]#           6.10110669e-07,   5.77248588e-07,   3.74342708e-07]),
#[Out]#  array([  6.11987675e-04,   6.45220653e-04,   2.07417842e-04, ...,
#[Out]#           1.44916261e-07,   8.09132586e-08,   3.41818384e-08]),
#[Out]#  array([  3.94944304e-04,   6.49271817e-04,   3.09452382e-04, ...,
#[Out]#           2.04054567e-07,   3.23892553e-07,   2.60249381e-07]),
#[Out]#  array([  9.40228863e-04,   1.38760501e-03,   1.18148144e-03, ...,
#[Out]#           7.71138865e-08,   1.82705869e-07,   1.89680708e-07]),
#[Out]#  array([  7.59817035e-04,   9.47782269e-04,   7.15659327e-04, ...,
#[Out]#           3.00177140e-07,   2.61651644e-08,   7.25329141e-08]),
#[Out]#  array([  1.51035903e-04,   4.37053158e-04,   5.70409593e-04, ...,
#[Out]#           2.28055216e-07,   1.02755990e-07,   1.30700871e-08]),
#[Out]#  array([  4.49256428e-04,   9.55640563e-04,   7.99356653e-04, ...,
#[Out]#           8.69284476e-08,   1.38419116e-07,   1.14435976e-07]),
#[Out]#  array([  7.83589122e-04,   8.87365843e-04,   3.99583105e-04, ...,
#[Out]#           1.86760982e-07,   1.16345617e-07,   8.15431850e-08]),
#[Out]#  array([  5.29835930e-04,   9.01301734e-04,   8.22080394e-04, ...,
#[Out]#           1.66533759e-07,   3.77138096e-08,   6.38540283e-08]),
#[Out]#  array([  8.68992259e-04,   1.15560921e-03,   8.57756862e-04, ...,
#[Out]#           4.79054205e-07,   5.07103211e-07,   3.62659624e-07]),
#[Out]#  array([  9.35000885e-04,   1.29288833e-03,   9.73586189e-04, ...,
#[Out]#           3.68870650e-07,   3.39542142e-07,   1.27451574e-07]),
#[Out]#  array([  3.55295092e-04,   1.17557922e-03,   1.21390339e-03, ...,
#[Out]#           1.69993108e-07,   1.10588835e-07,   4.81813709e-08]),
#[Out]#  array([  7.67588750e-04,   1.05527161e-03,   5.13975202e-04, ...,
#[Out]#           2.45750756e-07,   2.43577540e-07,   5.13016900e-08]),
#[Out]#  array([  8.58855608e-04,   1.73988866e-03,   1.18360403e-03, ...,
#[Out]#           5.08667797e-07,   3.63805181e-07,   1.58334252e-07]),
#[Out]#  array([  3.48736736e-04,   2.32542684e-03,   2.36525611e-03, ...,
#[Out]#           3.11944898e-07,   4.51130982e-07,   3.20948442e-07]),
#[Out]#  array([  1.36557873e-04,   3.47901672e-03,   4.62233232e-03, ...,
#[Out]#           3.11097622e-07,   3.93745577e-07,   2.86216460e-07]),
#[Out]#  array([  1.03935822e-03,   7.20824830e-04,   2.01959589e-03, ...,
#[Out]#           3.79185393e-07,   4.26390176e-07,   2.55157696e-07]),
#[Out]#  array([  1.51595948e-03,   2.29249535e-03,   2.32378673e-03, ...,
#[Out]#           2.84722614e-07,   3.17730652e-07,   1.06640270e-07]),
#[Out]#  array([  1.19988710e-04,   1.26188766e-03,   1.13992496e-03, ...,
#[Out]#           8.58959323e-08,   2.61350685e-08,   2.34884729e-08]),
#[Out]#  array([  6.96854577e-04,   1.14700155e-03,   6.24042116e-04, ...,
#[Out]#           2.71906227e-07,   3.14988737e-07,   2.29512889e-07]),
#[Out]#  array([  5.87680439e-04,   1.12115748e-03,   1.11247343e-03, ...,
#[Out]#           1.18640655e-07,   2.38881913e-07,   2.07561480e-07]),
#[Out]#  array([  6.48152198e-05,   7.99831120e-04,   7.15575725e-04, ...,
#[Out]#           1.97396529e-07,   4.47368806e-07,   3.91133288e-07]),
#[Out]#  array([  8.13483423e-04,   1.03958575e-03,   5.84207686e-04, ...,
#[Out]#           3.31075456e-07,   1.88193570e-07,   1.20684599e-07]),
#[Out]#  array([  3.07431046e-04,   1.44220006e-03,   1.31955732e-03, ...,
#[Out]#           2.96782642e-08,   1.11618134e-07,   1.27149643e-07]),
#[Out]#  array([  5.58795553e-04,   1.15370227e-03,   1.15524211e-03, ...,
#[Out]#           3.18096567e-08,   1.86440038e-07,   1.74988784e-07]),
#[Out]#  array([  9.89719107e-05,   1.29022107e-03,   1.09843909e-03, ...,
#[Out]#           1.93755397e-07,   2.18598794e-07,   1.17978084e-07]),
#[Out]#  array([  1.06224718e-03,   1.20298846e-03,   5.19343868e-04, ...,
#[Out]#           2.11419155e-07,   2.77376582e-07,   1.95603170e-07]),
#[Out]#  array([  1.68735956e-03,   2.19828924e-03,   1.45201354e-03, ...,
#[Out]#           3.80087098e-07,   3.69117260e-07,   2.35120495e-07]),
#[Out]#  array([  9.30013756e-04,   1.49390653e-03,   1.11159928e-03, ...,
#[Out]#           1.31638422e-07,   1.21530729e-07,   9.96077073e-08]),
#[Out]#  array([  8.36749084e-04,   9.69778728e-04,   7.47546099e-04, ...,
#[Out]#           1.62166927e-07,   4.21695883e-07,   3.86604043e-07]),
#[Out]#  array([  1.25707744e-03,   1.43886836e-03,   5.29621344e-04, ...,
#[Out]#           2.09847794e-07,   1.27292421e-07,   1.70921530e-08]),
#[Out]#  array([  5.80959349e-04,   9.96207894e-04,   7.94143932e-04, ...,
#[Out]#           3.38801860e-07,   3.23756863e-07,   1.33441780e-07]),
#[Out]#  array([  7.27789084e-04,   1.23076872e-03,   1.10726774e-03, ...,
#[Out]#           3.69809697e-07,   7.84000552e-08,   3.37760779e-08]),
#[Out]#  array([  1.94361681e-04,   9.07699249e-04,   7.57725348e-04, ...,
#[Out]#           2.01007007e-07,   2.89882259e-07,   1.91679995e-07]),
#[Out]#  array([  1.11040942e-03,   1.47941693e-03,   6.07567638e-04, ...,
#[Out]#           8.77491331e-08,   5.77873034e-08,   2.29685538e-09]),
#[Out]#  array([  1.61239279e-05,   5.05901701e-03,   4.55972543e-03, ...,
#[Out]#           4.70047277e-07,   3.60845395e-07,   2.84706882e-07]),
#[Out]#  array([  3.50920726e-03,   4.91278991e-03,   1.68227854e-03, ...,
#[Out]#           4.75707466e-07,   3.47608946e-07,   1.59830802e-07]),
#[Out]#  array([  2.51180164e-03,   5.39642784e-03,   3.68812709e-03, ...,
#[Out]#           3.12008149e-07,   2.34620840e-07,   3.23708807e-08]),
#[Out]#  array([  7.00431018e-04,   8.27084514e-04,   1.97835682e-03, ...,
#[Out]#           2.25653957e-07,   4.33349337e-07,   3.86777394e-07]),
#[Out]#  array([  8.63322523e-04,   1.00898629e-03,   5.61912743e-04, ...,
#[Out]#           2.82755812e-07,   2.81345389e-07,   1.80144347e-07]),
#[Out]#  array([  4.66068768e-04,   1.23351807e-03,   1.21583632e-03, ...,
#[Out]#           2.34995638e-07,   2.89513365e-07,   1.98326004e-07]),
#[Out]#  array([  1.79588170e-04,   3.16571315e-04,   2.70716235e-04, ...,
#[Out]#           2.08590228e-07,   1.81536081e-07,   5.89793218e-08]),
#[Out]#  array([  4.87728124e-04,   6.75738238e-04,   5.03820478e-04, ...,
#[Out]#           2.29818650e-07,   8.09060585e-08,   7.30165534e-09]),
#[Out]#  array([  6.01050273e-04,   9.05623759e-04,   2.86294289e-04, ...,
#[Out]#           6.38494915e-07,   6.08546925e-07,   4.04942089e-07]),
#[Out]#  array([  1.14279219e-03,   1.29173141e-03,   4.25651184e-04, ...,
#[Out]#           3.25599396e-07,   3.23407497e-07,   1.00661258e-07]),
#[Out]#  array([  3.10697461e-04,   4.49316285e-04,   3.21735564e-04, ...,
#[Out]#           1.61900686e-07,   2.11536314e-07,   1.51185669e-07]),
#[Out]#  array([  4.07031867e-04,   1.02630191e-03,   1.18757761e-03, ...,
#[Out]#           3.92392387e-07,   3.58156028e-07,   2.13638323e-07]),
#[Out]#  array([  3.77309241e-04,   7.29611004e-04,   1.29911694e-04, ...,
#[Out]#           1.74472255e-07,   2.26587595e-07,   1.65147519e-07]),
#[Out]#  array([  7.31703786e-04,   1.00344993e-03,   9.77111735e-04, ...,
#[Out]#           7.43189320e-09,   2.89602311e-07,   2.88612953e-07]),
#[Out]#  array([  2.45609398e-05,   6.11712180e-04,   6.43625454e-04, ...,
#[Out]#           1.14107665e-07,   8.72301223e-08,   1.16405099e-08]),
#[Out]#  array([  3.55418775e-04,   8.74847275e-04,   8.93326517e-04, ...,
#[Out]#           2.34600659e-07,   1.20141098e-07,   1.03627675e-07]),
#[Out]#  array([  5.57926597e-05,   5.09774184e-04,   6.41103790e-04, ...,
#[Out]#           2.66595104e-07,   3.13198727e-07,   4.84779933e-08]),
#[Out]#  array([  4.29316897e-04,   7.67086105e-04,   8.91227014e-04, ...,
#[Out]#           4.12398236e-08,   2.26254282e-07,   2.27218465e-07]),
#[Out]#  array([  2.24413315e-04,   2.51880568e-04,   5.82590846e-05, ...,
#[Out]#           3.97564324e-07,   3.51847049e-07,   7.35152433e-08]),
#[Out]#  array([  3.28118590e-04,   1.86258739e-03,   1.47775687e-03, ...,
#[Out]#           1.80683608e-07,   1.66496352e-07,   9.75402341e-08]),
#[Out]#  array([  1.45420659e-03,   2.22097012e-03,   2.39103442e-03, ...,
#[Out]#           4.11820170e-07,   5.17833355e-07,   1.97249674e-07]),
#[Out]#  array([  3.90688772e-04,   2.54528993e-03,   3.51625419e-03, ...,
#[Out]#           1.89996505e-07,   1.79322437e-07,   2.22271367e-09]),
#[Out]#  array([  3.91710789e-04,   2.00673364e-03,   2.49403532e-03, ...,
#[Out]#           3.52198809e-07,   3.79157996e-07,   2.20245616e-07]),
#[Out]#  array([  4.14520331e-03,   5.94767002e-03,   3.37825623e-03, ...,
#[Out]#           2.13198358e-07,   1.64540830e-07,   2.85810445e-08]),
#[Out]#  array([  4.16106281e-03,   5.89722486e-03,   2.25819452e-03, ...,
#[Out]#           2.82854115e-07,   1.54119736e-07,   1.04928859e-07]),
#[Out]#  array([  2.14718376e-03,   2.95701050e-03,   3.20812290e-03, ...,
#[Out]#           2.53864788e-07,   4.59113588e-07,   4.35957730e-07]),
#[Out]#  array([  1.77917985e-04,   2.95954206e-04,   7.51086737e-04, ...,
#[Out]#           1.34933602e-07,   4.39187752e-08,   5.95044881e-08]),
#[Out]#  array([  2.94588928e-04,   9.48827433e-04,   8.84466436e-04, ...,
#[Out]#           2.42725378e-07,   3.38479902e-07,   2.36325814e-07]),
#[Out]#  array([  2.52613915e-04,   3.56093446e-04,   3.48055348e-04, ...,
#[Out]#           5.65634583e-08,   2.05956788e-08,   2.15469543e-08]),
#[Out]#  array([  4.04055952e-04,   7.14967381e-04,   6.82303880e-04, ...,
#[Out]#           1.57548155e-07,   2.04586167e-07,   1.26589595e-07]),
#[Out]#  array([  4.33485826e-05,   7.05133190e-05,   1.07167967e-04, ...,
#[Out]#           6.44917923e-08,   2.13182898e-07,   2.18872382e-07]),
#[Out]#  array([  1.26485103e-04,   3.94743672e-04,   4.46936207e-04, ...,
#[Out]#           1.96529975e-07,   2.53937708e-07,   2.73335678e-07]),
#[Out]#  array([  1.13991671e-04,   7.02983193e-04,   8.01348617e-04, ...,
#[Out]#           1.55587022e-07,   1.68992276e-07,   1.86669468e-07]),
#[Out]#  array([  1.28701321e-04,   1.40717551e-04,   7.07100802e-05, ...,
#[Out]#           1.34139282e-07,   7.27059183e-08,   8.59890066e-08]),
#[Out]#  array([  1.68438412e-04,   1.25510568e-03,   1.13862880e-03, ...,
#[Out]#           2.61991126e-07,   1.64263753e-07,   6.90461491e-08]),
#[Out]#  array([  6.92630170e-04,   9.70240093e-04,   7.85355069e-04, ...,
#[Out]#           3.07975436e-07,   1.65276187e-07,   1.60011665e-08]),
#[Out]#  array([  6.97897721e-04,   1.04659316e-03,   9.36353685e-04, ...,
#[Out]#           1.24390624e-07,   1.43656400e-07,   1.67135085e-07]),
#[Out]#  array([  9.12320536e-04,   1.56083733e-03,   1.26164367e-03, ...,
#[Out]#           2.42357557e-07,   1.76272749e-07,   4.76465159e-08]),
#[Out]#  array([  1.19672949e-03,   1.46651103e-03,   7.91616094e-04, ...,
#[Out]#           2.32956225e-07,   7.75274202e-08,   3.09785327e-08]),
#[Out]#  array([  4.00449948e-04,   1.09816556e-03,   1.11847132e-03, ...,
#[Out]#           2.57393765e-07,   2.16452296e-07,   1.47251030e-07]),
#[Out]#  array([  7.48973098e-04,   1.63706994e-03,   1.94224212e-03, ...,
#[Out]#           6.03789634e-07,   5.86062027e-07,   3.79614161e-07]),
#[Out]#  array([  3.06847765e-03,   2.13879183e-03,   2.81344244e-03, ...,
#[Out]#           3.48700822e-07,   4.76398082e-07,   3.03334960e-07]),
#[Out]#  array([  2.72857848e-03,   5.00849837e-03,   7.04720089e-03, ...,
#[Out]#           4.31303421e-07,   3.99954421e-07,   2.34790561e-07]),
#[Out]#  array([  4.22402650e-04,   9.38297162e-04,   1.41331497e-03, ...,
#[Out]#           2.45862158e-07,   2.99571152e-07,   2.45874248e-07]),
#[Out]#  array([  2.42352509e-03,   6.71618037e-03,   4.87502158e-03, ...,
#[Out]#           2.19266792e-07,   2.27138028e-07,   1.00998676e-07]),
#[Out]#  array([  1.75143536e-03,   2.37053467e-03,   4.17108758e-03, ...,
#[Out]#           1.68161316e-07,   2.18060598e-07,   1.60846070e-07]),
#[Out]#  array([  1.29903185e-03,   1.71728351e-03,   1.22008087e-03, ...,
#[Out]#           2.52811744e-07,   2.94779356e-07,   2.15638443e-07]),
#[Out]#  array([  1.97786941e-04,   2.08254018e-04,   6.26071881e-04, ...,
#[Out]#           3.91942923e-07,   3.19367651e-07,   2.03536693e-07]),
#[Out]#  array([  8.90210949e-04,   1.22543852e-03,   1.00908785e-03, ...,
#[Out]#           2.50235680e-07,   4.54147139e-07,   3.68688765e-07]),
#[Out]#  array([  3.91054332e-04,   8.61566926e-04,   5.77801739e-04, ...,
#[Out]#           3.11916748e-07,   3.22020988e-07,   2.01928768e-07]),
#[Out]#  array([  4.11537652e-04,   1.21808849e-03,   1.16782653e-03, ...,
#[Out]#           3.59545150e-07,   2.23544478e-07,   6.51555489e-08]),
#[Out]#  array([  7.13289768e-05,   8.16328075e-04,   8.94943036e-04, ...,
#[Out]#           2.82670206e-07,   1.48640614e-07,   3.64856863e-08]),
#[Out]#  array([  1.56807013e-04,   6.02051435e-04,   7.85875152e-04, ...,
#[Out]#           4.32238810e-07,   1.76568989e-07,   4.49770064e-08]),
#[Out]#  array([  6.44330039e-04,   7.54896933e-04,   2.84779462e-04, ...,
#[Out]#           1.86726994e-07,   6.65551559e-08,   1.44611588e-07]),
#[Out]#  array([  2.06427486e-04,   1.47947246e-03,   1.47551239e-03, ...,
#[Out]#           3.27511773e-07,   1.56493211e-07,   4.39633185e-08]),
#[Out]#  array([  6.14869389e-04,   1.02988300e-03,   1.29864091e-03, ...,
#[Out]#           2.55345662e-07,   5.14938797e-07,   4.62733753e-07]),
#[Out]#  array([  3.83624048e-04,   6.15654249e-04,   8.82455968e-04, ...,
#[Out]#           2.55354378e-07,   2.22026795e-07,   1.40088210e-07]),
#[Out]#  array([  1.27560421e-03,   1.77690523e-03,   1.44363141e-03, ...,
#[Out]#           1.23457312e-07,   4.89577387e-08,   9.29415057e-09]),
#[Out]#  array([  4.29705054e-04,   5.58613383e-04,   4.76596377e-04, ...,
#[Out]#           3.18241452e-07,   3.59596466e-07,   2.30318254e-07]),
#[Out]#  array([  9.88906937e-04,   1.49701015e-03,   1.29699829e-03, ...,
#[Out]#           1.08542867e-07,   2.69598216e-07,   2.50781113e-07]),
#[Out]#  array([  9.24909415e-04,   1.33221350e-03,   1.15443876e-03, ...,
#[Out]#           8.05505108e-08,   4.34885694e-08,   6.39356750e-08]),
#[Out]#  array([  1.05786029e-03,   1.51527114e-03,   1.31769772e-03, ...,
#[Out]#           3.35016072e-07,   2.63835239e-07,   3.97913401e-08]),
#[Out]#  array([  1.10690929e-03,   1.70735296e-03,   2.05414379e-03, ...,
#[Out]#           2.47827488e-07,   2.30322592e-07,   1.59462144e-07]),
#[Out]#  array([  3.92124595e-04,   8.22223433e-04,   1.19343054e-03, ...,
#[Out]#           1.61313054e-07,   1.56945417e-07,   1.83623559e-07]),
#[Out]#  array([  2.52585309e-03,   5.06023943e-03,   4.78938780e-03, ...,
#[Out]#           6.26367159e-07,   7.81420691e-07,   6.22438613e-07]),
#[Out]#  array([  8.56389989e-04,   8.72398515e-04,   2.02323881e-03, ...,
#[Out]#           1.44561158e-07,   2.23968804e-07,   1.95505494e-07]),
#[Out]#  array([  1.43505778e-03,   3.07799573e-03,   3.95573160e-03, ...,
#[Out]#           1.95843580e-07,   2.71755055e-07,   2.63057597e-07]),
#[Out]#  array([  2.85129231e-04,   1.00342608e-04,   8.40352189e-04, ...,
#[Out]#           3.17770792e-07,   2.15980175e-07,   9.24371571e-08]),
#[Out]#  array([  4.22814089e-04,   6.22437335e-04,   4.83051633e-04, ...,
#[Out]#           2.20459695e-07,   1.84099714e-07,   5.45392468e-08]),
#[Out]#  array([  5.18474821e-04,   1.05898422e-03,   1.05917154e-03, ...,
#[Out]#           1.88219085e-07,   4.10397852e-07,   3.78310292e-07]),
#[Out]#  array([  4.84003106e-04,   6.18426928e-04,   2.94345222e-04, ...,
#[Out]#           1.28952253e-07,   4.21180506e-08,   9.27938350e-08]),
#[Out]#  array([  1.17415160e-03,   1.43135088e-03,   8.00089968e-04, ...,
#[Out]#           2.83086040e-07,   2.98910731e-07,   2.53663513e-07]),
#[Out]#  array([  1.72984880e-03,   2.21939729e-03,   1.57309485e-03, ...,
#[Out]#           2.84440079e-07,   2.09377267e-07,   5.78116749e-08]),
#[Out]#  array([  7.99768866e-04,   1.86910168e-03,   1.26221182e-03, ...,
#[Out]#           2.02672799e-07,   1.06398597e-07,   9.47918616e-09]),
#[Out]#  array([  3.88156124e-04,   2.72634755e-04,   2.58414773e-04, ...,
#[Out]#           1.33862440e-07,   5.11038332e-08,   2.75518279e-10]),
#[Out]#  array([  3.68387616e-04,   5.69068874e-04,   5.67165241e-04, ...,
#[Out]#           4.36292254e-07,   5.15616148e-07,   3.45387753e-07]),
#[Out]#  array([  1.38460658e-03,   1.90919041e-03,   1.53593170e-03, ...,
#[Out]#           4.20915780e-07,   5.52433392e-07,   4.68264705e-07]),
#[Out]#  array([  1.53902431e-03,   2.13047435e-03,   1.61241547e-03, ...,
#[Out]#           5.84672514e-07,   4.94162156e-07,   3.37820515e-07]),
#[Out]#  array([  1.43990484e-03,   1.60472060e-03,   7.95445127e-04, ...,
#[Out]#           2.84320481e-07,   3.01095571e-07,   1.83843006e-07]),
#[Out]#  array([  7.82291420e-04,   1.08626500e-03,   9.86796215e-04, ...,
#[Out]#           2.38270725e-07,   4.27580380e-07,   8.44095983e-08]),
#[Out]#  array([  3.67018103e-04,   6.27671286e-04,   7.86268772e-04, ...,
#[Out]#           1.96422988e-07,   2.15876448e-07,   9.33760307e-08]),
#[Out]#  array([  2.84333042e-05,   2.63400265e-04,   4.51115433e-04, ...,
#[Out]#           2.73623589e-07,   2.59566309e-07,   6.20859476e-08]),
#[Out]#  array([  4.15997053e-04,   5.30226535e-04,   3.44162528e-04, ...,
#[Out]#           2.22734572e-07,   1.80898549e-07,   9.58532158e-08]),
#[Out]#  array([  9.31610027e-05,   3.70562362e-04,   2.53264680e-04, ...,
#[Out]#           1.33113826e-07,   1.70294900e-07,   1.48133701e-07]),
#[Out]#  array([  1.26537211e-03,   1.39915281e-03,   3.81114350e-04, ...,
#[Out]#           9.59096453e-08,   7.25587809e-08,   5.61536237e-08]),
#[Out]#  array([  9.63047366e-04,   9.85889902e-04,   5.64387080e-04, ...,
#[Out]#           2.87633000e-07,   2.60735009e-07,   1.32188527e-07]),
#[Out]#  array([  9.29433577e-04,   1.09724981e-03,   7.05585409e-04, ...,
#[Out]#           6.80368008e-07,   8.20163339e-07,   6.29654759e-07]),
#[Out]#  array([  1.41966662e-04,   3.93950055e-04,   7.25541281e-04, ...,
#[Out]#           3.06997499e-07,   3.59378889e-07,   2.12331344e-07]),
#[Out]#  array([  2.84933425e-04,   3.80859803e-04,   2.13471126e-04, ...,
#[Out]#           1.16301536e-07,   2.12174089e-07,   7.71950912e-08]),
#[Out]#  array([  6.00804417e-04,   7.45868704e-04,   4.40105886e-04, ...,
#[Out]#           1.45319731e-07,   8.75177884e-08,   9.86340512e-08]),
#[Out]#  array([  1.33950806e-04,   1.70901970e-04,   2.20517175e-04, ...,
#[Out]#           2.44147923e-07,   1.63834198e-07,   7.22271238e-08]),
#[Out]#  array([  7.40838388e-04,   8.07991445e-04,   1.47697122e-04, ...,
#[Out]#           1.49879831e-07,   1.24047888e-07,   8.31791215e-08]),
#[Out]#  array([  8.52217975e-04,   1.20193300e-03,   5.92665714e-04, ...,
#[Out]#           5.02568930e-07,   3.43907779e-07,   1.71409185e-07]),
#[Out]#  array([  3.74182450e-04,   7.98817784e-04,   2.84123736e-04, ...,
#[Out]#           1.09061412e-07,   8.64387318e-08,   1.17321173e-07]),
#[Out]#  array([  7.13176438e-04,   1.00192994e-03,   9.72204814e-04, ...,
#[Out]#           3.87467668e-08,   2.05370401e-07,   2.33609804e-07]),
#[Out]#  array([  7.91366841e-05,   7.39022419e-04,   9.01169799e-04, ...,
#[Out]#           3.70756126e-07,   2.63845374e-07,   8.73557501e-08]),
#[Out]#  array([  5.56384842e-04,   1.06690401e-03,   7.18257711e-04, ...,
#[Out]#           2.66556916e-07,   8.47830746e-08,   7.40899286e-08]),
#[Out]#  array([  1.02797600e-03,   1.51669525e-03,   4.86906522e-04, ...,
#[Out]#           5.00216080e-07,   1.97960188e-07,   3.13064220e-08]),
#[Out]#  array([  1.16137193e-03,   1.51938879e-03,   1.12762513e-03, ...,
#[Out]#           2.02757765e-07,   9.76436516e-08,   1.25921589e-08]),
#[Out]#  array([  4.80482077e-04,   6.95286365e-04,   6.93679117e-04, ...,
#[Out]#           8.88213514e-08,   3.61773302e-07,   3.60932823e-07]),
#[Out]#  array([  1.56454821e-04,   5.93620566e-04,   8.01859516e-04, ...,
#[Out]#           1.72565280e-07,   5.54099703e-08,   1.62387611e-08]),
#[Out]#  array([  4.00558113e-04,   4.16864708e-04,   2.94638203e-04, ...,
#[Out]#           1.72386407e-07,   1.39825101e-07,   3.31044652e-08]),
#[Out]#  array([  3.78029117e-04,   5.57342942e-04,   5.23221259e-04, ...,
#[Out]#           5.22967430e-08,   4.04372992e-08,   4.39903569e-08]),
#[Out]#  array([  3.32899377e-04,   3.82985643e-04,   1.86779786e-04, ...,
#[Out]#           2.16639486e-07,   2.20369425e-07,   1.02939203e-07]),
#[Out]#  array([  6.32700092e-05,   8.73700300e-05,   3.78156638e-05, ...,
#[Out]#           1.74868107e-07,   2.41566090e-07,   2.52740212e-07]),
#[Out]#  array([  1.50610674e-04,   4.19570639e-04,   2.94013386e-04, ...,
#[Out]#           3.07686459e-07,   5.35169605e-07,   4.91174503e-07]),
#[Out]#  array([  3.30709971e-04,   6.66301849e-04,   5.41228798e-04, ...,
#[Out]#           3.21761063e-07,   2.41399662e-07,   2.34259595e-08]),
#[Out]#  array([  6.36826541e-05,   3.90639722e-04,   3.15478524e-04, ...,
#[Out]#           3.70189673e-07,   3.17200716e-07,   1.16262658e-07]),
#[Out]#  array([  1.65659089e-04,   2.78723861e-04,   3.22487600e-04, ...,
#[Out]#           4.46152555e-07,   4.52109822e-07,   3.12013237e-07]),
#[Out]#  array([  2.76286527e-04,   3.06185808e-04,   1.06160906e-04, ...,
#[Out]#           2.37888805e-07,   4.38203523e-07,   4.83749111e-07]),
#[Out]#  array([  8.55968278e-05,   3.58021161e-04,   3.62108702e-04, ...,
#[Out]#           1.86360320e-07,   8.97210828e-08,   4.30666688e-08]),
#[Out]#  array([  4.90941333e-05,   1.95689896e-04,   1.29102947e-04, ...,
#[Out]#           1.08776198e-07,   2.20494933e-07,   2.03933000e-07]),
#[Out]#  array([  3.45783077e-04,   3.68962461e-04,   1.92591835e-04, ...,
#[Out]#           1.35001419e-08,   6.03589482e-08,   5.95847056e-08]),
#[Out]#  array([  4.70002611e-04,   6.46979938e-04,   3.86023862e-04, ...,
#[Out]#           6.90787532e-08,   8.17566015e-08,   5.47841317e-08]),
#[Out]#  array([  2.06685606e-04,   5.06547950e-04,   4.28967983e-04, ...,
#[Out]#           3.47260639e-07,   2.31141265e-07,   7.52904132e-08]),
#[Out]#  array([  1.69537023e-04,   2.36249498e-04,   1.57725534e-04, ...,
#[Out]#           9.30684178e-08,   1.35698286e-07,   9.56613193e-08]),
#[Out]#  array([  1.44234243e-04,   2.40578677e-04,   1.65953042e-04, ...,
#[Out]#           1.12239207e-07,   2.81622047e-07,   3.00619748e-07]),
#[Out]#  array([  4.16106102e-04,   5.09852086e-04,   2.75885466e-04, ...,
#[Out]#           5.52354785e-07,   3.53846174e-07,   1.56985939e-07]),
#[Out]#  array([  1.70654626e-03,   2.33666506e-03,   1.66890383e-03, ...,
#[Out]#           2.60168843e-07,   2.92886552e-07,   2.88361837e-07]),
#[Out]#  array([  3.00353907e-04,   1.35239051e-03,   9.71885728e-04, ...,
#[Out]#           2.75919720e-07,   9.20513022e-08,   6.05189042e-08]),
#[Out]#  array([  2.93324788e-04,   3.01804470e-04,   2.01045249e-04, ...,
#[Out]#           2.87012346e-07,   2.20040653e-07,   1.30933663e-07]),
#[Out]#  array([  4.56685351e-05,   5.19167097e-04,   6.56708521e-04, ...,
#[Out]#           1.52355877e-07,   2.88770252e-07,   2.19563642e-07]),
#[Out]#  array([  4.21470586e-04,   8.38789396e-04,   9.99786818e-04, ...,
#[Out]#           1.80509784e-07,   3.07095730e-07,   2.61330870e-07]),
#[Out]#  array([  2.63540725e-04,   2.59738819e-04,   1.09778702e-04, ...,
#[Out]#           8.10058301e-08,   1.12114600e-07,   8.66549542e-08]),
#[Out]#  array([  1.25859341e-04,   8.60817732e-05,   2.76969871e-04, ...,
#[Out]#           1.85122933e-07,   6.26038704e-07,   5.91074275e-07]),
#[Out]#  array([  2.11361944e-04,   5.41207432e-04,   5.93604432e-04, ...,
#[Out]#           1.71438265e-07,   5.81068736e-08,   6.79016622e-08]),
#[Out]#  array([  2.13917471e-04,   2.82161067e-04,   9.79778662e-05, ...,
#[Out]#           3.58210354e-07,   3.06242016e-07,   1.54625395e-07]),
#[Out]#  array([  1.68394400e-05,   3.48578861e-04,   3.11200766e-04, ...,
#[Out]#           2.95541571e-08,   1.58789516e-07,   1.76629923e-07]),
#[Out]#  array([  3.80513640e-04,   4.77952119e-04,   3.76502347e-04, ...,
#[Out]#           2.98599127e-07,   3.92789040e-07,   3.92013721e-07]),
#[Out]#  array([  9.11179784e-05,   8.62944958e-05,   2.71812451e-05, ...,
#[Out]#           2.23821266e-07,   4.84873432e-08,   1.01640394e-07]),
#[Out]#  array([  1.87586287e-04,   1.99335373e-04,   9.86757055e-05, ...,
#[Out]#           1.37410275e-07,   2.45743838e-07,   2.19951014e-07]),
#[Out]#  array([  3.52885321e-04,   4.15867250e-04,   1.77606134e-04, ...,
#[Out]#           4.34911528e-07,   3.04937924e-07,   1.71523106e-07]),
#[Out]#  array([  3.62958070e-04,   4.88276604e-04,   3.32683535e-04, ...,
#[Out]#           7.04541771e-07,   6.87453237e-07,   4.65613142e-07]),
#[Out]#  array([  3.83697613e-05,   1.40958581e-04,   3.16365280e-04, ...,
#[Out]#           4.05318816e-07,   2.87008603e-07,   2.35513815e-07]),
#[Out]#  array([  1.85416022e-04,   3.53520017e-04,   3.88753412e-04, ...,
#[Out]#           2.28755110e-07,   2.57820539e-07,   7.28284915e-08]),
#[Out]#  array([  2.13547693e-04,   2.98487177e-04,   2.48735666e-04, ...,
#[Out]#           1.73475597e-07,   3.00207523e-07,   2.26937933e-07]),
#[Out]#  array([  2.99544748e-04,   4.30441956e-04,   3.78533533e-04, ...,
#[Out]#           2.07175518e-07,   2.24662866e-07,   1.47106094e-07]),
#[Out]#  array([  2.82589975e-05,   1.33594370e-04,   2.15636794e-04, ...,
#[Out]#           1.55815703e-07,   1.22107990e-07,   8.33469192e-08]),
#[Out]#  array([  2.15351904e-04,   2.82406639e-04,   2.28634521e-04, ...,
#[Out]#           2.14422633e-07,   1.28201311e-07,   2.01840431e-08])]
# Sun, 16 Jul 2017 22:36:21
len(v.psdaves)
#[Out]# 189
# Sun, 16 Jul 2017 22:36:33
9*21
#[Out]# 189
# Sun, 16 Jul 2017 22:36:42
v.filenames
#[Out]# ['2017-07-16_221615_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221621_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221627_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221633_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221639_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221645_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221651_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221657_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221703_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221708_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221714_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221720_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221726_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221732_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221738_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221744_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221750_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221756_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221801_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221807_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221813_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221820_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221826_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221832_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221838_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221843_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221849_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221855_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221901_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221907_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221913_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221919_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221924_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221930_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221936_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221942_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221948_AnnotatedSpectrum',
#[Out]#  '2017-07-16_221954_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222000_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222006_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222011_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222017_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222024_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222030_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222035_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222041_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222047_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222053_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222059_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222105_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222111_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222117_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222123_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222129_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222135_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222141_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222147_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222153_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222159_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222204_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222211_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222216_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222222_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222229_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222234_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222240_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222246_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222252_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222258_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222304_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222310_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222316_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222323_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222329_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222336_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222342_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222348_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222354_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222400_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222406_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222411_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222417_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222423_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222429_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222436_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222441_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222447_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222454_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222459_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222505_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222511_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222517_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222523_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222529_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222536_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222542_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222548_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222554_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222600_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222606_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222612_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222617_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222623_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222629_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222635_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222641_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222647_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222653_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222659_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222705_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222711_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222717_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222723_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222729_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222734_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222740_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222746_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222752_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222758_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222803_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222809_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222815_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222821_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222827_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222833_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222839_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222845_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222851_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222857_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222903_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222909_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222914_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222920_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222926_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222932_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222938_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222944_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222950_AnnotatedSpectrum',
#[Out]#  '2017-07-16_222955_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223001_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223007_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223013_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223019_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223025_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223031_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223037_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223042_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223049_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223055_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223101_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223107_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223113_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223119_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223124_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223130_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223136_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223142_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223148_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223154_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223200_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223206_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223211_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223217_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223223_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223229_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223235_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223241_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223247_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223253_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223259_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223305_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223311_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223316_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223322_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223328_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223334_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223340_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223346_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223352_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223358_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223403_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223409_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223415_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223421_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223427_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223433_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223439_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223445_AnnotatedSpectrum',
#[Out]#  '2017-07-16_223450_AnnotatedSpectrum']
# Sun, 16 Jul 2017 22:36:47
len(v.filenames)
#[Out]# 189
# Sun, 16 Jul 2017 22:36:54
len(v.dc)
#[Out]# 9
# Sun, 16 Jul 2017 22:37:11
v.dc
#[Out]# array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
#[Out]#          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
# Sun, 16 Jul 2017 22:39:26
a = np.array([ [1,2],[3,4]])
# Sun, 16 Jul 2017 22:39:27
a
#[Out]# array([[1, 2],
#[Out]#        [3, 4]])
# Sun, 16 Jul 2017 22:39:33
np.mean(a)
#[Out]# 2.5
# Sun, 16 Jul 2017 22:39:41
(1+2+3+4)/4
#[Out]# 2.5
# Sun, 16 Jul 2017 22:41:22
get_ipython().magic('load -i qtconsole/2017/07/setups/vibration_20170716.py')
# Sun, 16 Jul 2017 22:41:27
get_ipython().magic('load qtconsole/2017/07/setups/vibration_20170716.py')
# Sun, 16 Jul 2017 22:41:42
# %load qtconsole/2017/07/setups/vibration_20170716.py
reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,3),
                ys=np.linspace(25,65,3),
                measure_time=.1,
                averages=1
)
v.run()

# Sun, 16 Jul 2017 22:41:56
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

# Sun, 16 Jul 2017 22:42:59
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

# Sun, 16 Jul 2017 22:46:40
v.dc
#[Out]# array([[-0.41795319,  0.22442838, -0.39163969],
#[Out]#        [-0.64639764,  0.80661694, -0.51710935],
#[Out]#        [-0.38382405, -0.21154773, -0.11891607]])
# Sun, 16 Jul 2017 22:46:45
v.psdaves
#[Out]# [array([  1.60181506e-03,   2.74298929e-03,   2.58833229e-03, ...,
#[Out]#           2.86449602e-07,   4.40897219e-07,   3.57597229e-07]),
#[Out]#  array([  2.60740145e-04,   3.25046823e-03,   4.26839488e-03, ...,
#[Out]#           9.71613606e-08,   2.94641933e-07,   2.82237739e-07]),
#[Out]#  array([  5.02562261e-04,   1.24235888e-03,   1.51153457e-03, ...,
#[Out]#           2.11985330e-07,   2.68183267e-07,   1.71588443e-07]),
#[Out]#  array([  4.10464438e-04,   1.20418378e-03,   1.45014957e-03, ...,
#[Out]#           3.68025158e-07,   2.76266644e-07,   1.47654969e-07]),
#[Out]#  array([  1.41100706e-03,   4.71724510e-03,   4.80125735e-03, ...,
#[Out]#           1.20899455e-07,   1.11337993e-07,   1.15573264e-07]),
#[Out]#  array([  8.69453276e-04,   1.55869239e-03,   1.31456858e-03, ...,
#[Out]#           1.54541994e-07,   2.08157279e-07,   9.32539494e-08]),
#[Out]#  array([  3.53942604e-04,   2.16225864e-04,   1.44175415e-03, ...,
#[Out]#           3.28138053e-07,   3.44016512e-07,   1.62709921e-07]),
#[Out]#  array([  4.52574066e-06,   1.04346586e-04,   1.53862050e-04, ...,
#[Out]#           7.88107554e-08,   1.76031082e-07,   1.19495133e-07]),
#[Out]#  array([  3.10675372e-04,   4.50909886e-04,   2.52750022e-04, ...,
#[Out]#           1.61746872e-07,   1.21352967e-07,   2.79678469e-08])]
# Sun, 16 Jul 2017 22:46:54
len(v.psdaves
)
#[Out]# 9
# Sun, 16 Jul 2017 22:47:01
v.X
#[Out]# array([[ 222.,  272.,  322.],
#[Out]#        [ 222.,  272.,  322.],
#[Out]#        [ 222.,  272.,  322.]])
# Sun, 16 Jul 2017 22:47:02
v.Y
#[Out]# array([[ 25.,  25.,  25.],
#[Out]#        [ 45.,  45.,  45.],
#[Out]#        [ 65.,  65.,  65.]])
# Sun, 16 Jul 2017 22:47:03
v.Z
#[Out]# array([[ 210.72593577,  211.39147097,  212.05700616],
#[Out]#        [ 212.30969628,  212.97523148,  213.64076668],
#[Out]#        [ 213.89345679,  214.55899199,  215.22452719]])
# Sun, 16 Jul 2017 22:47:44
v.positions
#[Out]# [(221.94406279336962, 24.947893943044406, 210.76072943511684),
#[Out]#  (272.03721727879434, 24.947893943044406, 211.37916248404832),
#[Out]#  (321.975886092943, 24.97366186328734, 212.04913163763558),
#[Out]#  (221.96983084850268, 44.91803463958874, 212.2810440411409),
#[Out]#  (271.98568105148576, 44.99533842057362, 212.95101321894163),
#[Out]#  (322.0274224567562, 44.99533842057362, 213.6209824147832),
#[Out]#  (221.99559890366328, 64.99125290792533, 213.90443092615826),
#[Out]#  (271.98568105148576, 64.99125290792533, 214.52286405313964),
#[Out]#  (321.975886092943, 64.96548497259859, 215.21860133947925)]
# Sun, 16 Jul 2017 22:48:21
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

# Sun, 16 Jul 2017 22:51:11
instruments
#[Out]# {'atto': <Nowack_Lab.Instruments.attocube.Attocube at 0xe6ebd68>,
#[Out]#  'daq': <Nowack_Lab.Instruments.nidaq.NIDAQ at 0xc6fdac8>,
#[Out]#  'lockin_cap': <Nowack_Lab.Instruments.lockin.SR830 at 0xc74e7f0>,
#[Out]#  'lockin_squid': <Nowack_Lab.Instruments.lockin.SR830 at 0xc74e978>,
#[Out]#  'montana': <Nowack_Lab.Instruments.montana.Montana at 0xc74ab00>,
#[Out]#  'piezos': <Nowack_Lab.Instruments.piezos.Piezos at 0xc74eb38>,
#[Out]#  'preamp': <Nowack_Lab.Instruments.preamp.SR5113 at 0xc74e5c0>,
#[Out]#  'squidarray': <Nowack_Lab.Instruments.squidarray.SquidArray at 0xe6f1390>}
# Sun, 16 Jul 2017 22:54:51
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

# Sun, 16 Jul 2017 22:56:20
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

# Sun, 16 Jul 2017 22:57:09
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

# Sun, 16 Jul 2017 22:58:43
v.freqs
#[Out]# array([], dtype=float64)
# Sun, 16 Jul 2017 22:59:40
v.psdaves
#[Out]# array([[  1.30896687e-03,   1.82712970e-03,   1.37151997e-03, ...,
#[Out]#           9.47332175e-08,   2.00189457e-07,   2.02322133e-07],
#[Out]#        [  6.18381452e-04,   1.58824460e-03,   2.35047506e-03, ...,
#[Out]#           2.52084672e-07,   3.07766405e-07,   2.27829640e-07],
#[Out]#        [  1.15150860e-03,   1.95343813e-03,   1.60936355e-03, ...,
#[Out]#           2.57930087e-07,   2.41381711e-07,   2.24587489e-08],
#[Out]#        ..., 
#[Out]#        [  1.53498009e-03,   2.31094398e-03,   1.81069772e-03, ...,
#[Out]#           1.78053113e-07,   9.69602528e-08,   2.78382164e-08],
#[Out]#        [  1.91142572e-04,   3.70283642e-04,   2.88506681e-04, ...,
#[Out]#           3.97205976e-07,   2.33488619e-07,   4.24355556e-08],
#[Out]#        [  6.53020155e-05,   1.24492685e-04,   9.45262827e-05, ...,
#[Out]#           1.42339567e-07,   2.05507917e-07,   9.95501953e-08]])
# Sun, 16 Jul 2017 22:59:44
v.filenames
#[Out]# ['2017-07-16_225710_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225716_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225722_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225729_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225735_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225741_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225748_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225754_AnnotatedSpectrum',
#[Out]#  '2017-07-16_225800_AnnotatedSpectrum']
# Sun, 16 Jul 2017 22:59:50
v.positions
#[Out]# array([[ 221.91829474,   24.99942978,  210.68342531],
#[Out]#        [ 271.98568105,   24.97366186,  211.40493053],
#[Out]#        [ 321.97588609,   24.99942978,  212.02336359],
#[Out]#        [ 221.96983085,   45.02110635,  212.30681209],
#[Out]#        [ 272.01144917,   44.99533842,  213.00254931],
#[Out]#        [ 321.97588609,   44.94380257,  213.64675046],
#[Out]#        [ 221.9955989 ,   64.99125291,  213.85289483],
#[Out]#        [ 272.01144917,   64.96548497,  214.52286405],
#[Out]#        [ 322.00165427,   64.99125291,  215.21860134]])
# Sun, 16 Jul 2017 23:00:05
v.X
#[Out]# array([[ 222.,  272.,  322.],
#[Out]#        [ 222.,  272.,  322.],
#[Out]#        [ 222.,  272.,  322.]])
# Sun, 16 Jul 2017 23:00:06
v.Y
#[Out]# array([[ 25.,  25.,  25.],
#[Out]#        [ 45.,  45.,  45.],
#[Out]#        [ 65.,  65.,  65.]])
# Sun, 16 Jul 2017 23:00:09
v.dc
#[Out]# array([[-0.36820738,  0.11367304, -0.41154596],
#[Out]#        [-0.64306189,  0.67678558, -0.51731653],
#[Out]#        [-0.36449294, -0.21860715, -0.12001847]])
# Sun, 16 Jul 2017 23:00:20
np.imshow(v.dc)
# Sun, 16 Jul 2017 23:00:28
plt
#[Out]# <module 'matplotlib.pyplot' from 'C:\\Anaconda3\\lib\\site-packages\\matplotlib\\pyplot.py'>
# Sun, 16 Jul 2017 23:00:31
plt.imshow(v.dc)
#[Out]# <matplotlib.image.AxesImage at 0x3c7d9a20>
