logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
scores_dictionary = {"ace": 11, "2": 2,"3": 3 ,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"jack":10,"queen" :10,"king":10}
import random
card_first_user = random.randint(0,len(scores_dictionary)-1)
card_first_comp = random.randint(0,len(scores_dictionary)-1)
score_user = scores_dictionary[list(scores_dictionary)[card_first_user]]
score_comp = scores_dictionary[list(scores_dictionary)[card_first_comp]]
print(f"Your first hand is {score_user} and your card is {card_first_user}")
print(f"The first hand of computer is {score_comp}")
end_of_game = False
def end_game(score_comp,score_user):
    if score_comp > score_user:
        print(f"The score of computer is {score_comp}")
        end_of_game = True
        print("You lost!")
        print("Thanks for playing!")
    elif score_user > score_comp:
        print(f"The score of computer is {score_comp}")
        end_of_game = True
        print("You won!")
        print("Thanks for playing!")
def ace(score_comp,score_user):
    if score_user or score_comp > 21:
        scores_dictionary["ace"] = 1
def blackjack(score_comp,score_user):
    blackjack_condition = scores_dictionary["ace"] + 10
    if score_user == blackjack_condition:
        end_of_game = True
        print("You loose!")
        print("Thanks for playing!")
    elif score_comp == blackjack_condition:
        end_of_game = True
        print("You won!")
        print("Thanks for playing!")
while score_comp < 16:
    round_2_c = random.randint(0,len(scores_dictionary)-1)
    score_comp += scores_dictionary[list(scores_dictionary)[round_2_c]]
for i in range(0,2):
    ask = input("Do you want to draw another card?Type y for yes and n for no\n")
    if ask == "y":
        round_2 = random.randint(0,len(scores_dictionary)-1)
        score_user += scores_dictionary[list(scores_dictionary)[card_first_user]]
        ace(score_comp,score_user)
        blackjack(score_comp,score_user)
        print(f"Your score now is {score_user}")
    elif ask == "n":
        end_of_game = True
if end_of_game == True:
    end_game(score_comp,score_user)





