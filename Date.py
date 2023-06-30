class Date:
    compteur = 0
    def __init__(self,date,**kargs):
        self._day, self._month, self._year = date.split('/')
        self.args = kargs
        Date.compteur +1

    def number_date(compteur):
        return compteur
    
    def _combinations_date(self):
        combinations = []
        params = [self._day, self._month, self._year]
        num_params = len(params)

        for i in range(num_params):
            combinations.append(params[i])

            for j in range(i + 1, num_params):
                combinations.append(params[i] + params[j])
                combinations.append(params[j] + params[i])

                for k in range(j + 1, num_params):
                    combinations.append(params[i] + params[j] + params[k])
                    combinations.append(params[i] + params[k] + params[j])
                    combinations.append(params[j] + params[i] + params[k])
                    combinations.append(params[j] + params[k] + params[i])
                    combinations.append(params[k] + params[i] + params[j])
                    combinations.append(params[k] + params[j] + params[i])


        return combinations

    def _month_to_string(self):

        months = {
            '01': "janvier",
            '02': "février",
            '03': "mars",
            '04': "avril",
            '05': "mai",
            '06': "juin",
            '07': "juillet",
            '08': "août",
            '09': "septembre",
            '10': "octobre",
            '11': "novembre",
            '12': "décembre"
        }

        return months.get(self._month, "Mois invalide")
    

    def _two_digits_year(self):
        return str(int(self._year) % 100)
    
    def _four_digits_year(self):
        return self._year

    def _one_digit_month(self):
        return str(int(self._month))
    
    def _one_digit_day(self):
        return str(int(self._day))

    def getDate(self):
        all_date = []
        for key, value in self.args.items(): 
            if(key == 'combineall' and value == True):
                for dateformate in self._combinations_date():
                    all_date.append(dateformate)
            if(key == 'month_to_string' and value == True):
                all_date.append(self._month_to_string())
            if(key == 'two_digits_year' and value == True):
                all_date.append(self._two_digits_year())
            if(key == 'four_digits_year' and value == True):
                all_date.append(self._four_digits_year())

        return all_date