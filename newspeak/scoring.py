import os
import re
import sys

import nltk

from nltk.tokenize import RegexpTokenizer

class Newspeak:
    """ Measure how much a newspaper article contains newspeak words"""
    @classmethod

    def clean_text(cls, text):
        """ Cleans text """
        tokenizer = RegexpTokenizer(r'(\w|\')+')
        tokens = tokenizer.tokenize(text)
        tokens = [token for token in tokens if len(token)>2]
        return tokens

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
        words_list = clean_text(text)
        for word in words_list:
            if has_word(newspeak_words['words'], word):
                article_score['words'] += 1
            if has_suffix(newspeak_words['suffix'], word):
                article_score['suffix'] += 1
            if has_prefix(newspeak_words['prefix'], word):
                article_score['prefix'] += 1

        return article_score
            

    def has_word(cls, config, word):
        """ Checks that article word is in newspeak config """

    @classmethod
    def has_suffix(cls, config, word):
        """ Checks that article word has newspeak suffix """
        composed = ".*\w+({})$".format('|'.join(config))
        reg = re.compile(composed)
        return bool(reg.match(word))

    def has_prefix(cls, config, word):
        """ Checks that article word has newspeak prefix"""
        for newspeak_word in config:
            if word.startswith(newspeak_word):
                return True
            else:
                return False



if __name__== "__main__":
    pe = Newspeak(record=rec)
