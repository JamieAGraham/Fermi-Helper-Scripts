from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import pyfits
from matplotlib import colors
from mpltools import style
style.use('dark_background')

datafile = 'gti_photon_events.fits'
outfile = ''

data = pyfits.open(datafile)[1].data
print(len(data))
pos = []

for event in data:
    pos.append([event[3]-180, event[4]])

print("Done loading")
print(len(pos))
def bonne_project(pos, parallel=90, meridian=0):
    pos = np.array(pos)
    p1 = np.deg2rad(parallel)
    mer = np.deg2rad(meridian)
    rho = 1.0/np.tan(p1) + p1 - np.deg2rad(pos[1])
    E = (np.deg2rad(pos[0])-mer)*np.cos(np.deg2rad(pos[1]))/rho
    x = rho*np.sin(E)
    y = 1.0/np.tan(p1) - rho*np.cos(E)
    return np.array([x,y])

print("Projecting")
img = np.array([bonne_project(x) for x in pos]).T
print("Plotting")
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.hist2d(img[0], img[1], bins=500, cmap='cubehelix', norm=colors.LogNorm(), normed=True)
plt.savefig(outfile, dpi=750)
