from random import choice

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "Jack": 10, "Queen": 10, "King": 10,
    "Ace": 11
}

def deal():
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    return choice(cards) 

def calculate_total(cards):
    ace = 0 
    total = 0
    for card in cards: 
        total += card_values[card] 
        if card == 'Ace':
            ace += 1

    while total > 21 and ace: 
        total -= 10
        ace -= 1 
    return total

def compare_player_dealer(player_score, dealer_score):
    if dealer_score == 21:
        return "You Lose!"
    elif player_score == 21:
        return "You Win!"
    elif player_score == dealer_score:
        return "You Lose!"
    elif player_score > 21:
        return "Bust, You Lose!"
    elif dealer_score > 21:
        return ("Dealer Bust, You win!")
    elif player_score > dealer_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_blackjack():
    game_over = False
    while not game_over:
        player = [] 
        dealer = [] 
        dealer_score = 0
        player_score = 0

        dealer.append(deal()) 
        dealer.append(deal())
        print(f"The dealers cards are {dealer[0]} and {dealer[1]}.")
        player.append(deal())
        player.append(deal())
        print(f"Your cards are {player[0]} and {player[1]}.")

        while True:
            another_card = input(f"Hit? Type 'Y' for yes or 'N' for no. ").lower()
            while another_card not in ['y', 'n']:
                another_card = input("Please type 'Y' or 'N': ").lower()

            if another_card == 'y':
                player.append(deal())
                print(f"{player[-1]}") 
                player_score = calculate_total(player)
                if player_score >= 21:
                    break
            else:
                break

        dealer_score = calculate_total(dealer) 
        while dealer_score <= 16:
            dealer.append(deal())
            dealer_score = calculate_total(dealer) 

        game_over = True

        print(f"Your hand was {player}, and your score was {player_score}.")
        print(f"The dealers hand was {dealer}, and the score was {dealer_score}.")
        print(compare_player_dealer(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
        play_blackjack()
