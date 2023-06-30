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

    def mergeWords(self) : 
        words = []
        for word in self.words:
            words.append(Word(word,self.args).getWord())
        return words
    
    def mergeDate(self) : 
        dates = []
        for date in self.dates:
            dates.append(Date(date,self.args).getDate())
            print(dates)
        return dates
    