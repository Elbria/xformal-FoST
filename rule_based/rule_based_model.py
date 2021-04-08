# -*- coding: utf-8 -*-

"""
Created on 29 March 2020
@author: anonymous
"""

import argparse
import logging
import os

import string
from utils import tokenize_sentence_pair
from abbreviations import pt_abbreviations, en_abbreviations, it_abbreviations, fr_abbreviations



def main():
    parser = argparse.ArgumentParser(description='Rank corpus based on laser cosine distance')
    parser.add_argument('--debug', help='debug mode', action='store_true')
    parser.add_argument('--language', help='language', default='portuguese')
    parser.add_argument('--test_path', help='path to test folder', default='./test/pt/filtered')
    o = parser.parse_args()
    if o.debug:
        #logging.basicConfig(filename='debug.log', level=logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)

    formal_predictions = os.path.join(o.test_path, 'formal_rule_based')
    informal = os.path.join(o.test_path, 'informal')

    if o.language.lower() == 'portuguese':
        abbr = pt_abbreviations
    elif o.language.lower() == 'english':
        abbr = en_abbreviations
    elif o.language.lower() == 'italian':
        abbr = it_abbreviations
    elif o.language.lower() == 'french':
        abbr = fr_abbreviations

    with open(formal_predictions, 'w') as form, open(informal, 'r') as inform:
        inform = inform.readlines()

        for i in inform:

            # Punctuation normalization
            for punctuation in string.punctuation:
                if punctuation != '.':
                    while True:
                        replaced = i.replace(punctuation * 2, punctuation)
                        if replaced == i:
                            break
                        i = replaced

            # Repeated characters normalizations
            for char in i:
                if char != '.':
                    while True:
                        replaced = i.replace(char * 3, char)
                        if replaced == i:
                            break
                        i = replaced

            # Tokenize
            x, _ = tokenize_sentence_pair(i, i, lang=o.language)
            i_tokens = x[0]

            # Lower case tokens
            i_tokens = [x.lower() for x in i_tokens]

            # Normalize abbreviations
            for id_, x in enumerate(i_tokens):
                if x in abbr.keys():
                    print(x)
                    i_tokens[id_] = abbr[x]
                    
            # Capitalization of first letter
            i_tokens[0] = i_tokens[0].capitalize()

            # Detokenize sentence
            sent_detokenize = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i\
                                       in i_tokens]).strip()

            if o.debug:
                print('Original: %s' %(i))
                print('Rule-based output: %s' %(sent_detokenize))

            form.write(sent_detokenize + '\n')



if __name__ == "__main__":
    main()
