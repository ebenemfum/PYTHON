# # # ##For Loop
import random;
# # # ## for item in list_of_items:
# # # #       do something:

# # # fruits = ["apple","peach","pear"]
# # # for fruit in fruits:
# # #     print(fruit)
# # # scores = [87, 73, 65, 92, 48, 77, 81, 69, 54, 100, 39, 62, 85, 71, 58, 93, 44, 66, 79, 88, 51, 60, 90, 83, 75, 68, 57, 46, 99, 74]
# # # total_exam_score = sum(scores)
# # # print(total_exam_score)

# # # summ = 0

# # # for score in scores:
# # #     summ += score

# # # print(summ)
# # scores = [87, 73, 65, 92, 48, 77, 81, 69, 54, 100, 39, 62, 85, 71, 58, 93, 44, 66, 79, 88, 51, 60, 90, 83, 75, 68, 57, 46, 99, 74, 10000]
# # max = 0
# # for score in scores:
# #     if(score>max):
# #         max = score
# # print (max)
# number=0
# for number in range(1,100):
#     print(f"{number}\n")    
##Password Generator
combined_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?', '~', '`']

# Ask user for input on the number of characters they want for each type
num_alphabets = int(input("How many alphabets (letters) would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

#Password
password = []
# Add random alphabets (lowercase and uppercase)
for _ in range(num_alphabets):
    char = random.choice(combined_alphabets)
    password.append(char)

# Add random numbers
for _ in range(num_numbers):
    char = random.choice(numbers)
    password.append(char)

# Add random symbols
for _ in range(num_symbols):
    char = random.choice(password_symbols)
    password.append(char)
    
# Shuffle the password list to make it more random
#6
random.shuffle(password)

# Convert the list to a string
final_password = ''.join(password)

print("Your randomly generated password is:", final_password)