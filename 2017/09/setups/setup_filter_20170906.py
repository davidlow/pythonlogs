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


from Nowack_Lab.Instruments.lockin          import SR830

import Nowack_Lab.Procedures.transport

from Nowack_Lab.Procedures.transport        import VvsF


# Initialize other measurement equipment
lockin_V = SR830(gpib_address=13)

# Create dictionary of instruments for measurements to use
instruments = {
    'lockin_V' : lockin_V,
}
