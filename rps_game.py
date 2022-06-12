import random
print('''welcom to Rock Paper Scissors Game!
This is a simple 2-Player game, where at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules below:

RULES:
* Rock wins against scissors.
* Scissors win against paper.
* Paper wins against rock.

Let's START!

''')
r = "Rock"
p = "Paper"
s = "Scissors"

options = [r, p, s]


def init():

    is_selected_option = False

    while is_selected_option == False:

        user_input = input('''Start by selecting a choice below:
R. Rock
P. Paper
S. Scissor

Type R for Rock, P for Paper and S for Scissors: 

''').lower()

        if user_input == "r":
            user_choice = options[0]
            computers_choice = random.choice(options)
            print(f"Player ({user_choice}) : CPU ({computers_choice})")

            if computers_choice == options[2]:
                print("You won!")
                is_selected_option = True

            elif computers_choice == options[1]:
                print("You lose!")
                is_selected_option = True

            elif computers_choice == user_choice:
                print("It is a tie! Please start again.\n")

        elif user_input == "p":
            user_choice = options[1]
            computers_choice = random.choice(options)
            print(f"Player ({user_choice}) : CPU ({computers_choice})")

            if computers_choice == options[0]:
                print("You won!")
                is_selected_option = True

            elif computers_choice == options[2]:
                print("You lose!")
                is_selected_option = True

            elif computers_choice == user_choice:
                print("It is a tie! Please start again.\n")

        elif user_input == "s":
            user_choice = options[2]
            computers_choice = random.choice(options)
            print(f"Player ({user_choice}) : CPU ({computers_choice})")

            if computers_choice == options[1]:
                print("You won!")
                is_selected_option = True

            elif computers_choice == options[0]:
                print("You lose!")
                is_selected_option = True

            elif computers_choice == user_choice:
                print("It is a tie! Please start again.\n")

        else:
            print('''You've selected an invalid option. Please try again

**************************************************

''')


init()
