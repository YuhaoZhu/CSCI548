from argparse import ArgumentParser
from os import listdir
from nltk.tokenize import word_tokenize
import sys,string,nltk

#Define the output format
#word prefix surfix pos wshape hasCap label
class Generator:
    
    def wshape(self,word):
        this_word=word
        i=0
        wshape=''
        for i in range(len(this_word)):
            if this_word[i] in (string.digits):
                if wshape.find('0')==-1:
                    wshape+='0'
            if this_word[i] in (string.ascii_lowercase):
                if wshape.find('x')==-1:
                    wshape+='x'
            if this_word[i] in (string.ascii_uppercase):
                if wshape.find('X')==-1:
                    wshape+='X'
        if wshape=='':
           wshape='?'
        return wshape
    
    def hasCap(self,word):
        for i in range(len(word)):
            if word[i] in (string.ascii_uppercase):
               return 'YES'
        return 'NO'

    def generate(self,data):
        words=word_tokenize(data)
        try:
            tags=nltk.pos_tag(words)
            for tag in tags:
                word=tag[0]
                print word,word[0],word[-1],tag[1],self.wshape(word),self.hasCap(word)
        except:
            self.error+=1    
def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    parser = ArgumentParser()
    parser.add_argument("-path", help="Path for plain text files")
#   parser.add_argument("-out", help="File word with features")
    args = parser.parse_args()

    gen = Generator()
    for f in listdir(args.path):
        with open(args.path+f) as fin:
            data=fin.read().replace('\n',' ')
            gen.generate(data)
        
        

if __name__ == '__main__':
    main()

