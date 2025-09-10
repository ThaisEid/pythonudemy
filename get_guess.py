def get_guess():
    guess = int(input("Enter a Guess "))
    return guess

def main():
    guess = get_guess()
    if guess == 18:
       print("Correct!")
    else:
       print("Incorrect!")

main()

