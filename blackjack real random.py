# imports random module
from random import randint
# sets game_continue to true and assigns following variables to 0
game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
num_ties = 0

# controls the number of games the player will play
while game_continue:

    # prints game number message
    game_num += 1
    print(f"START GAME #{game_num}")
    print()

    # deals a card to the player automatically
    player_hand = 0
    dealer_hand = 0
    card = randint(1, 13)
    if card == 1:
        print("Your card is a ACE!")
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10

    # adds card number to the player's hand value
    player_hand = 0
    player_hand += card
    print(f"Your hand is: {player_hand}")
    no_winner = True

# prints menu for player to select from
    while no_winner:
        print()
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()
        menu_select = int(input("Choose an option: "))
        print()

        # gives player another card and adds it to their hand
        if menu_select == 1:
            card = randint(1, 13)
            # checks if player's hand is == 21 or > 21 before card is given
            if player_hand == 21:
                print()
                print("BLACKJACK! You win!")
                print()
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print()
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                no_winner = False
            # checks what the card the player received
            elif card == 1:
                print("Your card is a ACE!")
                player_hand += card
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
                player_hand += card
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
                player_hand += card
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
                player_hand += card
            elif card == 13:
                print("Your card is a KING!")
                card = 10
                player_hand += card
            print(f"Your hand is: {player_hand}")
            # checks if player's hand is == 21 or > 21 after card is given
            if player_hand == 21:
                print()
                print("BLACKJACK! You win!")
                print()
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print()
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                no_winner = False
            continue

        # deals a card to the dealer
        elif menu_select == 2:
            card2 = randint(1, 13)
            if card2 == 1:
                dealer_hand += card2
            elif 2 <= card2 <= 10:
                dealer_hand += card2
            elif card2 == 11:
                dealer_hand += 10
            elif card2 == 12:
                dealer_hand += 10
            elif card2 == 13:
                dealer_hand += 10
            while dealer_hand < player_hand:
                card2 = randint(1, 13)
                if card2 == 1:
                    dealer_hand += card2
                elif 2 <= card2 <= 10:
                    dealer_hand += card2
                elif card2 == 11:
                    dealer_hand += 10
                elif card2 == 12:
                    dealer_hand += 10
                elif card2 == 13:
                    dealer_hand += 10
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()
            # checks if dealer or player won or if they tied
            if dealer_hand > 21:
                print("You win!")
                print()
                player_wins += 1
                no_winner = False
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                print()
                num_ties += 1
                no_winner = False
            elif dealer_hand < player_hand:
                print("You win!")
                print()
                player_wins += 1
                no_winner = False
            elif dealer_hand > player_hand:
                print("Dealer wins!")
                print()
                dealer_wins += 1
                no_winner = False

        # displays stats for player
        elif menu_select == 3:
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {num_ties}")
            game_num2 = player_wins + dealer_wins + num_ties
            print(f"Total # of games played is: {game_num2}")
            wins_percent = float((player_wins / game_num2) * 100)
            print(f"Percentage of Player wins: {wins_percent:.1f}%")

        # exits game
        elif menu_select == 4:
            no_winner = False
            game_continue = False

        # displays error message if player inputs something other than 1, 2, 3, or 4
        elif menu_select != range(1, 5):
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
