# IPython log file

get_ipython().magic('load qtconsole/2017/07/setups/startlog_20170703.py')
# Mon, 17 Jul 2017 22:54:19
get_ipython().magic('run -i qtconsole/2017/07/setups/RvsTsetup_20170714.py')
# Mon, 17 Jul 2017 22:54:37
lks.T
#[Out]# {1: 47.671, 2: 3.83386, 3: 4.29301, 5: 4.16381, 6: 4.33829, 7: 0.0, 8: 0.0}
# Mon, 17 Jul 2017 22:54:47
liV.R
#[Out]# 1.13587e-06
# Mon, 17 Jul 2017 22:54:52
liI.R
#[Out]# 9.02572e-07
# Mon, 17 Jul 2017 22:54:59
liI.X
#[Out]# 8.98148e-07
# Mon, 17 Jul 2017 22:55:02
liV.X
#[Out]# 9.59386e-07
# Mon, 17 Jul 2017 22:55:11
liV.X/liI.X
#[Out]# 1.079039774200693
# Mon, 17 Jul 2017 23:00:51
get_ipython().magic('load qtconsole/2017/07/setups/hari_20170714.py')
# Mon, 17 Jul 2017 23:00:53
# %load qtconsole/2017/07/setups/hari_20170714.py
m = R_vs_T(instruments=instruments,
           lakeshore_channel=6,
           meas_dur=43200,
           timestep=10)
m.run()

# Mon, 17 Jul 2017 23:02:36
from Nowack_Lab import set_experiment_data_path
# Mon, 17 Jul 2017 23:02:42
set_experiment_data_path()
# Mon, 17 Jul 2017 23:03:03
get_ipython().magic('load qtconsole/2017/07/setups/hari_20170714.py')
# Mon, 17 Jul 2017 23:03:04
# %load qtconsole/2017/07/setups/hari_20170714.py
m = R_vs_T(instruments=instruments,
           lakeshore_channel=6,
           meas_dur=43200,
           timestep=10)
m.run()

