f1 = open('adj', 'r')
f2 = open('adjSenti', 'r')
g1 = open('adv', 'r')
g2 = open('advSenti', 'r')

f1lines = f1.readlines()
f2lines = f2.readlines()
g1lines = g1.readlines()
g2lines = g2.readlines()
f1.close()
f2.close()
g1.close()
g2.close()

adjFile = open('finalAdjSenti', 'w')
advFile = open('finalAdvSenti', 'w')
for i in range(len(f1lines)):
    adjFile.write(f1lines[i].strip('\n') + ' ; ' + f2lines[i].strip('\n') + '\n')
for i in range(len(g1lines)):
    advFile.write(g1lines[i].strip('\n') + ' ; ' + g2lines[i].strip('\n') + '\n')

advFile.close()
adjFile.close()
