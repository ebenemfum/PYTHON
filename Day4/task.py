# # # ##Randomization
import random
# # # # random_integer = random.randint(1,10)
# # # random_number_0_to_1 = random.random()
# # # print(random_number_0_to_1)

# # #A program which either prints out Heads or Tails.
# # luck=random.randint(0,1)
# # print(luck)
# # if(luck==1):
# #     print("Heads")
# # else:
# #     print("Tails")

# ##Lists
# states = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
#     "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
#     "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
#     "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
#     "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
#     "New Hampshire", "New Jersey", "New Mexico", "New York", 
#     "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
#     "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
#     "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
#     "West Virginia", "Wisconsin", "Wyoming"
# ]

# print(states[-1])

# friends = [ "James", "Hannah", "Kwams", "DJ"]
# print(random.choice(friends))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])



# Defining the rock, paper, and scissors ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store them in a list
game_images = [rock, paper, scissors]

# Define a variable for the computer's choice (random selection from the list)
computer_choice = random.choice(game_images)

# Ask the user for their choice (rock, paper, or scissors)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Convert user choice to ASCII art
if user_choice == "rock":
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
elif user_choice == "scissors":
    user_choice = scissors
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    exit()

# Print both choices
print("\nYour choice:")
print(user_choice)
print("\nComputer's choice:")
print(computer_choice)

# Compare the choices using rock-paper-scissors rules
if user_choice == computer_choice:
    print("\nIt's a tie!")
elif (user_choice == rock and computer_choice == scissors) or \
     (user_choice == paper and computer_choice == rock) or \
     (user_choice == scissors and computer_choice == paper):
    print("\nYou win!")
else:
    print("\nYou lose!")
