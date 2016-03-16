# Fermi-Helper-Scripts
A collection of scripts I've found useful for doing Fermi analysis

**Bonne_Projection.py:**

It makes a pretty map projections of Fermi-LAT photon data in galactic coordinates

Takes a Fermi fits file and projects the photon source coordinates into a pseudoconic projection. If the parallel is 90 degrees, this is the Werner projection. If the parallel is 45 degrees, this is the Bonne projection. 

This is mostly not useful, but for some reason the Fermi tool "gtbin" does not support the BON projection (for all-sky images, I've not tried otherwise) despite being in the FITS definitions. It's equal area, but the only reason I use it is because it looks really pretty and it's nice to have on a slide at the end of a talk. Using mpltools and their dark style can fill in the white spots if your colourmap has black at 0.

**Count_Map_Plotting.py:**

A quick way of grabbing a countmap and a modelfile, taking a residual and plotting the three side by side. Uses aplpy for plotting.

**RegionMaker.py:**

Use 
>python RegionMaker.py --help

if you're stuck with this one.

Makes whole-sky region maps for DS9. I was plotting all-sky images for some nice plots, and found that make3FGLxml.py (Fermi user contributed tool) doesn't cut it for region files. I found that instead of plotting the whole 3FGL, I really wanted just the most significant sources in a region file to load into DS9. This is the script I wrote to do it. Note: Required 'gll_psc_v16.fit' from the Fermi Collaboration.

Recommended usage:
>python RegionMaker.py 1000 -assoc True

This seems to give a nice number of sources.
