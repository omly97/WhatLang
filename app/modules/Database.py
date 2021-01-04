import sqlite3
from string import ascii_uppercase

class Database:

    @staticmethod
    def __get_connection():
        connexion = None
        try:
            connexion = sqlite3.connect("database.db")
        except Error as e:
            print(e)
        return connexion


    @staticmethod
    def migration():
        # query data
        gen = lambda c: c + " FLOAT NOT NULL DEFAULT 0"
        cols_ascii = [gen(char) for char in ascii_uppercase]
        cols = "id INTEGER PRIMARY KEY AUTOINCREMENT, langue TEXT NOT NULL, " + ",".join(cols_ascii)

        # creation de la table probabilites
        connexion = Database.__get_connection()
        curseur = connexion.cursor()
        curseur.execute("DROP TABLE IF EXISTS probabilites")
        curseur.execute("CREATE TABLE probabilites({})".format(cols))
        connexion.commit()
        connexion.close()


    @staticmethod
    def insert(langue, dicto):
        # query data
        cols = "langue," + ",".join(dicto.keys())
        params = "?," * len(dicto) + "?"
        values = (langue.upper(),) + tuple(dicto[c] for c in dicto.keys())

        # query execution
        connexion = Database.__get_connection()
        curseur = connexion.cursor()
        curseur.execute("INSERT INTO probabilites({}) VALUES ({})".format(cols, params), values)
        connexion.commit()
        connexion.close()


    @staticmethod
    def select_all():
        connexion = Database.__get_connection()
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM probabilites")
        rows = curseur.fetchall()
        connexion.close()
        return rows


    @staticmethod
    def __select_by_langue(langue):
        connexion = Database.__get_connection()
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM probabilites WHERE langue = ?", (langue,))
        rows = curseur.fetchall()
        connexion.close()
        return rows


    @staticmethod
    def select_fr():
        return Database.__select_by_langue('FR')


    @staticmethod
    def select_ang():
        return Database.__select_by_langue('ANG')


    @staticmethod
    def __select_avg_by_langue(langue):
        cols_ascii = ["AVG({})".format(c) for c in ascii_uppercase]
        cols = ",".join(cols_ascii)

        connexion = Database.__get_connection()
        curseur = connexion.cursor()
        curseur.execute("SELECT {} FROM probabilites WHERE langue = ?".format(cols), (langue,))
        row = curseur.fetchone()
        connexion.close()

        return row


    @staticmethod
    def select_avg_fr():
        return Database.__select_avg_by_langue('FR')


    @staticmethod
    def select_avg_ang():
        return Database.__select_avg_by_langue('ANG')