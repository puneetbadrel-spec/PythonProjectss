import random
user_score = 0
computer_score = 0
options = ['Rock','Paper','Scissor']


while True:
    user_input = input("Chose Rock/Paper/Scissor or 'q' to Quit : ")
    if user_input == 'q':
        break
    elif user_input not in options:
        continue
    random_num = random.randint(0,2)
    computer_pick = options[random_num]
    print("computer pick", computer_pick + ".")

    if user_input =='Rock' and computer_pick  =='Scissor' :
        print("You win")
        user_score += 1
        continue

    elif user_input == 'Paper' and computer_pick == 'Rock':
        print("You win")
        user_score += 1
        continue
    elif user_input == 'Scissor' and computer_pick == 'Paper':
            print("You win")
            user_score += 1
            continue
    else:
        print("You Lose")
        computer_score += 1
        continue

print("You win ", user_score , "times")
print("Computer win ", computer_score , "times")

print("Good bye")


