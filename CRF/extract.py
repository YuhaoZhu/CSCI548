from bs4 import BeautifulSoup
from argparse import ArgumentParser
from os import listdir
import sys,string


class Extractor:

    def extract(self,filePath):
        soup = BeautifulSoup(open(filePath))
        try:
            return soup.find('section', id="postingbody").text.strip()
        except:
            return 'Yuhao'

def main():
    parser = ArgumentParser()
    parser.add_argument("-path", help="Path for html files")
    parser.add_argument("-out", help="Path for plain files")
    args = parser.parse_args()
    
    extractor=Extractor()
    for f in listdir(args.path):
        with open(args.out+f.split('.')[0]+'.txt','w') as fout:
            fout.write(extractor.extract(args.path+f).encode('utf-8'))


if __name__ == '__main__':
    main()
