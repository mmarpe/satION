#!/usr/bin/python

import sys
from subprocess import call


print "Usage: hist_RU_DIV_lm.py IDsList RepeatMaskerOut FASTA"

try:
    idfile = sys.argv[1]
except:
    idfile = raw_input("Introduce IDsList file: ")

try:
    rmfile = sys.argv[2]
except:
    rmfile = raw_input("Introduce RepeatMasker out file: ")


ids = open(idfile).readlines()


d=open("hist_script.R","w")
d.write("pdf()")

for id in ids:
	l=id.split("\t")
	name=l[0]
	length=l[1]
	norm=l[2]
	call("grep %s %s > %s"% (name, rmfile, name+'hist.txt'),shell=True)
	call("cat head3.txt %s > %s"% (name+'hist.txt', name+'hist_ok.txt'),shell=True)
	code = "\ndata <- read.table('%s', header=TRUE) \nggplot(data, aes(REP))+ geom_point(aes(REP, DIV*%s), size=1, col='mistyrose3') +geom_histogram(binwidth=1, col='#01665e',fill='#01665e', alpha = .4)+ theme_light() + labs(title='%s', x='numberRUs', y='Frequency')  + geom_smooth(aes(REP, DIV*%s),method = 'lm',colour = 'mistyrose4',size = 1) + scale_y_continuous(sec.axis = sec_axis(~./%s, name = 'Kimura divergence []'))"% (name+'hist_ok.txt', norm[:-1], length, norm[:-1], norm[:-1])
	d.write(code)
d.write("\ndev.off()")
d.close()
