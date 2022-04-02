import random

diamonds = ["A\u2666", "2\u2666", "3\u2666", "4\u2666", "5\u2666", "6\u2666",
            "7\u2666", "8\u2666", "9\u2666", "10\u2666", "J\u2666", "Q\u2666", "K\u2666"]
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
