
from Ilaria.logica_aula import Studente, Admin, Aula
from Fabio.gestione_dati import DataManager


def main():
    aula = Aula("informatica")  # per ora una sola aula (poi aule todo)
    utente_loggato = None
    tipo_utente = None  # "studente" oppure "admin"

    stop = False
    while not stop:

        scelta = input("\nPuoi:"
                       "\n1. Registrazione studente"
                       "\n2. Login"
                       "\n3. Uscita"
                       "\nIndica il numero corrispondente \n> ")

        match scelta:
            case "1":
                username = input("\nusername \n> ")
                password = input("password \n> ")
                nome = input("nome \n> ")
                corso = input("corso \n> ")

                studente = Studente.registrati(DataManager, username, password, nome, corso)
                if studente is None:
                    print("\nregistrazione fallita (username già usato o errore).")
                else:
                    print("\nregistrazione completata.")
                    aula.aggiungi_studente(studente)

            case "2":
                scelta_login = input("\nLogin come:"
                                     "\n1. Studente"
                                     "\n2. Admin"
                                     "\n> ")

                if scelta_login == "1":
                    username = input("\nUsername \n> ")
                    password = input("Password \n> ")

                    studente = Studente.login(DataManager, username, password)
                    if studente is None:
                        print("\nlogin studente fallito.")
                    else:
                        utente_loggato = studente
                        tipo_utente = "studente"
                        print("\nlogin studente effettuato.")

                elif scelta_login == "2":
                    username = input("\nusername admin \n> ")
                    password = input("password admin \n> ")

                    admin = Admin.login_admin(username, password)
                    if admin is None:
                        print("\nlogin admin fallito.")
                    else:
                        utente_loggato = admin
                        tipo_utente = "admin"
                        print("\nlogin admin effettuato.")

                else:
                    print("\ncomando non valido.")
                    continue

                if utente_loggato is not None:
                    logout = False
                    while not logout:

                        if tipo_utente == "studente":
                            scelta2 = input("\nSei loggato come studente. Puoi:"
                                            "\n1. Stampa aula"
                                            "\n2. Logout"
                                            "\n> ")

                            match scelta2:
                                case "1":
                                    utente_loggato.stampa_aula(aula)  # polimorfismo: usa la stampa dello studente
                                case "2":
                                    print("\n-- Logout")
                                    utente_loggato = None
                                    tipo_utente = None
                                    logout = True
                                case _:
                                    print("\nComando non valido.")
                                    continue

                        elif tipo_utente == "admin":
                            scelta2 = input("\nSei loggato come admin. Puoi:"
                                            "\n1. Aggiungi studente"
                                            "\n2. Modifica corso studente"
                                            "\n3. Stampa aula (admin)"
                                            "\n4. Reset sistema"
                                            "\n5. Logout"
                                            "\n> ")

                            match scelta2:
                                case "1":
                                    username = input("\nUsername \n> ")
                                    password = input("Password \n> ")
                                    nome = input("nome \n> ")
                                    corso = input("corso \n> ")

                                    ok = utente_loggato.aggiungi_studente(DataManager, aula, username, password, nome, corso)
                                    if ok:
                                        print("\nStudente aggiunto.")
                                    else:
                                        print("\nOperazione fallita (username già usato o errore).")

                                case "2":
                                    username = input("\nUsername studente \n> ")
                                    nuovo_corso = input("Nuovo corso \n> ")

                                    ok = utente_loggato.modifica_studente(DataManager, aula, username, nuovo_corso)
                                    if ok:
                                        print("\nCorso aggiornato.")
                                    else:
                                        print("\nStudente non trovato o errore.")

                                case "3":
                                    utente_loggato.stampa_aula(aula)  # polimorfismo: usa la stampa dell'admin

                                case "4":
                                    motivazione = input("\nMotivazione reset \n> ")
                                    utente_loggato.reset_sistema(DataManager, motivazione)
                                    print("\nReset effettuato.")

                                    # svuoto anche l'aula in memoria per coerenza
                                    aula = Aula(aula.get_nome_aula())

                                case "5":
                                    print("\n-- Logout")
                                    utente_loggato = None
                                    tipo_utente = None
                                    logout = True

                                case _:
                                    print("\nComando non valido.")
                                    continue

            case "3":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido. \nRiprova.")
                continue


if __name__ == "__main__":
    main()