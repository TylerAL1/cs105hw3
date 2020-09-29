import random


def dealer():
    card = random.randint(1,13)
    deck = random.shuffle("A2345678910KQJ")
    hand = ""
    for i in range(len(deck)):
        if card == 1:
            card = "A"
            hand = hand + "A"
        elif card == 11:
            card = "K"
            hand = hand + "K"

# Yeah whatever. I'm just going to add gibberish

def whatever(oompaloompa):
    Wonka = "nonsense"
    willy = "insanity"

# Why are you still reading this?
