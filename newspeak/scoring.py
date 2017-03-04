import os, sys
import nltk
from nltk.tokenize import RegexpTokenizer

class Newspeak:
    """ Measure how much a newspaper article contains newspeak words"""
    @classmethod

    def clean_text(cls, text):
        """ Cleans text """
        tokenizer = RegexpTokenizer(r'(\w|\')+')
        tokens = tokenizer.tokenize(text)
        return tokens

    def scoring(cls, newspeak_words, words_list):
        """ 
        Scores a list of words based on a newspeak words object 
        newspeak object:
        TEST_CONFIG = {
            'words': ['find', 'me'],
            'suffix': ['ed'],
            'prefix': ['un', 'ante']
        }
        """
        for word in words_list:
            if has_word(word):
                pass
            

    def has_word(cls, config, word):
        """ Checks that article word is in newspeak config """

    def has_suffix(cls, config, word):
        """ Checks that article word has newspeak suffix """
        for newspeak_word in config:
            if word.endswith(newspeak_word):
                return True
            else:
                return False

    def has_prefix(cls, config, word):
        """ Checks that article word has newspeak prefix"""
        for newspeak_word in config:
            if word.startswith(newspeak_word):
                return True
            else:
                return False



if __name__== "__main__":
    pe = Newspeak(record=rec)
