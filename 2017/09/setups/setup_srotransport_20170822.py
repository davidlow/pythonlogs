### Setup script, modified from gmf57.  
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
#import Nowack_Lab.Instruments.lakeshore


from Nowack_Lab.Instruments.lockin          import SR830
#from Nowack_Lab.Instruments.lakeshore       import Lakeshore372

import Nowack_Lab.Procedures.transport

from Nowack_Lab.Procedures.transport        import SimpleRvsTime


# Initialize other measurement equipment
lockin_V1 = SR830(gpib_address=13)
lockin_V2 = SR830(gpib_address=15)
lockin_I = SR830(gpib_address=12)
#lakeshore = Lakeshore372(host='192.168.82.72')

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()


# Create dictionary of instruments for measurements to use
instruments = {
    'lockin_V1' : lockin_V1,
    'lockin_V2' : lockin_V2,
    'lockin_I' : lockin_I,
}
