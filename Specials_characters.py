import itertools
from abc import ABC

class Specials_characters(ABC):
    
    @staticmethod
    def get_specials_chararacters():
            combinations = []
            for char in '.$?!*':
                combinations.append(char)
            
            for char1 in '.$?!*':
                for char2 in '.$?!*':
                    combinations.append(char1 + char2)
            
            return combinations





