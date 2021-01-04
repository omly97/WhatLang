from string import ascii_uppercase

class Dico:

    @staticmethod
    def dict_occurrence_of(text):
        """
            Dictionnaire occurrence des lettres
            Args:
                text (string): chaine de caracteres
            Return
                dict: (key: value) <--> (char, text.count(char))
        """

        text = text.upper()
        occs = {c: text.count(c) for c in ascii_uppercase}
        return {key:val for key,val in occs.items() if val != 0}


    @staticmethod
    def dict_probability_of(dicto):
        """
            Dictionnaire probabilite occurrence des lettres
            Args:
                dicto (dict): resultat de dict_occurrence_of(text)
            Return
                dict: (key: value) <--> (char, dicto(char)/n)
        """

        n = 0
        for c in dicto.keys():
            n += dicto[c]
        return {c: round(dicto[c] / n, 2) for c in dicto.keys()}


    @staticmethod
    def sum_dict(dict1, dict2):
        """
            Somme de deux dictionnaires
            Args:
                dict1 (dict):
                dict2 (dict):
            Return
                dict: (key: value) <--> (char, dict1[char] + dict2[char])
        """

        dicto = dict1.copy()

        for c in dict2.keys():
            if c in dicto.keys():
                dicto[c] = round(dicto[c] + dict2[c], 2)
            else:
                dicto[c] = round(dict2[c], 2)

        return dicto


    @staticmethod
    def diff_dict(dict1, dict2):
        """
            Somme de deux dictionnaires
            Args:
                dict1 (dict):
                dict2 (dict):
            Return
                dict: (key: value) <--> (char, dict1[char] - dict2[char])
        """

        dict3 = {c: -1 * dict2[c] for c in dict2.keys()}
        return Dico.sum_dict(dict1.copy(), dict3)


    @staticmethod
    def get_occurrences_of_file(filename):
        dic = dict([])
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                dic = Dico.sum_dict(dic, Dico.dict_occurrence_of(line))
        return dic


    @staticmethod
    def dict_of_row(row):
        return {ascii_uppercase[i]:row[i] for i in range(len(ascii_uppercase))}