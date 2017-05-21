
# coding: utf-8

# In[167]:
from __future__ import division
import sys
#sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
import nltk
import numpy as np
import sys
import collections
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk import ngrams
from collections import namedtuple



# In[168]:

arguments = sys.argv
corpus = open(arguments[1],'r').read()
sentence1 = arguments[2]
sentence2 = arguments[3]
#

# Do this in your ipython notebook or analysis script

#corpus = open('/Users/shobhikapanda/Documents/NLP/corpus.txt').read()
#sentence1 = "The chief executive said that the company’s profit was going down last year."
#sentence2 = "The president said the revenue was good last year."
#sentence1 = "rain rain go away."
#sentence2 = "go rain rain no more."
#nltk.download()


# In[78]:

tokens = nltk.word_tokenize(corpus)
# In[43]:

#nltk.download()

biGramCountCorpus = Counter(ngrams(tokens, 2))
# In[101]:

#print(biGramCountCorpus)


# In[80]:

tokenizeS1 = nltk.word_tokenize(sentence1)
#print(tokenizeS1)
biGramCountS1 = Counter(ngrams(tokenizeS1,2))


# In[81]:

tokenizeS2 = nltk.word_tokenize(sentence2)
biGramCountS2  = Counter(ngrams(tokenizeS2, 2))


# In[49]:

#print(biGramCountS1)


# In[50]:

#print(biGramCountS2)


# In[82]:

NO_S1 = len(tokenizeS1)
NO_S2 = len(tokenizeS2)
NO_Corpus = len(tokens)


# In[52]:


#print(NO_S1)
#print(NO_S2)
#print(NO_Corpus)


# In[53]:



# In[54]:

#print(tokenizeS1)
#print(tokenizeS2)


# In[55]:
 


# In[56]:

#print(lst)


# In[83]:

def mergeAndFormTable(tokenizedInput,number,biGramCountInputCorpus):
    dout = [[0]*number for x in range(number)]
    for x in range(number):
        for y in range(number):
                 dout[x][y] = biGramCountInputCorpus[(tokenizedInput[x],tokenizedInput[y])] 
    return dout


# In[233]:
sentence1Count=[[0]*NO_S1 for i in range(NO_S1)]
sentence2Count=[[0]*NO_S2 for i in range(NO_S2)]
sentence1Count = mergeAndFormTable(tokenizeS1,NO_S1,biGramCountCorpus)
sentence2Count = mergeAndFormTable(tokenizeS2,NO_S2,biGramCountCorpus)
print("Count Matrix sentence1 without smoothing::")
print(np.matrix(sentence1Count))
print("\n")
print("Count Matrix sentence2 without smoothing::")
print(np.matrix(sentence2Count))
print("\n")
#print(sentence1Count)


# In[85]:

unigramCountCorpus = Counter(ngrams(tokens,1))
vocabCount = len(unigramCountCorpus)


# In[61]:

#print(unigramCountCorpus)
#print(vocabCount)


# In[86]:

def calcProb(sCount,number,unigramCountCorpus,tokenizedSentence):
    dPout = sCount
    for x in range(number):
        for y in range(number):
            #print(unigramCountCorpus[(tokenizedSentence[i],)])
            if unigramCountCorpus[(tokenizedSentence[x],)] != 0 :
                dPout[x][y] = sCount[x][y]/unigramCountCorpus[(tokenizedSentence[x],)]
            else:
                dPout[x][y] = 0
    return dPout


# In[87]:

sentence1Prob = calcProb(sentence1Count,NO_S1,unigramCountCorpus,tokenizeS1)
sentence2Prob = calcProb(sentence2Count,NO_S2,unigramCountCorpus,tokenizeS2)


# In[64]:
print("Sentence 1 Probability without smoothing:")
print(np.matrix(sentence1Prob))
print("\n")

# In[65]:
print("Sentence 2 Probability without smoothing:")
print(np.matrix(sentence2Prob))
print("\n")


# In[66]:

#print(np.matrix(sentence1Prob))


# In[88]:

