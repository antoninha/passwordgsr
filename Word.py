import unidecode
import re
x = input("Word : ")
print(x)

print(x.lower())
print(x.upper())
print(x.capitalize())
print(unidecode.unidecode(x))
re.findall('.',x)
print(x)    
