### Setup script
###
###  +-----------------+
###  |  DO NOT MODIFY  |
###  +-----------------+
###
### Make a copy and rename with today's date
###
### Author: david low (dhl88)

from matplotlib import pyplot as plt
plt.ion()
#plt.style.use("notebook")

import Nowack_Lab.Instruments.lockin
import Nowack_Lab.Instruments.lakeshore


from Nowack_Lab.Instruments.lockin          import SR830
from Nowack_Lab.Instruments.lakeshore       import Lakeshore372

import Nowack_Lab.Procedures.bluefors_vs_T

from Nowack_Lab.Procedures.bluefors_vs_T    import R_vs_T
from Nowack_Lab.Procedures.bluefors_vs_T    import Bluefors_vs_T



# Initialize other measurement equipment
liV = SR830(gpib_address=13)
liI = SR830(gpib_address=15)
lks = Lakeshore372()

# Create dictionary of instruments for measurements to use
instruments = {
    'lockin_I':  liI,
    'lockin_V':  liV,
    'lakeshore': lks
}