def calcTotProb(number,unigramCountCorpus,tokenizedSentence,biGramCountCorpus,NO_Corpus):
    startProb = unigramCountCorpus[(tokenizedSentence[0],)]/NO_Corpus
    #print(startProb)
    for x in range(1,number):
        if (unigramCountCorpus[(tokenizedSentence[x-1],)] != 0 and biGramCountCorpus[(tokenizedSentence[x-1],tokenizedSentence[x])] !=0) :
            startProb *=  biGramCountCorpus[(tokenizedSentence[x-1],tokenizedSentence[x])]/unigramCountCorpus[(tokenizedSentence[x-1],)]
    
           # print(unigramCountCorpus[(tokenizedSentence[x-1],)])
           # print(biGramCountCorpus[(tokenizedSentence[x-1],tokenizedSentence[x])])
    endProb = startProb * (unigramCountCorpus[(tokenizedSentence[number-1],)]/NO_Corpus)
    return endProb


# In[89]:

sentence1TotProb1 = calcTotProb(NO_S1,unigramCountCorpus,tokenizeS1,biGramCountCorpus,NO_Corpus)


# In[69]:
print("Sentence 1 Total Probability without smoothing:")
print(sentence1TotProb1)


# In[90]:

sentence1TotProb2 = calcTotProb(NO_S2,unigramCountCorpus,tokenizeS2,biGramCountCorpus,NO_Corpus)


# In[71]:
print("Sentence 2 Total Probability without smoothing:")
print(sentence1TotProb2)


# In[91]:

sentence1TotProb1 < sentence1TotProb2
sentence1Count = mergeAndFormTable(tokenizeS1,NO_S1,biGramCountCorpus)
sentence2Count = mergeAndFormTable(tokenizeS2,NO_S2,biGramCountCorpus)

# In[92]:

def addOneMatrixCount(sentenceCount,lengthOfSentence):
    addOneMatrixCount=[[0]*lengthOfSentence for i in range(lengthOfSentence)]
    for i in range(lengthOfSentence):
        for j in range(lengthOfSentence):
            addOneMatrixCount[i][j] = sentenceCount[i][j]+1
    return addOneMatrixCount


# In[ ]:



# In[93]:

addOneSentence1 = addOneMatrixCount(sentence1Count,NO_S1)
addOneSentence2 = addOneMatrixCount(sentence2Count,NO_S2)


# In[75]:
print("Add one sentence1 count matrix:")
print(np.matrix(addOneSentence1))


# In[94]:
print("Add one sentence2 count matrix:")
print(np.matrix(addOneSentence2))


# In[95]:

def addOneMatrixProbCount(addOneSentenceCount,vocabCount,sentenceLength,unigramCountCorpus,tokenizedSentence):
    resultProb = addOneSentenceCount
    for i in range(sentenceLength):
        for j in range(sentenceLength):
            resultProb[i][j] = resultProb[i][j]/(unigramCountCorpus[(tokenizedSentence[i],)]+vocabCount)
    return resultProb


# In[96]:


addOneSentence1Prob = addOneMatrixProbCount(addOneSentence1,vocabCount,NO_S1,unigramCountCorpus,tokenizeS1)
addOneSentence2Prob = addOneMatrixProbCount(addOneSentence2,vocabCount,NO_S2,unigramCountCorpus,tokenizeS2)


# In[226]:
print("Add one sentence1 prob matrix:")
print(np.matrix(addOneSentence1Prob))


# In[ ]:
print("Add one sentence2 prob matrix:")
print(np.matrix(addOneSentence2Prob))


# In[97]:

def addOneMatrixCalcTotProb(biGramCountCorpus,NO_Corpus,sentenceLength,unigramCountCorpus,tokenizedSentence,vocabCount):
    startProb = unigramCountCorpus[(tokenizedSentence[0],)]/NO_Corpus
    for x in range(1,sentenceLength):
        startProb *=  (biGramCountCorpus[(tokenizedSentence[x-1],tokenizedSentence[x])]+1)/(unigramCountCorpus[(tokenizedSentence[x-1],)]+vocabCount)
    endProb = startProb * (unigramCountCorpus[(tokenizedSentence[sentenceLength-1],)]/NO_Corpus)
    return endProb


# In[98]:

