#This code was modified on the basis of turtorial of CRFsuite
#The link of the source code is here:
#http://www.chokkan.org/software/crfsuite/tutorial.html
#
#Yuhao Zhu, Sep 10, 2015

#!/usr/bin/env python

"""
A feature extractor for chunking.
Copyright 2010,2011 Naoaki Okazaki.
"""

# Separator of field values.
separator = ' '

# Field names of the input data.
fields = 'word prefix surfix pos len wshape hasCap y'

# Attribute templates.
templates = (
    (('word', 0), ),
    (('prefix', 0), ),
    (('surfix',  0), ),
    (('pos',  0), ),
    (('len',  0), ),
    (('wshape', 0), ),
    (('hasCap',  0), ),
    (('word', -1),('word',0) ),
    (('word', 0),('word',1) ),
    (('pos', -1),('word',0) ),
    (('pos', 1),('word',0)),
    (('word',0),('wshape',1)),
    (('word',0),('wshape',-1)),
    (('len',0),('word',1)),
    (('len',0),('wshape',1)),
    )


import crfutils

def feature_extractor(X):
    # Apply attribute templates to obtain features (in fact, attributes)
    crfutils.apply_templates(X, templates)
    if X:
	# Append BOS and EOS features manually
        X[0]['F'].append('__BOS__')     # BOS feature
        X[-1]['F'].append('__EOS__')    # EOS feature

if __name__ == '__main__':
    crfutils.main(feature_extractor, fields=fields, sep=separator)
