import crfsuite
import sys
from argparse import ArgumentParser

class CRFTrainer(crfsuite.Trainer):
    def message(self,msg):
        print msg[:-1]

    def instances(self,fi):
        xseq = crfsuite.ItemSequence()
        yseq = crfsuite.StringList()
    
        for line in fi:
            line = line.strip('\n')
            if not line:
                yield xseq, tuple(yseq)
                xseq = crfsuite.ItemSequence()
                yseq = crfsuite.StringList()
                continue
            
            item = crfsuite.Item()
            fields = line.split('\t')
            yseq.append(fields[0])
            for field in fields[1:]:
                p = field.rfind(':')
                if p == -1:
                    item.append(crfsuite.Attribute(field))
                else:
                    item.append(crfsuite.Attribute(field[:p], float(field[p+1:])))
            xseq.append(item)


    def loadData(self,fi):
        for xseq, yseq in self.instances(fi):
            self.append(xseq,yseq,0)


def main():
    parser = ArgumentParser()
    parser.add_argument("-m", help="Path for Model")
    args = parser.parse_args()

    trainer=CRFTrainer()
    trainer.loadData(sys.stdin)
    trainer.select('lbfgs','crf1d')
    trainer.set('c2','0.25')
    trainer.train(args.m,-1)


if __name__ == '__main__':
    main()

