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

