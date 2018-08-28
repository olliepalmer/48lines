import os
import glob

root = '/Users/o/Documents/github-root/48lines/'
infolder = 'cornell-movie-dialogs-corpus/'
outfolder = 'out/csvs/'


for file in glob.glob(os.path.join(root,infolder)+'/*.txt'):
	with open(file,encoding='utf8',errors='ignore') as f:
		fname = os.path.split(file)[1].replace('txt','csv')
		outfile = os.path.join(root,outfolder,fname)
		for line in f:
			a = line.replace('"','\'')
			b = '"%s"' % a.replace(' +++$+++ ','","').strip()
			c = b+'\n'
			with open(outfile,'a+') as f2:
				f2.write(c)