import time
import random as r

PLAYERS = []

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Dealer:
    def __init__(self) -> None:
        self.hand = []

    def deal_card(self, card):
        self.hand.append(card)


class Player:
    number_of_players = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cash = 100
        self.hand = []
        Player.number_of_players += 1

    def deal_card(self, card):
        self.hand.append(card)


def start_game():

    for i in range(7):
        player_counter = i + 1
        player_name = input(f"Input player {player_counter} name: ")

        if player_name == "":
            break

        player = Player(player_counter, player_name)
        PLAYERS.append(player)
    print()


def shuffle_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    r.shuffle(deck)
    return deck


def deal_strating_hand(dealer, shuffled_deck):
    for i in range(2):

        for player in PLAYERS:
            player.deal_card(shuffled_deck.pop())

        dealer.deal_card(shuffled_deck.pop())

    print("Dealer Top Card")
    print(dealer.hand[1])
    print()


def check_if_bust():
    pass


def card_value(hand):

    for card in hand:
        pass


def round():
    dealer = Dealer()
    shuffled_deck = shuffle_deck()

    deal_strating_hand(dealer, shuffled_deck)

    for player in PLAYERS:
        i = 1
        print(f"{player.name}'s hand -----> {player.hand}")
        choice = input("HIT: H | STAY: S ---> :")

        while choice.lower() == "h":
            # checks if bust
            player.deal_card(shuffled_deck.pop())
            print(f"{player.name}'s hand -----> {player.hand}")
            choice = input("HIT: H | STAY: S ---> :")


def main():

    start_game()
    round()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"{end_time - start_time:.3f} seconds")
