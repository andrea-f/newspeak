import os
import re
import sys

import nltk
from collections import defaultdict
from typing import List

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
    def clean_text(cls, text: str) -> List[str]:
        """ Cleans text """
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        tokens = [token for token in tokens if len(token)>3]
        return tokens

    @classmethod
    def has_prop(cls, mode: str, config: List[str], word: str) -> bool:
        reg = gen_regexp(mode, config)
        return bool(reg.match(word))

    @classmethod
    def counter(cls, config: dict, words_list: List[str]) -> float:
        """ 
        Scores a list of words based on a newspeak words object 
        newspeak object:
        TEST_CONFIG = {
            'words': ['find', 'me'],
            'suffix': ['ed'],
            'prefix': ['un', 'ante']
        }
        """
        article_score = defaultdict(lambda: 0)
        for word in words_list:
            for mode in POINTS:
                if cls.has_prop(mode, config[mode], word):
                    article_score[mode] += 1

        return dict(article_score)

    @classmethod
    def scoring(cls, newspeak_words, text) -> float:
        total_newspeak = 0
        words_list = cls.clean_text(text)
        total_words = len(words_list)
        article_score = cls.counter(newspeak_words, words_list)
        for val in article_score.values():
            total_newspeak += val
        has_newspeak = (total_newspeak / total_words)
        return has_newspeak


if __name__== "__main__":
    pe = Newspeak(record=rec)
