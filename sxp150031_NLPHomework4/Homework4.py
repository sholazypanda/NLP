import sys
#sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
import nltk
#nltk.download()
from nltk.corpus import wordnet as wn

arguments= sys.argv
word = arguments[1]
sentence = arguments[2]

def getOverlap(signature,context):
    context = set(context)
    return len(signature.intersection(context))

def lesk(word,sentence):
    maxOverlap = 0
    bestSense = None
    signature = set()
    examples = set()
    context = nltk.word_tokenize(sentence)
    for sense in wn.synsets(word,None):
        tokSense = nltk.word_tokenize(sense.definition())
        dict = set(tokSense)
        signature = dict
        exam = sense.examples()
        for i in exam:
            signature.union(i.split(' '))
        overlap= getOverlap(signature,context)
        if overlap > maxOverlap:
            maxOverlap= overlap
            bestSense = sense
    return bestSense
                


# word = "bank"
# sentence ="I went to the bank to deposit my money"
print(lesk(word,sentence))
print(lesk(word,sentence).definition())
print(lesk(word,sentence).examples())

# sentence = ""
# word =""
# print(lesk(word,sentence))
# print(lesk(word,sentence).definition())
# print(lesk(word,sentence).examples())

