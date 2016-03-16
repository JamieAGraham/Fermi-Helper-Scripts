import pyfits

def make_region(args):
	cat = pyfits.open(args.catalog_name)
	gal = ['bin  ', 'BIN  ', 'glc  ', 'GLC  ', 'hmb  ', 'HMB  ', 'nov  ', 'NOV  ', 'PSR  ', 'psr  ', 'pwn  ', 'PWN  ', 'sfr  ', 'SFR  ', 'snr  ', 'SNR  ', 'spp  ', 'SPP  ']
	exgal = ['agn  ', 'AGN  ', 'bcu  ', 'BCU  ', 'bll  ', 'BLL  ', 'css  ', 'CSS  ', 'fsrq ', 'FSRQ ', 'gal  ', 'GAL  ', 'nlsy1', 'NLSY1', 'rdg  ', 'RDG  ', 'sbg  ', 'SBG  ', 'sey  ', 'SEY  ', 'ssrq ', 'SSRQ ']
	count = 0
	with open(args.outfile, 'w') as f:
		f.write("""# DS9 Region File\n# Sources from 3FGL\n# For issues with script contact Jamie Graham (Durham)\nglobal font="roman 10 normal" move =0\n""")
		for source in cat[1].data:
			if source['Signif_Avg']**2 > args.TS:
				if source['CLASS1'] in gal:
					color = args.gcol
				elif source['CLASS1'] in exgal:
					color = args.excol
				else:
					color = args.unkcol
				if args.assoc == True:
					name = source['ASSOC1']
				else:
					name = source[0]
				f.write("J2000;point(%s,%s) # point = circle 15 color = %s text={%s}\n" % (source['RAJ2000'], source['DEJ2000'], color, name))
				count +=1
	print "Included %i sources, quitting" % count

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description="Makes a region file from the 3FGL FITS catalog using sources with a given TS")
	parser.add_argument('TS', metavar='TS', type=float, help="The TS above which to include sources")
	parser.add_argument('--o', dest = 'outfile', default='full_sky_region.reg', type=str, help="The name of the output file you want to produce")
	parser.add_argument('--i', dest = 'catalog_name', default='gll_psc_v16.fit', type=str, help="The filename / path of gll_psc_v16.fit")
	parser.add_argument('--galactic', dest='gcol', default='green', type=str, help="The colour in which to plot galactic sources")
	parser.add_argument('--exgal', dest='excol', default='magenta', type=str, help="The colour in which to plot extragalactic sources")
	parser.add_argument('--unk', dest='unkcol', default='blue', type=str, help="The colour in which to plot unknown sources")
	parser.add_argument('--assoc', dest='assoc', default=False, type=bool, help="If true, the name will appear as the associated source's ID, as opposed to 3FGL J****.*+****")
	args = parser.parse_args()
	print args
	make_region(args)
	
