import random

# Definiamo due giocatori con punti vita e attacco iniziali
giocatore_1 = {"nome": "Gran cavaliere", "punti_vita": 4700, "attacco": 350}
giocatore_2 = {"nome": "Principe", "punti_vita": 3100, "attacco": 520}

turno = 1

# Simulazione della partita fino a quando uno dei giocatori ha esaurito i punti vita
while giocatore_1["punti_vita"] > 0 and giocatore_2["punti_vita"] > 0:
    print(f"Turno {turno}:")
    
    # Simulazione di un attacco casuale per ciascun giocatore
    attacco_giocatore_1 = random.randint(1, giocatore_1["attacco"])
    attacco_giocatore_2 = random.randint(1, giocatore_2["attacco"])
    
    # Sottraiamo i punti vita in base all'attacco
    giocatore_2["punti_vita"] -= attacco_giocatore_1
    giocatore_1["punti_vita"] -= attacco_giocatore_2
    
    print(f"{giocatore_1['nome']} attacca {giocatore_2['nome']} con {attacco_giocatore_1} punti vita")
    print(f"{giocatore_2['nome']} attacca {giocatore_1['nome']} con {attacco_giocatore_2} punti vita\n")
    
    turno += 1

# Mostra il vincitore della partita
if giocatore_1["punti_vita"] <= 0:
    print(f"{giocatore_2['nome']} ha vinto la partita!")
else:
    print(f"{giocatore_1['nome']} ha vinto la partita!")