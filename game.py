import math
import random
# We denote D as diamond, H as heart, S as Spade, and C as Clubs
suit_list = ['D','H','S','C']
game = True
can_hit = True
dealer_can_hit = True
cards = []
val_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
for i in suit_list:
    for j in val_list:
        cards.append(i + j)
yourDeck = []
dealerDeck = []
random.shuffle(cards)
yourDeck.append(cards.pop(0))
random.shuffle(cards)
yourDeck.append(cards.pop(0))
random.shuffle(cards)
dealerDeck.append(cards.pop(0))
random.shuffle(cards)
dealerDeck.append(cards.pop(0))
print('Your cards are:')
print(yourDeck)
print('Dealer cards are: ')
print(str(dealerDeck[0]) + ' hidden')
yourDeck_val = []
dealerDeck_val = []
val_dict = {'2':[2],'3':[3],'4':[4],'5':[5],'6':[6],'7':[7],'8':[8],'9':[9],'10':[10],'J':[10],'Q':[10],'K':[10],'A':[1,11]}
for i in yourDeck:
    if len(yourDeck_val) != 0:
        vals_to_consider = val_dict[i[1:]]
        new_list = []
        while yourDeck_val:
            a = yourDeck_val.pop(0)
            for j in vals_to_consider:
                new_list.append(a + j)
        yourDeck_val = new_list
    else:
        for i in val_dict[i[1:]]:
            yourDeck_val.append(i)
yourDeck_val = list(set(yourDeck_val))
print(sorted(yourDeck_val))
for i in dealerDeck:
    if len(dealerDeck_val) != 0:
        vals_to_consider = val_dict[i[1:]]
        new_list = []
        while dealerDeck_val:
            a = dealerDeck_val.pop(0)
            for j in vals_to_consider:
                new_list.append(a + j)
        dealerDeck_val = new_list
    else:
        for i in val_dict[i[1:]]:
            dealerDeck_val.append(i)
dealerDeck_val = list(set(dealerDeck_val))

# setup of board and values
while can_hit:
    if min(yourDeck_val) > 21:
        can_hit = False
        print("Unfortunate Loss")
        dealer_can_hit = False
    else:
        a = input("Do you want to hit? (Y or N) ")
        if a == 'Y':
            card = cards.pop(0)
            print('You got ' + card)
            vals_to_consider = val_dict[card[1:]]
            new_list = []
            while yourDeck_val:
                a = yourDeck_val.pop(0)
                for j in vals_to_consider:
                    new_list.append(a + j)
            yourDeck_val = new_list
            print(yourDeck_val)
        else:
            break
print("dealer 2nd card is : " + str(dealerDeck[1]))
while dealer_can_hit:
    if max(dealerDeck_val) > 16:
        dealer_can_hit = False
    else:
            card = cards.pop(0)
            print('Dealer got ' + card)
            vals_to_consider = val_dict[card[1:]]
            new_list = []
            while dealerDeck_val:
                a = dealerDeck_val.pop(0)
                for j in vals_to_consider:
                    new_list.append(a + j)
            dealerDeck_val = new_list
best_dealer = 0
best_you = 0
for i in dealerDeck_val:
    if i <= 21:
        best_dealer = max(best_dealer,i)
for i in yourDeck_val:
    if i <= 21:
        best_you = max(best_you,i)
print("Your val was: " + str(best_you))
print("Dealer val was: " + str(best_dealer))
if best_you == best_dealer:
    print("These are equal so it's a draw")
elif best_you > best_dealer:
    print("You Won!")
else:
    print("You lost :(")
    










