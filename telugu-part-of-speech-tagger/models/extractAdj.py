#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 varshit <varshit@varshit-Lenovo>
#
# Distributed under terms of the MIT license.

"""

"""

f = open('telugu.lemma','r')
g = open('adjectives.lemma','w')
for line in f:
    if 'JJ' in line or 'QC' in line or 'QF' in line or 'QO' in line:
        temp = line.split('\t')
        for i in temp:
            if 'JJ' in i or 'QC' in i or 'QF' in i or 'QO' in i:
                if 'JJ' in i:
                    print i.strip().decode('utf-8')
                g.write(i.strip())
                g.write('\n')
f.close()
g.close()
