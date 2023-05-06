guessing_word = "Rome"
guesses = ""
print("The Capital City of ITALY is")
print("NOTE : Please write the first letter in capital\n")


hint = ['Rser', 'Rodr', 'Ruge']
for i in range(3):
    print('HINT : ', hint[i])
    guesses = input("Guess the capital:")
    if guesses == guessing_word:
        print("you WON")
        break
    print()
else:
    print("you LOST")


# Your old Code
# maximum_guesses = 3
# number_of_guesses = 0

# while guesses != guessing_word:
#     if number_of_guesses == 0:
#         print("Hint:Rser")
#         guesses = input("Guess the capital:")
#         number_of_guesses += 1
#     elif number_of_guesses == 1:
#         print("Hint:Rodr")
#         print("Guess the capital")
#         guesses = input("Guess again: ")
#         number_of_guesses += 1
#     elif number_of_guesses == 2:
#         print("Hint:Ruge")
#         print("Guess the capital ")
#         guesses = input("Guess again: ")
#         break
# if (guesses == guessing_word):
#     print("You have won")

# else:
#     print("you have lost")
