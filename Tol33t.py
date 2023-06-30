from math import comb
from Word import Word

class ToL33t(Word):
    def _generate_combinations(self):
        replacements = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            'l': '1',
            's': '5',
            'b': '8',
            't': '7',
            'z': '2',
            'g': '6'
        }

        def _recursive_combinations(string, index, current_combination, results):
            if index == len(string):
                results.append(current_combination)
                return

            letter = string[index]
            if letter in replacements:
                _recursive_combinations(string, index + 1, current_combination + replacements[letter], results)

            _recursive_combinations(string, index + 1, current_combination + letter, results)

        results = []
        _recursive_combinations(self.string, 0, '', results)
        return results

