from pyparsing import *

f = open("log2.txt", "r")
myList = []
for line in f:
    myList.append(line)
#mulai parsing
#0,093: [GC pause (G1 Evacuation Pause) (young) 14M->13M(256M), 0,0104626 secs]
word  = Word(alphas)
wordNum = Word(alphanums)
number = Word(nums)
plusorminus = Literal('+') | Literal('-')
point = Literal('.') | Literal(',')
floatnumber = Combine( number + Optional( point + Optional(number) ))
sentence = OneOrMore(wordNum)
description = Combine(sentence + "(" + ")" + "->")

grammar = floatnumber + ":" + "[" + description + "," + floatnumber +"secs" + "]"
mystr = myList[3]
print mystr
print grammar.parseString(mystr)
