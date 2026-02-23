# Esercizio_recap

Collaboratori: Ilaria Cuccaro, Fabio D'Alessandro

## Esercizio Recap

Obiettivo
Verificare la comprensione della gestione dei file in Python applicando le tre regole fondamentali:

- Gestire la modalità di apertura (r, w, a)
- Recap delle tre regole fondamentali

Realizza un programma Python che gestisca un file chiamato studenti.txt e svolga le seguenti operazioni:

- Crea un sistema ripetitivo che permetta di registrarsi e fare login
- Chieda all’utente per registrarsi di inserire nome e password
- Salvi i nomi nel file credenziali.txt, uno per riga
- Quando un utente è loggato può fare due cose: Inserire/Modificare studenti oppure stampare l’aula
- In Inserisci/Modifica studenti deve poter aggiungere uno studente (attributi: Nome, CORSO) oppure modificare la lista in file CSV
- La stampa della lista deve stampare tutta l’aula ordinando gli studenti per corso
- Creare una classe figlia di utente che è admin, che può resettare completamente la lista e non deve registrarsi

---

# Esercizio Recap - Soluzione
Il progetto è organizzato in tre file principali:
- `main.py`: contiene la logica principale del programma, gestisce l'interazione con l'utente e coordina le operazioni tra le classi.
- `Ilaria/logica_aula.py`: definisce le classi `Utente`, `Studente`, `Admin` e `Aula` che rappresentano la logica della gestione dell'aula e degli utenti.
- `Fabio/gestione_dati.py`: contiene la classe `DataManager` che gestisce la lettura e scrittura dei dati nei file, oltre a una funzione per loggare gli interventi di reset.

Il programma permette agli utenti di registrarsi, fare login, inserire o modificare studenti e stampare la lista degli studenti ordinati per corso. Gli admin hanno la possibilità di resettare completamente la lista degli studenti, con un log dettagliato dell'intervento.

