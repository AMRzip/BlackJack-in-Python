import random

#creating a class card
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.number} of {self.color}"

power = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

#creating a deck class
class Deck:
    def __init__(self):
        self.color = ["Spade", "Diamond", "Heart", "Club"]
        self.numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.deck_in_play = []
    
    def create_deck(self):
        for i in self.color:
            for j in self.numbers:
                self.deck_in_play.append(Card(i, j))

    def shuffle_deck(self):
        random.shuffle(self.deck_in_play)

    def remove_card(self):
        return deck_in_play.pop()

#Creating a wallet class
class Wallet:
    def __init__(self, balance = 1000):
        self.balance = balance
        self.bet = 0

    def add_money(self, amount):
        self.balance = self.balance + amount

    def remove_money(self, amount):
        self.balance = self.balance - amount

    def ask_bet(self):
        bet_set = True
        while bet_set:
            print(f"Current Balance = {self.balance}")
            amount = int(input("Enter the Beting Amount : "))
            if amount > self.balance:
                print("Insufficient Balance!!")
            else:
                self.balance = self.balance - amount
                self.bet = amount
                bet_set = False
                break

class Player(Deck, Card):
    def __init__(self):
        self.player_hand = []
        self.values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "K":10, "Q":10, "J":10}
        self.val = 0

    def add_card(self, addCard):
        self.player_hand.append(addCard)

    def clear_hand(self):
        self.player_hand = []

    def calculate_power(self, Card):
        if Card.number == "A":
            x = int(input("Do you want the value of ace to be 1 or 11?: "))
            return x
        else:
            return self.values[Card.number]
        
    def __str__(self):
        return f"The Player's hand has a total value of {lem(player_hand)}"

#initiating a wallet
myWallet = Wallet()

#Game Loop
gameOn = True
while gameOn:

    #creating the deck in play
    deck1 = Deck()
    deck1.create_deck()

    #shuffling the deck
    deck1.shuffle_deck()

    #asking the user for bet
    myWallet.ask_bet()

    #creating a player
    print("Player's Hand is: ")
    P1 = Player()
    for i in range(2):
        P1.add_card(deck1.deck_in_play.pop())
    for i in P1.player_hand:
        print(i)

    #Dealer's Hand
    print("Dealer's Hand is: ")
    dealer_hand = []
    dealer_hand.append(deck1.deck_in_play.pop())
    dealer_hand.append(deck1.deck_in_play.pop())
    print(dealer_hand[0])
    print("Dealer's second card is faced down")

    #Player turn sequence
    player_turn = True
    player_hand_value = 0
    for i in P1.player_hand:
        a = P1.calculate_power(i)
        player_hand_value = player_hand_value + a
    dealer_hand_value = 0
    for i in dealer_hand:
        b = P1.calculate_power(i)
        dealer_hand_value = dealer_hand_value + b
    print(f"Total Bet amount is {myWallet.bet}")
    print(f"The remaining Balance is {myWallet.balance}")
    while player_turn:
        print("You have 2 Options")
        print("1 - Hit (Take another card)")
        print("2 - Stand (Stop taking more cards)")
        print(f"Player hand's Current Value is: {player_hand_value}")
        if player_hand_value >= 21:
            player_turn = False
            break
        choice = int(input("What is your next move?: "))
        if choice == 1:
            P1.add_card(deck1.deck_in_play.pop())
            print(f"The new card added is: {P1.player_hand[-1]}")
            y = P1.calculate_power(P1.player_hand[-1])
            player_hand_value = player_hand_value + y
        elif choice == 2:
            player_turn = False
            print("Player Turn Ends!! ")
            break
        else:
            print("Please chose a valid Move!! ")
            continue

    #Dealers sequence
    dealer_turn = True
    while dealer_turn:
        print("Now its the Dealer's turn!")
        if dealer_hand_value >= 17:
            print("The Deler chose to Stand !!")
            print(f"The total value of the Dealer's Hand is {dealer_hand_value}")
            print("The Dealer's cards are: ")
            for i in dealer_hand:
                print(i)
            dealer_turn = False
            break
        else:
            print("The dealer chose to Hit!!")
            dealer_hand.append(deck1.deck_in_play.pop())
            c = P1.calculate_power(dealer_hand[-1])
            dealer_hand_value = dealer_hand_value + c
            print(f"The new card is {dealer_hand[-1]}")
            print(f"Dealer's Hand New Value is {dealer_hand_value}")

    #Final Show-down
    if player_hand_value > 21:
        print(f"The Player is Bust as the value of all the cards is {player_hand_value}")
        print("The Dealer Won, Player Lost")
        myWallet.bet = 0
        print("The Player lost the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif player_hand_value == 21:
        print("The Player has BlackJack!! ")
        print("The player won!!")
        myWallet.bet = myWallet.bet*2
        myWallet.add_money(myWallet.bet)
        myWallet.bet = 0
        print("The Player won the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif dealer_hand_value == 21:
        print("The Dealer has BlackJack!! ")
        print("The dealer won!!")
        myWallet.bet = 0
        print("The Player lost the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif dealer_hand_value > 21 and player_hand_value <= 21:
        print("The dealer bust!!")
        print("Player won! Dealer Lost!")
        myWallet.bet = myWallet.bet*2
        myWallet.add_money(myWallet.bet)
        myWallet.bet = 0
        print("The Player won the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif dealer_hand_value > player_hand_value and player_hand_value < 21 and dealer_hand_value < 21:
        print("The dealer has higher value!!")
        print("The dealer won! Player lost!")
        myWallet.bet = 0
        print("The Player lost the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif player_hand_value > dealer_hand_value and player_hand_value < 21 and dealer_hand_value < 21:
        print("The Player has higher value!")
        print("Player Won! Dealer Lost!")
        myWallet.bet = myWallet.bet*2
        myWallet.add_money(myWallet.bet)
        myWallet.bet = 0
        print("The Player won the bet!")
        print(f"Player's Balance: {myWallet.balance}")
    elif dealer_hand_value == player_hand_value:
        print("It is a Tie!!")
        myWallet.bet = myWallet.bet / 2
        myWallet.add_money(myWallet.bet)
        myWallet.bet = 0
    else:
        print("Error! Verification needed \nNo output Found")
    
    #continue game confirmation
    cntChoice = input("Continue the game? (Y/N): ")
    if cntChoice.upper() == "Y":
        if myWallet.balance == 0:
            print("Insufficient Balance!")
            print("End of Game")
            gameOn = False
            break
        else:
            print("The game will start again")
            continue
    else:
        gameOn = False
        break
