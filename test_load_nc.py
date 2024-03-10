
# %%

import os
import pprint
import sys

from netCDF4 import Dataset


infile = '/Users/hironorimori/CodeSample/data/WG100-L0AO-PROTO/20240101/20240101000029_VAD_1.nc'

rootgrp = Dataset(infile, 'r')
# pprint.pprint(rootgrp)
# sys.exit()

pprint.pprint(rootgrp.dimensions)
# pprint.pprint(rootgrp.observation_id)
for k in rootgrp.variables.keys():
    print(f'{k = }')
    pprint.pprint(rootgrp[k][0])

    ### Debug
    # sys.exit()







# %%
