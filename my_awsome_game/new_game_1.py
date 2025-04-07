import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Välkommen till Gissa Numret-spelet!")
    print("Jag har valt ett nummer mellan 1 och 100. Kan du gissa vilket?")
    
    while True:
        try:
            guess = int(input("Din gissning: "))
            attempts += 1
            
            if guess < number:
                print("För lågt! Försök igen.")
            elif guess > number:
                print("För högt! Försök igen.")
            else:
                print(f"Grattis! Du gissade rätt på {attempts} försök.")
                break
        except ValueError:
            print("Vänligen ange en giltig siffra.")

if __name__ == "__main__":
    guess_number()