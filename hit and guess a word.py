guessing_word = "Rome"
guesses = ""
maximum_guesses = 3
number_of_guesses = 0

print("The Capital City of ITALY is")
print("Please write the first letter in capital")
while guesses != guessing_word:
   
    if number_of_guesses == 0:
        print("Hint:Rser")
        guesses = input("Guess the capital:")
        number_of_guesses += 1
    elif number_of_guesses == 1:
        print("Hint:Rodr")
        print("Guess the capital")
        guesses = input("Guess again: ")
        number_of_guesses += 1
    elif number_of_guesses == 2:
        print("Guess the capital ")
        guesses = input("Guess again: ")
        break
if(guesses==guessing_word):
    print("You have won")

else:
    print("you have lost")