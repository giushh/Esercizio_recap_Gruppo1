""""-- 2 file json: utenti.json, login.json
(è la struttura più simile ad un DB per facilitare la gestione)"""

import json as j

class DataManager:
    __FILE_UTENTI = r"db/utenti.json"
    __FILE_LOGIN = r"db/login.json"
    
    # Getter per la classe
    @classmethod
    def get_file_utenti(cls):
        return cls.__FILE_UTENTI

    @classmethod
    def get_file_login(cls):
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