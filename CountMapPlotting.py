# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:36:28 2016

@author: Metis
"""
import pyfits
import aplpy
import matplotlib.pyplot as plt
import numpy as np

CMAP_file = 'CMAP.fits'
ModelMap_file = 'ModelMap.fits'

cnt = pyfits.open(CMAP_file)[1].data
mod = pyfits.open(ModelMap_file)[1].data
temp_fits = pyfits.open(CMAP_file)
temp_fits[1].data = (cnt-mod)/mod

fig = plt.figure(figsize=(15,5))
f1 = aplpy.FITSFigure(CMAP_file, figure = fig, subplot=(1,3,1))
f2 = aplpy.FITSFigure(ModelMap_file, figure = fig, subplot=(1,3,2))
f3 = aplpy.FITSFigure(temp_fits, figure = fig, subplot=(1,3,3))

f1.add_grid()
f2.add_grid()
f3.add_grid()

f1.grid.set_linestyle('--')
f2.grid.set_linestyle('--')
f3.grid.set_linestyle('--')


f1.tick_labels.set_font(size='smaller')
f2.tick_labels.set_font(size='smaller')
f3.tick_labels.set_font(size='smaller')

f2.axis_labels.hide_y()
f3.axis_labels.hide_y()

f1.axis_labels.hide_x()
f3.axis_labels.hide_x()

f1.tick_labels.set_xformat('ddd')
f2.tick_labels.set_xformat('ddd')
f3.tick_labels.set_xformat('ddd')

f1.tick_labels.set_yformat('ddd')
f2.tick_labels.set_yformat('ddd')
f3.tick_labels.set_yformat('ddd')

f1.show_colorscale(cmap='cubehelix', smooth=1)
f2.show_colorscale(cmap='cubehelix')
f3.show_colorscale(cmap='cubehelix', smooth=1)

f1.add_colorbar()
f2.add_colorbar()
f3.add_colorbar()

f1.colorbar.set_location('top')
f2.colorbar.set_location('top')
f3.colorbar.set_location('top')

f1.colorbar.set_width(0.1)
f2.colorbar.set_width(0.1)
f3.colorbar.set_width(0.1)

f1.colorbar.set_pad(0.03)
f2.colorbar.set_pad(0.03)
f3.colorbar.set_pad(0.03)

f1.colorbar.set_font(size='smaller')
f2.colorbar.set_font(size='smaller')
f3.colorbar.set_font(size='smaller')

f1.set_title('Count Map', y=1.10)
f2.set_title('Model Map', y=1.10)
f3.set_title('Subtract Map', y=1.10)


fig.savefig('All_Model.pdf', dpi=500)

fig.savefig('All_Model.png', dpi=500)
