import unidecode
class Word:
    def __init__(self,string,**kargs):
        self.string = string
        self.args = kargs
    def lower_string(self):
        self.string = self.string.lower()

    def upper_string(self):
        self.string = self.string.capitalize()
    
    def upper_first_letter_string(self):
        self.string = self.string[0].upper() + self.string[1:]

    def remove_accent(self):
        self.string =  unidecode.unidecode(self.string)

    def getWord(self):
        for key, value in self.args.items(): 
            if(key == 'lower' and value == True):
                self.lower_string()
            if(key == 'upper' and value == True):
                self.upper_string()
            if(key == 'first_letter' and value == True):
                self.upper_first_letter_string()
            if(key == 'remove_accent' and value == True):
                self.remove_accent()
        
        return self.string