import crfsuite
import sys
from argparse import ArgumentParser

class CRFTagger(crfsuite.Tagger):
    def instances(self,fi):
        xseq = crfsuite.ItemSequence()
        
        for line in fi:
            line = line.strip('\n')
            if not line:
                yield xseq
                xseq = crfsuite.ItemSequence()
                continue
            
            item = crfsuite.Item()
            fields = line.split('\t')
            for field in fields[1:]:
                p = field.rfind(':')
                if p == -1:
                    item.append(crfsuite.Attribute(field))
                else:
                    item.append(crfsuite.Attribute(field[:p], float(field[p+1:])))
            xseq.append(item)

    def loadModel(self,model):
        self.open(model)

    def tag(self,fi):
        for xseq in self.instances(fi):
            self.set(xseq)
            yseq = self.viterbi()
            for t,y in enumerate(yseq):
                print y
            print

def main():
    parser = ArgumentParser()
    parser.add_argument("-m", help="Path for Model")
    args = parser.parse_args()
    
    tagger=CRFTagger()
    tagger.loadModel(args.m)
    tagger.tag(sys.stdin)


if __name__ == '__main__':
    main()

