import sys
from h5py import *
import numpy

filename = 'dataset.h5'
h5file = File(filename,mode='w')

# 2d surface
h5grp = h5file.create_group('test_surface')

nx = 2
ny = 2
nz = 1

h5grp.attrs['Dimension'] = numpy.string_('XY')
h5grp.attrs['Discretization'] = [1.,1.]
h5grp.attrs['Origin'] = [0.,0.]

rarray = numpy.zeros((nx,ny),'=f8')

rarray[0][0] = 3.e6
rarray[1][0] = 2.e6
rarray[0][1] = 2.e6
rarray[1][1] = 1.e6
h5dset = h5grp.create_dataset('Data', data=rarray)

h5file.close()

print('done')
