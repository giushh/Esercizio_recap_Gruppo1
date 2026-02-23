
from Fabio.gestione_dati import DataManager


class Utente:
    def __init__(self, username: str, password: str):
        self._username = username
        self.__password = password  # incapsulamento: password privata, accessibile solo tramite metodi della classe

    def get_username(self):
        return self._username

    def check_password(self, password: str):
        return password == self.__password

    def stampa_aula(self, aula: "Aula"):
        # polimorfismo: metodo base "vuoto", saranno studente e admin a sovrascriverlo
        pass


class Studente(Utente):
    # ereditarietà: studente eredita username/password e metodi da utente
    def __init__(self, username: str, password: str, nome: str, corso: str, data_ingresso: str = ""):
        super().__init__(username, password)
        self._nome = nome
        self._corso = corso
        self._data_ingresso = data_ingresso  # info extra che l'admin può stampare (esempio polimorfismo)

    def get_nome(self) :
        return self._nome

    def get_corso(self):
        return self._corso

    def get_data_ingresso(self):
        return self._data_ingresso

    def set_corso(self, nuovo_corso: str):
        self._corso = nuovo_corso

    @classmethod
    def registrati(cls, gestione_dati, username: str, password: str, nome: str, corso: str):
        # qui gestione_dati è la classe DataManager (o un altro data manager equivalente)
        # i metodi del data manager salvano su json e ritornano bool (ok/non ok)
        # qui ritorniamo un oggetto studente se la registrazione va bene, altrimenti None

        if gestione_dati.user_check(username):
            return None

        studente = cls(username, password, nome, corso)

        ok = gestione_dati.salva_utente(studente)
        if not ok:
            return None

        return studente

    @classmethod
    def login(cls, gestione_dati, username: str, password: str):
        # incapsulamento: controllo password con check_password
        # qui supponiamo che gestione_dati.carica_studente(username) ritorni un oggetto studente o None
        studente = gestione_dati.carica_studente(username)
        if studente is None:
            return None
        if not studente.check_password(password):
            return None
        return studente

    def stampa_aula(self, aula: "Aula"):
        # polimorfismo: lo studente stampa solo info base dei compagni
        aula.ordina_per_corso()
        aula.stampa(admin=False)


class Admin(Utente):
    # ereditarietà

    ADMIN_USER = "admin"
    ADMIN_PASS = "admin123"

    def __init__(self, username: str, password: str):
        super().__init__(username, password)

    @classmethod
    def login_admin(cls, username: str, password: str):
        if username == cls.ADMIN_USER and password == cls.ADMIN_PASS:
            return cls(username, password)
        return None

    def aggiungi_studente(self, gestione_dati, aula: "Aula", username: str, password: str, nome: str, corso: str):
        # l'admin aggiunge uno studente: salva su json e poi lo aggiunge in memoria (aula)
        studente = Studente.registrati(gestione_dati, username, password, nome, corso)
        if studente is None:
            return False
        aula.aggiungi_studente(studente)
        return True

    def modifica_studente(self, gestione_dati, aula: "Aula", username: str, nuovo_corso: str):
        ok = aula.modifica_corso_studente(username, nuovo_corso)
        if not ok:
            return False

        # to do: questo metodo dovrà esistere nel data manager
        gestione_dati.courr_update(username, nuovo_corso)
        return True

    def reset_sistema(self, gestione_dati, motivazione: str):
        # reset completo: elimina lista studenti e credenziali
        # to do: questi metodi dovranno esistere nel data manager
        gestione_dati.reset_students()
        gestione_dati.log_intervention(motivazione)

    def stampa_aula(self, aula: "Aula"):
        # polimorfismo: l'admin stampa più info (esempio: data ingresso)
        aula.ordina_per_corso()
        aula.stampa(admin=True)


class Aula:
    def __init__(self, nome_aula: str):
        self._nome_aula = nome_aula
        self.__studenti: list[Studente] = []  # incapsulamento: lista privata, modificabile solo con metodi

    def get_nome_aula(self) -> str:
        return self._nome_aula

    def get_studenti(self) -> list[Studente]:
        # incapsulamento: ritorno una copia, così dall'esterno non modificano direttamente la lista
        return self.__studenti.copy()

    def aggiungi_studente(self, studente: Studente):
        self.__studenti.append(studente)

    def trova_studente_per_username(self, username: str):
        for s in self.__studenti:
            if s.get_username() == username:
                return s
        return None

    def modifica_corso_studente(self, username: str, nuovo_corso: str):
        studente = self.trova_studente_per_username(username)
        if studente is None:
            return False
        studente.set_corso(nuovo_corso)
        return True

    def ordina_per_corso(self):
        self.__studenti.sort(key=lambda s: s.get_corso())

    def stampa(self, admin: bool = False):
        if not self.__studenti:
            print("\nNessuno studente presente in aula.")
            return

        print(f"\n--- Aula: {self._nome_aula} ---")

        if admin:
            for i, s in enumerate(self.__studenti, start=1):
                print(
                    f"{i}) username: {s.get_username()} | nome: {s.get_nome()} | corso: {s.get_corso()} | data_ingresso: {s.get_data_ingresso()}"
                )
        else:
            for s in self.__studenti:
                print(f"nome: {s.get_nome()} | corso: {s.get_corso()}")


