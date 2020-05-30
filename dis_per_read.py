#!/usr/bin/python

import sys
from subprocess import call

print "Usage: dis_per_read.py IDsList RepeatMaskerOut"

try:
    idfile = sys.argv[1]
except:
    idfile = raw_input("Introduce IDsList file: ")

try:
    disfile = sys.argv[2]
except:
    disfile = raw_input("Introduce RepeatMasker out file: ")


ids = open(idfile).readlines()


d=open("dis_script.R","w")
d.write("pdf()")

for id in ids:
	call("grep %s %s > %s"% (id[:-1], disfile, id[:-1]+'disg.txt'),shell=True)
	call("cat head_dis.txt %s > %s"% (id[:-1]+'disg.txt', id[:-1]+'disg_ok.txt'),shell=True)
	code = "\ndis <- read.table('%s',header=TRUE) \nggplot(dis, aes(x=READ, y=DISLOG, label=READ), size=2) + geom_pointrange(mapping = aes(ymin = min(DISLOG), ymax = max(DISLOG)), color='darkseagreen3') + geom_count(show.legend = TRUE, color='darkseagreen3') + theme_light()+ ggtitle('Distances between arrays of %s Family') + xlab('READS') + ylab('Distance in log10(bp)') + geom_point(aes(color=REP), size=3) + scale_color_gradientn(colours = c('pink', 'pink2', 'pink4')) + theme(plot.title = element_text(hjust = 0.5),legend.text=element_text(size=rel(0.7)), legend.position='bottom', legend.key.size = unit(0.3, 'cm'), legend.justification = 'centre', axis.text.x =element_blank(), )"% (id[:-1]+'disg_ok.txt', id[:-1])
	d.write(code)
	
d.write("\ndev.off()")
d.close()
