# -*- coding: utf-8 -*-

"""
Created on 10 July 2020
@author: anonysous
"""

from nltk.tokenize import sent_tokenize, word_tokenize

languages_codes = {
    'portuguese': 'pt',
    'italian': 'it',
    'french': 'fr'
}

def tokenize_sentence_pair(informal, formal, lang):
    splitext_informal = sent_tokenize(informal.replace("\n", ""), language=lang)
    splitext_formal = sent_tokenize(formal.replace("\n", ""), language=lang)

    tokens_informal = []
    for sent in splitext_informal:
        tokens_informal.append(word_tokenize(sent, language=lang))

    tokens_formal = []
    for sent in splitext_formal:
        tokens_formal.append(word_tokenize(sent, language=lang))

    return tokens_informal, tokens_formal


def edits(informal, formal):
    informal_sents = [item for sublist in informal for item in sublist]
    formal_sents = [item for sublist in formal for item in sublist]

    # Unchanged tokens
    intersection = list(set(informal_sents).intersection(set(formal_sents)))
    informal_changed = [x for x in informal_sents if x not in intersection]
    formal_changed = [x for x in formal_sents if x not in intersection]

    return informal_changed, formal_changed


def capitalization_edit(informal_changed, formal_changed):
    edits = 0
    for token in formal_changed:
        if token.lower() in informal_changed:
            edits += 1
    return edits


def lowercase_edit(informal_changed, formal_changed):
    edits = 0
    for token in informal_changed:
        if token.lower() in formal_changed:
            edits += 1
    return edits


def punctuation_edit(informal_changed, formal_changed):
    edits = 0
    for token in informal_changed:
        if not token.isalpha():
            edits += 1

    for token in formal_changed:
        if not token.isalpha():
            edits += 1
    return edits


def repetition_edit(informal_changed, formal_changed):
    edits = 0

    formal_lower = [x.lower() for x in formal_changed]
    informal_lower = [x.lower() for x in informal_changed]

    for token in informal_lower:
        remove_duplicates = ''.join(sorted(set(token), key=token.index))
        if token != remove_duplicates and remove_duplicates in formal_lower:
            edits += 1
    return edits


def spelling_edit(informal_changed, formal_changed):
    edits = 0

    formal_lower = [x.lower() for x in formal_changed]
    informal_lower = [x.lower() for x in informal_changed]

    for i_token in informal_lower:
        for f_token in formal_lower:
            distance = levenshtein_distance(i_token, f_token)
            if distance > 0 and distance / len(i_token) < 0.5:
                edits += 1

    return edits


def normalization_edit(informal_changed, formal_changed, abbreviations):
    edits = 0
    for i_token in informal_changed:
        if i_token in abbreviations.keys():
            replace_i_token = abbreviations[i_token]
            if replace_i_token in formal_changed:
                edits += 1
    return edits


def paraphrase_edit(informal_changed, formal_changed, abbreviations):
    minor_edits = []

    formal_lower = [x.lower() for x in formal_changed if x.isalpha()]
    informal_lower = [x.lower() for x in informal_changed]

    for i_token in informal_lower:
        for f_token in formal_lower:
            distance = levenshtein_distance(i_token, f_token)
            if distance > 0 and distance / len(i_token) < 0.5:
                minor_edits.append(f_token)

    for i_token in informal_changed:
        if i_token in abbreviations.keys():
            replace_i_token = abbreviations[i_token]
            if replace_i_token in formal_changed:
                minor_edits.append(f_token)

    major_edits = [x for x in formal_lower if x not in minor_edits]
    # print(len(major_edits))
    return len(major_edits)


def levenshtein_distance(s1, s2):
    s1 = ' '.join(s1)
    s2 = ' '.join(s2)
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
