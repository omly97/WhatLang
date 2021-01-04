from prettytable import PrettyTable
from string import ascii_uppercase


class Printer:

    @staticmethod
    def print_proba(rows):
        table = PrettyTable()
        table.field_names = ["ID", "LANG"] + [c for c in ascii_uppercase]
        for row in rows:
            table.add_row(row)
        print(table)


    @staticmethod
    def print_avg(row):
        table = PrettyTable()
        table.field_names = [c for c in ascii_uppercase]
        table.add_row(row)
        print(table)