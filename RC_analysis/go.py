
import os
import numpy as np


D = os.listdir(".")

for filename in D:
    if filename[0:2] != 'rc': continue


    try: dat = np.loadtxt(filename)
    except: continue

    try: print "%3.2f %s" % (np.median(dat[:,5] * .395), filename)
    except: continue
