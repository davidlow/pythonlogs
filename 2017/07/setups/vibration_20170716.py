reload(Nowack_Lab.Procedures.vibration)
from Nowack_Lab.Procedures.vibration import Vibration

v = Vibration(pf, liC.R, instruments=instruments,
                xs=np.linspace(222,322,21),
                ys=np.linspace(25,65,9),
                measure_time=.1,
                averages=1
)
v.run()
