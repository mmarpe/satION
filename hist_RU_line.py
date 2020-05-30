#!/usr/bin/python

import sys
from subprocess import call

print "Usage: hist_RU_line.py IDsList RepeatMaskerOut FASTA"

try:
    idfile = sys.argv[1]
except:
    idfile = raw_input("Introduce IDsList file: ")

try:
    rmfile = sys.argv[2]
except:
    rmfile = raw_input("Introduce RepeatMasker out file: ")


ids = open(idfile).readlines()

d=open("hist_script_new.R","w")
d.write("pdf()")

for id in ids:
	l=id.split("\t")
	name=l[0]
	length=l[1]
	norm=l[2]
	call("grep %s %s > %s"% (name, rmfile, name+'hist.txt'),shell=True)
	call("cat head3.txt %s > %s"% (name+'hist.txt', name+'hist_ok.txt'),shell=True)
	code = "\ndata <- read.delim('%s', header=TRUE, sep='\t')\ndata$DIS<-factor(data$DIS, levels = c('0nt', '1x','Read', 'Junction_50nt', 'Longer_5000nt')) \nggplot(data, aes(REP))+ geom_freqpoly(aes(colour = DIS),binwidth = 1, size = 1, alpha=0.8)+ scale_color_manual(values = c('#01665e', '#5ab4ac', '#c7eae5','#d8b365','#f6e8c3'))+theme_light()+ labs(fill='Approach', title='%s', x='numberRUs', y='Number of arrays')+ theme(legend.position='top') +guides(fill=guide_legend(title.position='top'))"% (name+'hist_ok.txt', norm[:-1])
	d.write(code)
d.write("\ndev.off()")
d.close()
