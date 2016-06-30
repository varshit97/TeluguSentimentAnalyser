#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 varshit <varshit@varshit-Lenovo>
#
# Distributed under terms of the MIT license.

"""

"""

import os, sys, codecs
reload(sys)
sys.setdefaultencoding("utf-8")

posSynSet = {
        'noun':['NN','NNS','NST','NNP'],
        'pronoun':['PRP'],
        'verb':['VM','VAUX','UT'],
        'adjective':['JJ','QC','QF','QO'],
        'adverb':['RB','INTF'],
        'preposition':['PSP'],
        'conjunction':['CC'],
        'interjection':['INJ'],
        'particle':['RP'],
        'questionverbs':['WQ'],
        'reduplication':['RDP']
        }

with codecs.open('telugu-part-of-speech-tagger/telugu.input.txt','rwa+', encoding = 'utf-8') as f:
    f.truncate()
    for i in sys.argv[1:]:
        f.write(i.decode('utf-8'))
        f.write(" ")

os.system("cd telugu-part-of-speech-tagger; make tag")

with open('telugu-part-of-speech-tagger/telugu.output.txt','r') as myFile:
    output = myFile.read()

output = output.split('\n')
output1 = filter(None, output)

posTag = []

for i in output1:
    tempData = i.split('\t')
    posTag.append([tempData[1],tempData[2]])

for j in posSynSet.values():
    for k in posTag:
        if k[1] in j:
            presIndex = posSynSet.values().index(j)
            k.append(posSynSet.keys()[presIndex])
            
for i in posTag:
    print i[0].decode('utf-8'),i[1],i[2]
