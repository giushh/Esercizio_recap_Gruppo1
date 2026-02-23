""""-- 2 file json: utenti.json, login.json
(è la struttura più simile ad un DB per facilitare la gestione)"""

import json as j

"""Classe per la gestione dei dati, con metodi per leggere, scrivere e aggiungere dati ai file json,
fatta statica perché non ha bisogno di essere istanziata, e con metodi di classe per accedere ai file json"""
class DataManager:
    __FILE_UTENTI = r"db/utenti.json"
    __FILE_LOGIN = r"db/login.json"
    
    # Getter per la classe
    @classmethod
    def get_users_file(cls):
        return cls.__FILE_UTENTI

    @classmethod
    def get_login_file(cls):
        return cls.__FILE_LOGIN

    # Metodi per la gestione dei file json
    #inizializzazione del file se non esiste
    @staticmethod
    def write_f(file, data):
        with open(file, "w") as f:
            j.dump(data, f, indent=4)

    #lettura del file, se non esiste ritorna None
    @staticmethod
    def read_f(file):
        try:
            with open(file, "r") as f:
                return j.load(f)
        except FileNotFoundError:
            return None

    #aggiunta di un elemento al file, se il file non esiste lo crea
    #cls perché è un metodo di classe, non statico, e deve accedere ad altri metodi di classe
    @classmethod
    def append_f(cls, file, data):
        current_data = cls.read_f(file)
        if current_data is not None:
            current_data.append(data)
            cls.write_f(file, current_data)
        else:
            cls.write_f(file, [data])

    #-> MI SERVE METODO esiste_utente(username) e salva_utente(studente).
    @classmethod
    def login_check(cls, username, password):
        login_data = cls.read_f(cls.get_login_file())
        if login_data is not None:
            for login in login_data:
                if login["username"] == username and login["password"] == password:
                    return True
        return False

    @classmethod
    def user_check(cls, username):
        users = cls.read_f(cls.get_users_file())
        if users is not None:
            for user in users:
                if user["username"] == username:
                    return True
        return False
    
    #-> MI SERVE METODO aggiorna_corso(username, nuovo corso)
    @classmethod
    def cours_update(cls, username, new_course):
        users = cls.read_f(cls.get_users_file())
        if users is not None:
            for user in users:
                if user["username"] == username:
                    user["corso"] = new_course
                    cls.write_f(cls.get_users_file(), users)
                    return True
        return False
    
    #-> MI SERVE METODO reset_studenti() e intervento(motivazione)
    @classmethod
    def reset_students(cls):
        cls.write_f(cls.get_users_file(), [])
        cls.write_f(cls.get_login_file(), [])
    
    #generatore id univoco per ogni studente, basato sul numero di studenti già presenti
    @classmethod
    def generate_id(cls):
        users = cls.read_f(cls.get_users_file())
        if users is not None:
            return len(users) + 1
        else:
            return 1