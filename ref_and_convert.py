import rsf.api as rsf
import numpy as npy
from bruges.reflection import zoeppritz_rpp as zoep_rpp
import numpy as np
import sys

# Read in logs and calculate rpp
def readrsf(infile):

    f = rsf.Input(infile)
    shape = f.shape()
    data = np.zeros(shape, 'f')
    f.read(data)
    f.close()
    return data.T


if __name__ == "__main__":
    

    vp, vs, rho = [readrsf(f) for f in sys.argv[1:4]]
    vp2, vs2, rho2 = [np.roll(d, 1) for d in (vp, vs, rho)]

    theta = 0
    rpp = zoep_rpp(vp2, vs2, rho2, vp, vs, rho, theta)

    np.save(sys.argv[4], rpp)

    # save seismic as numpy array
    np.save(sys.argv[5], readrsf('seismic.rsf'))
