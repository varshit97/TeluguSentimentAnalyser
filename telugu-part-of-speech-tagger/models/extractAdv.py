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
g = open('adverbs.lemma','w')
for line in f:
    if 'RB' in line or 'INTF' in line:
        temp = line.split('\t')
        for i in temp:
            if 'RB' in i or 'INTF' in i:
                g.write(i.strip())
                g.write('\n')
f.close()
g.close()
