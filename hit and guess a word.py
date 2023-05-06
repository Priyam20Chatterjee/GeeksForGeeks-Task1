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