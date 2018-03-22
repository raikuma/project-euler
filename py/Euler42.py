from lib import *

f = open("words.txt", 'r')
a = f.readline()[1:-1].split('","')
f.close()

print len([x for x in a if isTriNumber(getWordValue(x))])
