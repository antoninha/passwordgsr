import itertools
from Date import Date
from Word import Word
from Tol33t import ToL33t
from Specials_characters import Specials_characters

class Merge:
    def __init__(self,words,dates,**kargs):
        self.words = words
        self.dates = dates
        self.args = kargs

    def merge(self) :
        date = Date.getDate(self.dates)
        word = Word.getWord(self.words)
        char = Specials_characters.get_specials_chararacters()
        print(itertools.product(date,word,char))

    