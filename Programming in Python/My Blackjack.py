import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = [] #Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp =' '
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: {}".format(deck_comp)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = [] # Start with an empty list as we did in the Deck class
        self.value = 0  # Start with zero value
        self.aces = 0   # Add an attribute to keep track of aces

    def add_card(self,card):
        # Card passed in are from the Deck.deal() --> single_Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #Track for Aces
        if card.rank == "Ace":
            self.aces +=1

    def adjust_for_ace(self):

        #IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        #THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces:  #The same as self.aces > 0
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an Integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing #To control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter h or s" )

        if x.lower().startswith('h'):
            hit(deck,hand)

        elif x.lower().startswith('s'):
            print("Player Stands Dealer's Turn")
            playing=False
        else:
            print("Sorry, I did not understand that, please enter h or s only!")
            continue

        break

def show_some(player,dealer):

    print("\n")
    print("DEALER HAND:")
    print("One card hidden!")
    print(dealer.cards[1])
    print("\n")
    print("PLAYER HAND:")
    for card in player_hand.cards:
        print(card)

def show_all(player,dealer):
    print("\n")
    print("DEALER HAND:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYER HAND:")
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("BUST PLAYER! DEALER WINS")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! PUSH")

while True:
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips=Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

            if player_hand.value <= 21:
                while dealer_hand.value < 17:
                    hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
                break
            elif player_hand.value > dealer_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
                break
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
                break
            else:
                push(player_hand,dealer_hand)
                break

    print(f"\n{name}'s winning stand at: {player_chips.total} ")
    new_game=input("\n\t\tWould you like to play another hand? Enter 'y' or 'n': ")
    if new_game.lower().startswith('y'):
        playing=True
        continue
    else:
        print(f"\nThanks for playing {name}! Have a nice day!")
        break
