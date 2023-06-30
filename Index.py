from Merge import Merge

word = "salAté"
date = "22/09/1998"
# OPTIONS WORDS : lower | upper | first_letter |remove_accent 
# OPTIONS DATE : combineall | month_to_string | two_digits_year | four_digits_year

Merge('slt','22/09/1998',combineall = True, ).mergeDate()