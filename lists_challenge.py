import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    select = input("Press enter to pick a card, or Q then enter to quit:\t")
    if select == 'Q':
        print("Goodbye")
        break
    else:
        random.shuffle(diamonds)
        hand = hand + diamonds[-1:]
        diamonds.pop()
        print(f"Your hand:\t{hand}")
        print(f"Remaining cards:\t{diamonds}")

if not diamonds:
    print("There are no more cards to pick.")
