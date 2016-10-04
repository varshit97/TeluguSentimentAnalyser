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

class calculateSentiment:
    def getSentiment(self, sentence):
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
            for i in sentence:
                f.write(i.decode('utf-8'))
                f.write(" ")
        f.close()
        
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
        
        advFile = open('finalAdvSenti', 'r')
        adjFile = open('finalAdjSenti', 'r')
        advSentiment = 0.5
        adjSentiment = 0.5
        
        adjs = adjFile.readlines()
        adjFile.close()
        advs = advFile.readlines()
        advFile.close()
        
        for i in posTag:
            if i[2] == 'adjective':
                f = open('adjectives.lemma','r')
                for line in f:
                    tempData = line.split(' ')[1]
                    if tempData.split('.')[1].strip() == '0':
                        tempData = tempData.split('.')[0].encode('utf-8')
                    if i[0] == tempData.strip():
                        for j in adjs:
                            adj = j.split(';')[0].encode('utf-8')
                            #print tempData, adj, 'adj'
                            if tempData.strip() == adj.strip():
                                value = float(j.split(';')[1].strip().split(' ')[-2].strip())
                                wordType = j.split(';')[1].strip().split(' ')[-1].strip()
                                if wordType == 'Negative':
                                    value *= -1
                                print 'ADJ Inside: ', adj.strip(), value
                                #print 'adj valu : ', value
                                adjSentiment = value/100.0
                                #print 'ADJS: ', adjSentiment
                                #adjQuality = line.split(' ')[-1]
                        print 'ADJ Outside : ', tempData, ' ', adj
            if i[2] == 'adverb':
                g = open('adverbs.lemma','r')
                for line in g:
                    tempData = line.split(' ')[1]
                    #if tempData.split('.')[1].strip()=='0':
                    tempData = tempData.split('.')[0].encode('utf-8')
                    if i[0] == tempData.strip():
                        for j in advs:
                            adv = j.split(';')[0].encode('utf-8')
                            #print tempData, adv, 'adv'
                            if tempData.strip() == adv.strip():
                                value = float(j.split(';')[1].strip().split(' ')[-2].strip())
                                wordType = j.split(';')[1].strip().split(' ')[-1].strip()
                                if wordType == 'Negative':
                                    value *= -1
                                print 'ADV Inside: ', adv.strip(), value
                                #print 'adv valu : ', value
                                advSentiment = value/100.0
                                #print 'ADVS: ', advSentiment
                                #advQuality = line.split(' ')[-1]
                        print 'ADV Outside : ', tempData, ' ', adv
        
        if advSentiment > 0.3:
            if adjSentiment > 0:
                sentenceSentiment = adjSentiment + ((1 - adjSentiment) * advSentiment)
            else:
                sentenceSentiment = adjSentiment - ((1 - adjSentiment) * advSentiment)
        else:
            if adjSentiment < 0:
                sentenceSentiment = adjSentiment - ((1 - adjSentiment) * advSentiment)
            else:
                sentenceSentiment = adjSentiment + ((1 - adjSentiment) * advSentiment)
        return sentenceSentiment

#print calculateSentiment().getSentiment(sys.argv[1:])
