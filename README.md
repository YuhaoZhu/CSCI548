#USC CSCI 548 HOMEWORKS FOR 2015 FALL


##Web_crawler
###This part is for HomeWork1 and based on scrapy
1. Target source: craigilist
2. Language: Python
3. Goal: At least 1000 pages
4. Usage: scrapy crawl crawl_house
5. Basic Introduction:
  1. Implemented a spider with XPath features
  2. Implemented 3 pipelines


##Information Extraction
###This part is for HomeWork2 and based on CRFSuite
1. Target source: craigilist
2. Language: Python
3. Goal: extract useful infromation from unstructured text
4. Basic Introduction:
  1. Extracted text from unstructed html file with BeautifulSoup
  2. NLP features: pos, Word Shape, prefix, surfix and etc. NLTK used.
  3. CRF with CRFsuite in python

####Python Code and explanation
1. extract.py: Extract the plain text from Html with BS
2. generator.py: Generate feature: word prefix surfix pos len wshape hasCap label from Plain txt and the default label if 'I', irrelevant
3. chunking.py: This code was based on turtorial on the CRFsuite website. Please refer the website for more. http://www.chokkan.org/software/crfsuite/tutorial.html