addOneTotProbS1 = addOneMatrixCalcTotProb(biGramCountCorpus,NO_Corpus,NO_S1,unigramCountCorpus,tokenizeS1,vocabCount)
print("Add one sentence1 Total Probability :")
print(addOneTotProbS1)


# In[99]:

addOneTotProbS2 = addOneMatrixCalcTotProb(biGramCountCorpus,NO_Corpus,NO_S2,unigramCountCorpus,tokenizeS2,vocabCount)


# In[ ]:
print("Add one sentence2 Total Probability :")
print(addOneTotProbS2)


# In[100]:

print(addOneTotProbS1 < addOneTotProbS2)


# In[228]:

def goodTuringCount(biGramCountCorpus,sentenceLength,tokenizedSentence,vocabCount):
    gtCount=[[0]*sentenceLength for i in range(sentenceLength)]
    dictionaryBigram = dict(biGramCountCorpus)
    freqOfFreq = Counter(dictionaryBigram.values())
    Ncplus1 = 0
    Nc = 0
    for x in range(sentenceLength):
        for y in range(sentenceLength):
            gtCount[x][y] = (biGramCountCorpus[(tokenizedSentence[x],tokenizedSentence[y])]+1);
            Ncplus1 += freqOfFreq[gtCount[x][y]]
            Nc += freqOfFreq[gtCount[x][y] - 1]
            if Nc == 0:
                gtCount[x][y] = Ncplus1/vocabCount
            else:
                gtCount[x][y] *= Ncplus1/Nc
    return gtCount     


# In[229]:

#dictionaryBigram = dict(biGramCountCorpus)
#freqOfFreq = Counter(dictionaryBigram.values())
#freqOfFreq[1]
#print(NO_S1)


# In[230]:

gtCountSentence1 = goodTuringCount(biGramCountCorpus,NO_S1,tokenizeS1,vocabCount)
gtCountSentence2 = goodTuringCount(biGramCountCorpus,NO_S2,tokenizeS2,vocabCount)


# In[231]:
print("Good Turing sentence1 Count Matrix :")
print(np.matrix(gtCountSentence1))


# In[232]:
print("Good Turing sentence2 Count Matrix :")
print(np.matrix(gtCountSentence2))


# In[194]:

def goodTuringProbCount(gtCount,unigramCountCorpus,tokenizedSentence,sentenceLength):
    gtProb = gtCount
    for i in range(sentenceLength):
        for j in range(sentenceLength):
            if unigramCountCorpus[(tokenizedSentence[i],)] != 0 :
                gtProb[i][j] = gtProb[i][j]/unigramCountCorpus[(tokenizedSentence[i],)]
    return gtProb


# In[201]:

gtProbSentence1 = goodTuringProbCount(gtCountSentence1,unigramCountCorpus,tokenizeS1,NO_S1)
gtProbSentence2 = goodTuringProbCount(gtCountSentence2,unigramCountCorpus,tokenizeS2,NO_S2)


# In[247]:
print("Good Turing sentence1 Prob Matrix :")
print(np.matrix(gtProbSentence1))
print("Good Turing sentence2 Prob Matrix :")
print(np.matrix(gtProbSentence2))


# In[249]:

def goodTuringTotProb(gtProbSentence,NO_Corpus,tokenizedSentence,sentenceLength,unigramCountCorpus):
    startProb = unigramCountCorpus[(tokenizedSentence[0],)]/NO_Corpus 
    for i in range(1,sentenceLength):
        startProb = startProb * gtProbSentence[i-1][i]
        #print(startProb)
    return startProb


# In[250]:

goodTuringProbSentence1 = goodTuringTotProb(gtProbSentence1,NO_Corpus,tokenizeS1,NO_S1,unigramCountCorpus)


# In[251]:

goodTuringProbSentence2 = goodTuringTotProb(gtProbSentence2,NO_Corpus,tokenizeS2,NO_S2,unigramCountCorpus)


# In[241]:
print("Good Turing sentence1 Total Probability :")

print(goodTuringProbSentence1)


# In[246]:
print("Good Turing sentence2 Total Probability :")
print(goodTuringProbSentence2)


# In[ ]:



