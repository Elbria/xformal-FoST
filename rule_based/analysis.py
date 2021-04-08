# -*- coding: utf-8 -*-

"""
Created on 29 March 2020
@author: anonymous
"""

import argparse
import logging
import os

from utils import tokenize_sentence_pair
from utils import capitalization_edit
from utils import edits
from utils import lowercase_edit
from utils import punctuation_edit
from utils import repetition_edit
from utils import spelling_edit
from utils import paraphrase_edit
from utils import normalization_edit
from abbreviations import pt_abbreviations, en_abbreviations, it_abbreviations, fr_abbreviations


def main():
    parser = argparse.ArgumentParser(description='Rank corpus based on laser cosine distance')
    parser.add_argument('--debug', help='debug mode', action='store_true')
    parser.add_argument('--language', help='language', default='portufuese')
    parser.add_argument('--test_path', help='path to test folder', default='./portuguese_spell_check')
    o = parser.parse_args()
    if o.debug:
        #logging.basicConfig(filename='pt_debug.log', level=logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)

    formal = os.path.join(o.test_path, 'formal.all.4')
    informal = os.path.join(o.test_path, 'informal.all.4')

    if o.language.lower() == 'portuguese':
        abbr = pt_abbreviations
    elif o.language.lower() == 'english':
        abbr = en_abbreviations
    elif o.language.lower() == 'italian':
        abbr = it_abbreviations
    elif o.language.lower() == 'french':
        abbr = fr_abbreviations

    # Initialize counter stats
    split_sentences = 0
    unchanged = 0
    capitalization_edits, lowercase_edits, punctuation_edits, repetition_edits = 0, 0, 0, 0
    spelling_edits, paraphrase_edits, normalization_edits = 0, 0, 0
    total_sentences = 0
    minor_edits = 0


    with open(formal, 'r') as form, open(informal, 'r') as inform:
        form = form.readlines()
        inform = inform.readlines()

        for id_, (i, f) in enumerate(zip(inform, form)):
            total_sentences += 1
            i_tokens, f_tokens = tokenize_sentence_pair(i, f, lang=o.language)

            # Unchanged sentences
            if i == f:
                unchanged += 1

            # Split sentences
            if len(f_tokens) > len(i_tokens):
                if o.debug:
                    logging.info('Split sentence:\t Informal %s' % (i.rstrip()))
                    logging.info('Split sentence:\t Formal %s' % (f.rstrip()))
                split_sentences += 1

            # Collect edited tokens
            informal_edits, formal_edits = edits(i_tokens, f_tokens)

            # Capitalization
            if capitalization_edit(informal_edits, formal_edits) != 0:
                capitalization_edits += 1

            # Lowercase
            if lowercase_edit(informal_edits, formal_edits) != 0:
                lowercase_edits += 1

            # Punctuation
            if punctuation_edit(informal_edits, formal_edits) != 0:
                punctuation_edits += 1

            # Rpetition
            if repetition_edit(informal_edits, formal_edits) != 0:
                repetition_edits += 1

            # Spelling
            if spelling_edit(informal_edits, formal_edits) != 0:
                spelling_edits += 1

            # Normalization (abbreviations)
            if normalization_edit(informal_edits, formal_edits, abbr) != 0:
                normalization_edits += 1

            # Paraphrase edits
            if paraphrase_edit(informal_edits, formal_edits, abbr) >= 3:
                paraphrase_edits += 1
            else:
                minor_edits += 1

    print('Split sentences:\t\t %.2f' % (split_sentences / total_sentences))
    print('Unchanged sentences:\t\t %.2f' % (unchanged / total_sentences))
    print('Capitalization sentences:\t %.2f' % (capitalization_edits / total_sentences))
    print('Lowercase sentences:\t\t %.2f' % (lowercase_edits / total_sentences))
    print('Punctuation sentences:\t\t %.2f' % (punctuation_edits / total_sentences))
    print('Repetition sentences:\t\t %.2f' % (repetition_edits / total_sentences))
    print('Spelling sentences:\t\t %.2f' % (spelling_edits / total_sentences))
    print('Paraphrase sentences:\t\t %.2f' % (paraphrase_edits / total_sentences))
    print('Normalization sentences:\t %.2f' % (normalization_edits / total_sentences))
    print('Minor edits:\t %.2f' % (minor_edits / total_sentences))

   
if __name__ == "__main__":
    main()
