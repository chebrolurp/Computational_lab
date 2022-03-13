from collections import defaultdict
import random

class TextGenerator:
    
    def __init__(self):
        self.dic = defaultdict(list)
        self.WordList = []
    
    def assimilateText(self,filename):
        with open(filename,'r+') as f:
            text = f.readlines()
            
        text = ' '.join(text).replace('\n','')
        #List of Words in the document
        WordList = str(text).split(' ')
        self.WordList=WordList
        # prefix dictonary
        for i in range(len(WordList)-2):
            self.dic[tuple([WordList[i],WordList[i+1]])].append(WordList[i+2])
    
    def generateText(self,n,word=None):
        if word is None:
            word = list(random.choice(list(d.keys())))
        else:
            try:
                word = [word,self.WordList[self.WordList.index(word)+1]]
            except ValueError:
                raise Exception('Unable to produce text with the specified start word')
        for i in range(n-2):
            word.append(random.choice(self.dic[tuple([word[i],word[i+1]])]))
        Gtext = ' '.join(word)
        print(Gtext)

if __name__=='__main__':
    t = TextGenerator()
    t.assimilateText('sherlock.txt')
    t.generateText(50,'London')
