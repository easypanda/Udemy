import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True
name=input("\t\t\tEntre Your Name: ")


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        d1=" "
        for card in self.deck:
            d1+= "\n" + card.__str__()
        return f"The cards in the deck are: {d1}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):

        self.cards.append(card)            #appending the poped card from method deal of class deck
        self.value += values[card.rank]      #then rank of that card checks with the keys of values dict and returns its value
        # counting for aces
        if card.rank == "Ace":
            self.aces+=1

    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("\n\t\tEnter how many chips you want to bet? "))
        except:
            print("ERROR!!\tERROR\tERROR")
            print("\nSorry, a bet must be an integer!")
        else:
            if chips.bet>chips.total:
                print(f"\nSorry, your bet can't exceed 100 !! You currently have {chips.total} chips")
            else:
                break


def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x=input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")

        if x.lower().startswith('h'):
            hit(deck,hand)

        elif x.lower().startswith('s'):
            print(f"\n{name} Stand Dealers Turn's!!")
            playing=False

        else:
            print("\nSorry, please try again.!!")
            continue

        break



def show_some(player,dealer):
    m=2
    n='\t'
    print(f"{6*n}-----------------------------")
    print(f"{7*n}Dealers Hand: ")
    print(f"{6*n}-----------------------------")
    print(f"\n{2*n}**This Card Is Hidden!!**\n")
    print(f"{5*n}{dealer.cards[0]}\n")
    print(f"{6*n}-----------------------------")
    print(f"{7*n}{name}'s Hand:")
    print(f"{6*n}-----------------------------")
    for i in player.cards:
        print(f"\n{n*m}{i}")
        m+=2


def show_all(player,dealer):
    p=2
    q='\t'
    r=2
    print(f"\n{6*q}-----------------------------")
    print(f"{7*q}Dealers Hand: ")
    print(f"{6*q}-----------------------------")
    for i in dealer.cards:
        print(f"\n{p*q}{i}")
        p+=2
        print(f"\n{6*q}---------------------------------")
        print(f"{6*q}|     Dealers Hand Value: {dealer.value} {q}|")
        print(f"{6*q}---------------------------------")
        print(f"\n{6*q}-----------------------------")
        print(f"{7*q}{name}'s Hand:")
        print(f"{6*q}-----------------------------")
    for j in player.cards:
        print(f"\n{r*q}{j}")
        r+=2
        print(f"\n{6*q}---------------------------------")
        print(f"{6*q}|     {name}'s Hand Value: {player.value} {q}|")
        print(f"{6*q}---------------------------------")


def player_busts(player,dealer,chips):
    print(f"\n{name} Busted!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print(f"\n{name} Won!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer Busted!!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("\nDealer wins!!")
    chips.lose_bet()

def push(player,dealer):
    print(f"\nDealer and {name} tied! It's a push.")


while True:

    print("\n------------------------------------------------------- BLACKJACK--------------------------------------------------------------")

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
