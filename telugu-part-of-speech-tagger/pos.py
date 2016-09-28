f = open('telugu.output.txt', 'r')
new = ''
for line in f:
    if '<' not in line:
        words = line.split('\t')
        new += words[0].decode('utf-8') + '/' + words[2].decode('utf-8')
f.close()
for j in new.split('./SYM'):
    print j
    print
