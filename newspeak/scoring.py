import os
import re
import sys

import nltk

from nltk.tokenize import RegexpTokenizer

from newspeak.regexp_utils import gen_regexp


POINTS = {
    'words': 1,
    'prefix': 1,
    'suffix': 1,
}

class Newspeak:
    """ Measure how much a newspaper article contains newspeak words"""
    @classmethod

    def clean_text(cls, text):
        """ Cleans text """
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        tokens = [token for token in tokens if len(token)>3]
        return tokens

    @classmethod
    def has_prop(cls, mode, config, word):
        reg = gen_regexp(mode, config)
        return bool(reg.match(word))

    def scoring(cls, newspeak_words, text):
        """ 
        Scores a list of words based on a newspeak words object 
        newspeak object:
        TEST_CONFIG = {
            'words': ['find', 'me'],
            'suffix': ['ed'],
            'prefix': ['un', 'ante']
        }
        """
        article_score = {
            "words": 0,
            "prefix": 0,
            "suffix": 0
        }
        words_list = clean_text(text)
        total_words = 0
        for word in words_list:
            for mode in POINTS:
                if cls.has_prop(mode, config, word):
                    article_score[mode] += 1
        total_newspeak = 0
        for k, v in article_score.iteritems():
            total_newspeak += v
        has_newspeak = (total_newspeak / total_words) * 100
        return has_newspeak



if __name__== "__main__":
    pe = Newspeak(record=rec)
