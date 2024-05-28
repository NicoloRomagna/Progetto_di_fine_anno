import random

# Definizione delle risorse e quantità iniziali
oro = 100
elisir = 50

# Funzione per controllare se il giocatore ha abbastanza risorse per compiere un'azione
def controlla_risorse(oro_necessario, elisir_necessario):
    if oro >= oro_necessario and elisir >= elisir_necessario:
        return True
    else:
        return False

while True:
    print("Hai", oro, "oro e", elisir, "elisir")

    # Scelta dell'azione da parte del giocatore
    scelta = input("Cosa vuoi fare? (attaccare/difendere/raccogliere)")

    # Attaccare
    if scelta == "attaccare":
        if controlla_risorse(10, 5):
            print("Hai attaccato il nemico!")
            oro += 10
            elisir += 5
        else:
            print("Non hai abbastanza risorse per attaccare.")

    # Difendere
    elif scelta == "difendere":
        if controlla_risorse(5, 10):
            print("Hai difeso il tuo territorio!")
            oro -= 5
            elisir -= 10
        else:
            print("Non hai abbastanza risorse per difendere.")

    # Raccogliere risorse
    elif scelta == "raccogliere":
        risorsa_guadagnata = random.choice(["oro", "elisir"])
        if risorsa_guadagnata == "oro":
            amount = random.randint(5, 10)
            oro += amount
            print("Hai raccolto", amount, "di oro!")
        else:
            amount = random.randint(5, 10)
            elisir += amount
            print("Hai raccolto", amount, "di elisir!")

    else:
        print("Scelta non valida. Scegli tra attaccare, difendere o raccogliere.")