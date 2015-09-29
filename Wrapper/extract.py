from bs4 import BeautifulSoup
from argparse import ArgumentParser
from os import listdir
import sys,string


class Extractor:

    def extract(self,filePath):
        soup = BeautifulSoup(open(filePath))
        try:
            #return soup.find('section', id="postingbody").text.strip()
            car=soup.find('p','attrgroup').span.b.text
            attr=soup.find('p','attrgroup').next_sibling
            condition="N/A"
            title="N/A"
            odometer="N/A"
            transmission="N/A"
            attrs=attr.find_all('span')
            for a in attrs:
                str=a.text
                if ('condition' in str):
                    condition=a.b.text
                elif ('title' in str):
                    title=a.b.text
                elif ('odometer' in str):
                    odometer=a.b.text
                elif ('transmission' in str):
                    transmission=a.b.text
            return car+','+condition+','+title+','+odometer+','+transmission+'\n'
        except:
            return 'Yuhao'

def main():
    parser = ArgumentParser()
    parser.add_argument("-path", help="Path for html files")
    parser.add_argument("-out", help="Path for plain files")
    args = parser.parse_args()
    
    extractor=Extractor()
    with open(args.out+'.csv','w') as fout:
        fout.write('Model,Condition,Title,Odometer,Transmission\n')
        for f in listdir(args.path):
            fout.write(extractor.extract(args.path+f).encode('utf-8'))


if __name__ == '__main__':
    main()
